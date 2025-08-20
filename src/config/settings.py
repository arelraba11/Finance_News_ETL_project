from __future__ import annotations

from pydantic import BaseModel
import os
from dotenv import load_dotenv
load_dotenv()
class Settings(BaseModel):
    db_url: str = os.getenv("DB_URL", "postgresql+psycopg://etl:etlpass@localhost:5432/newsdb")
    newsapi_key: str | None = os.getenv("NEWSAPI_KEY")
    env: str = os.getenv("ENV", "dev")

settings = Settings()
