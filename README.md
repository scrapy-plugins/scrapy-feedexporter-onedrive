# OneDrive Feed Storage
[Storage backend](https://docs.scrapy.org/en/latest/topics/feed-exports.html#storage-backends) to store feeds in [Microsoft OneDrive](https://www.microsoft.com/en-us/microsoft-365/onedrive/online-cloud-storage). 
- URI scheme: `onedrive`
- Example URI: `onedrive://path/to/store/the_feed_file.csv`

## Requirements
- Python >= 3.8
- Scrapy >= 2.11.1

## Installation
Install the OneDrive Feed Storage for Scrapy via pip:

```
pip install git+https://github.com/scrapy-plugins/scrapy-feedexporter-onedrive
```

## Configuration and Usage
Follow these steps to use the OneDrive Feed Storage with Scrapy:

1. Add this storage backend in your Scrapy project's settings FEED_STORAGES dictionary, as follows:

```
# settings.py
FEED_STORAGES = {
    'onedrive': 'scrapy_onedrive_exporter.onedrive_exporter.OneDriveFeedStorage'
}
```

2. Configure authentication by providing an access token with permission to read and write the user's OneDrive files, as exemplified below. To obtain the access token using the standard `OAuth 2.0` authorization framework of the OneDrive API, please follow the steps described in the [Microsoft OneDrive API documentation](https://learn.microsoft.com/en-us/onedrive/developer/rest-api/getting-started/graph-oauth?view=odsp-graph-online).

```python
# settings.py
ONEDRIVE_ACCESS_TOKEN = 'EwBoA8l6BAAUs5%2bHQn0N%2bh2FxWzLS31ZgQVuHsYAAQe0m4RTofw7c6jCDsPCN5Hq6RYwdPsQxxJZKLJBFXt8SCoSJ3BeN36l/YoTBHaBNjyI8KmYtr1AcYx93wqvojL4g1PNR%2bLRqFSzQe2PyhumzMsGGbFqmZzNtzluaQSm3rdtSorbriPL3AFuWcIpo0AnD7iS666OLolARAnCpqLHY2sNyM6SUIo3DZgLEUrJwS6S05YWAQQvjuNiQsSG49r8jmHJ6O9cDbsXXjpTku3UtSN3558cuOordIj5mQQ4evJ1dDPRI3L18%2bTgilmAqOcz6R%2b%2b5YhUk3cU854L9gZe86WsRjfs9ztTvwc3IpQD4ICoJ94L1kNGZjlKRQBfBsMDZgAACF9C2ej1pyckOALbj9o2vGrEU/7DpKSmjCyf7IaVcbzohSH1exYk4qmovogcIcHx%2bqjklQyosJsHt5k1RzXg69GS/9hde9h%2blBSx3d30ceDO309jrTm2S9lG9Qe5PeYA6G062Ros0ms%2btfxmL3NJTz/eIWWIYICoFjpd85WGTpG1qAWvF6UY%2bJZbME2x8ewM9oVGQfHY4WDWcquMEU/UYpdlxlV3RHcv/tqKoqR1jqJE6A45fo7u%2bPGfBlg7HQktVZ%2bnT6gK054xq6dbEGByRunZdGHZs3ThpC40wCcOHzuK7Z9GVhbnRDIeMGCPofCVkn/z7uuNgowAEAadfOZyuGRLTwNrTiG70mo5kub5o3tX5lLUdrkbgbK6riBK8rsN6tlZUENymMU95A8svBqlsm27fxDk2D/S2ltEmQLBlULKXZPmpcIfHUNAoum%2bhfVPQZoN5nzVa3d/7RYDT0S4%2bd/5jsV5yoem0/Yd8VnclvJs14UC4Eq%2bw7L3r314rAMojg5rgbMhfmei2PharkNctvn%2b5j8Ay35YbFVknhLrj1lY5I1GcCX4J5qADbdn8l%2b1fg3B3H3wVV9yo1EjFaRW4LObrOwTcjQRPkC4FMbDbpSitXeRaSiNrNZuVzSXgUcHIcGTUXsYz89c7n55bHQDKLtWThXT%2bUEgNR/8%2bIqpdBukM1S78h4EOZo8mz5sj%2b7znPRAqyCedrLLL5bleq2viUCx3dFThnQ6ChxV64E508C96VACj4PofHpG2sfB6PJIrP0MfgI%3d'
```

3. Configure in Scrapy FEEDS settings by specifying the URI with the path to which the feed will be exported on OneDrive:

```python
# settings.py
FEEDS = {
    "onedrive://path/to/store/the_feed_file.csv": {
        "format": "csv",
        "overwrite": True  # default
    }
}
```

## Limitations
- The `overwrite` feed option is fixed to `True`, meaning each export will replace the existing file at the specified URI. Use with caution to avoid unintended data loss.
- This storage backend uses [delayed file delivery](https://docs.scrapy.org/en/latest/topics/feed-exports.html#delayed-file-delivery).








