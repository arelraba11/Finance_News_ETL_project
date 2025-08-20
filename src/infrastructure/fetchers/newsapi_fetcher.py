from typing import Iterable
import requests
from datetime import datetime
from pydantic import HttpUrl
from ...config.settings import settings
from ...domain.models import NewsArticle

BASE_URL = "https://newsapi.org/v2/everything"

class NewsApiFetcher:
    def __init__(self):
        if not settings.newsapi_key:
            raise RuntimeError("NEWSAPI_KEY missing. Put it in your .env")
        self.api_key = settings.newsapi_key

    def fetch(self, query: str, from_iso: str, to_iso: str) -> Iterable[NewsArticle]:
        params = {
            "q": query,
            "from": from_iso,
            "to": to_iso,
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": 100,
            "apiKey": self.api_key,
        }
        r = requests.get(BASE_URL, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        for item in data.get("articles", []):
            title = item.get("title") or ""
            published_at = item.get("publishedAt") or datetime.utcnow().isoformat()
            source = (item.get("source") or {}).get("name") or "unknown"
            url = item.get("url")
            yield NewsArticle(title=title, published_at=published_at, source=source, url=url)
