from typing import Iterable, Optional, Tuple
from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
from ...config.settings import settings
from ...domain.models import NewsArticle, SentimentResult

class PostgresLoader:
    def __init__(self, engine: Engine | None = None):
        self.engine = engine or create_engine(settings.db_url, pool_pre_ping=True)

    def load_news(self, items: Iterable[Tuple[NewsArticle, Optional[SentimentResult]]]) -> int:
        sql = text(
            """
            INSERT INTO news(title, published_at, source, url, sentiment_label, sentiment_score)
            VALUES (:title, :published_at, :source, :url, :sentiment_label, :sentiment_score)
            """
        )
        count = 0
        with self.engine.begin() as conn:
            for article, sent in items:
                conn.execute(sql, {
                    "title": article.title,
                    "published_at": article.published_at,
                    "source": article.source,
                    "url": str(article.url) if article.url else None,
                    "sentiment_label": sent.label if sent else None,
                    "sentiment_score": sent.score if sent else None,
                })
                count += 1
        return count
