import os
import pandas as pd
from sqlalchemy import create_engine, text
from ..config.settings import settings

def main():
    # pick latest parquet in data/
    files = [f for f in os.listdir("data") if f.endswith("_with_sentiment.parquet")]
    if not files:
        raise FileNotFoundError("No parquet with sentiment found. Run transform_job first.")
    files.sort()
    path = os.path.join("data", files[-1])

    df = pd.read_parquet(path)
    engine = create_engine(settings.db_url, pool_pre_ping=True)
    # write to 'news' table
    with engine.begin() as conn:
        rows = df.to_dict(orient="records")
        insert_sql = text("""
            INSERT INTO news(title, published_at, source, url, sentiment_label, sentiment_score)
            VALUES (:title, :published_at, :source, :url, :sentiment_label, :sentiment_score)
        """)
        for r in rows:
            conn.execute(insert_sql, r)
    print(f"Inserted {len(df)} rows into Postgres")

if __name__ == "__main__":
    main()
