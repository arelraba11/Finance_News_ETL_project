import os, csv
from datetime import date
import pandas as pd
from ..infrastructure.sentiment.vader_analyzer import VaderAnalyzer

IN_DIR = "data"
OUT_DIR = "data"
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    # pick today's file by default
    today = date.today().isoformat()
    in_path = os.path.join(IN_DIR, f"news_{today}.csv")
    if not os.path.exists(in_path):
        # fallback to latest csv in data
        csvs = [f for f in os.listdir(IN_DIR) if f.endswith(".csv")]
        if not csvs:
            raise FileNotFoundError("No CSV found in data/. Run extract_job first.")
        csvs.sort()
        in_path = os.path.join(IN_DIR, csvs[-1])

    df = pd.read_csv(in_path)
    analyzer = VaderAnalyzer()
    labels, scores = [], []
    for t in df["title"].fillna(""):
        res = analyzer.analyze(t)
        labels.append(res.label)
        scores.append(res.score)
    df["sentiment_label"] = labels
    df["sentiment_score"] = scores

    out_path = os.path.join(OUT_DIR, os.path.basename(in_path).replace(".csv", "_with_sentiment.parquet"))
    df.to_parquet(out_path, index=False)
    print(f"Wrote {len(df)} rows with sentiment to {out_path}")

if __name__ == "__main__":
    main()
