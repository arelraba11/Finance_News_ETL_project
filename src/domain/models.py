from pydantic import BaseModel, HttpUrl
from datetime import datetime

class NewsArticle(BaseModel):
    title: str
    published_at: datetime
    source: str
    url: HttpUrl | None = None

class SentimentResult(BaseModel):
    label: str   # 'pos' | 'neu' | 'neg'
    score: float # -1.0 .. 1.0
