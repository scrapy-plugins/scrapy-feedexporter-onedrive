import logging

import requests
from scrapy.exceptions import NotConfigured
from scrapy.extensions.feedexport import BlockingFeedStorage, build_storage

logger = logging.getLogger(__name__)

GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0"


class OneDriveFeedStorage(BlockingFeedStorage):
    def __init__(self, uri, access_token=None, *, feed_options=None):
        if not access_token:
            raise NotConfigured("Missing ONEDRIVE_ACCESS_TOKEN")

        if feed_options and feed_options.get("overwrite", True) is False:
            raise NotConfigured(
                "OneDriveFeedStorage does not support appending to files. Please "
                "remove the overwrite option from your FEEDS setting or set it to True."
            )

        self.session_headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        self.file_path = uri.replace('onedrive://', '')
        self.session_url = self._create_session(self.file_path)

    @classmethod
    def from_crawler(cls, crawler, uri, *, feed_options=None):
        return build_storage(
            cls,
            uri,
            access_token=crawler.settings.get("ONEDRIVE_ACCESS_TOKEN"),
            feed_options=feed_options,
        )

    def _create_session(self, file_path):
        session_endpoint = f"/me/drive/root:/{file_path}:/createUploadSession"
        response = requests.post(GRAPH_API_ENDPOINT + session_endpoint, headers=self.session_headers)
        return response.json()['uploadUrl']

    def _store_in_thread(self, file):
        file.seek(0)
        content = file.read()
        content_range = f"bytes 0-{len(content) - 1}/{len(content)}"
        headers = {'Content-Length': str(len(content)), 'Content-Range': content_range}
        response = requests.put(self.session_url, headers=headers, data=content)
        if not response.ok:
            raise NotConfigured(f"Failed to upload the file to OneDrive: {response.content}")
        logger.info(f"Feed file uploaded to OneDrive: {response.json()['webUrl']}")
        file.close()
