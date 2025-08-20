CREATE TABLE IF NOT EXISTS news (
  id BIGSERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  published_at TIMESTAMPTZ NOT NULL,
  source VARCHAR(64) NOT NULL,
  url TEXT,
  sentiment_label VARCHAR(8),
  sentiment_score REAL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS ix_news_published_at ON news(published_at);
CREATE INDEX IF NOT EXISTS ix_news_source ON news(source);
