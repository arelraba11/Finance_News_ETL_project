from datetime import datetime, timedelta, timezone
import csv, os
from ..infrastructure.fetchers.newsapi_fetcher import NewsApiFetcher

OUT_DIR = "data"
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    fetcher = NewsApiFetcher()
    to_ts = datetime.now(timezone.utc)
    from_ts = to_ts - timedelta(days=3)  # הרחב חלון ל-3 ימים
    to_iso = to_ts.isoformat()
    from_iso = from_ts.isoformat()

    rows = []
    for art in fetcher.fetch(query="(stock OR stocks OR market OR earnings OR wall street)", from_iso=from_iso,
                             to_iso=to_iso):
        rows.append([art.title, art.published_at, art.source, art.url or ""])

    out_path = os.path.join(OUT_DIR, f"news_{to_ts.date().isoformat()}.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["title", "published_at", "source", "url"])
        w.writerows(rows)
    print(f"Wrote {len(rows)} rows to {out_path}")

if __name__ == "__main__":
    main()
