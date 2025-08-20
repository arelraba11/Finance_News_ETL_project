# Finance News ETL (MVP)

Minimal ETL pipeline to pull financial market news, apply sentiment scoring, and load into Postgres.
Visualization and analysis through Metabase.

## Services
•   Postgres → localhost:5432
•	Adminer → http://localhost:8081
•	Metabase → http://localhost:3000

## Quickstart
•   Install Docker Desktop.
•   Copy .env.example → .env and set values (DB_URL, NEWSAPI_KEY).
•   Start services: `docker compose up -d`
•   Create & activate a virtualenv (Python 3.11+).
•   Install deps: `pip install -r requirements.txt`
•   Run ETL jobs in sequence:
`python -m src.application.extract_job
python -m src.application.transform_job
python -m src.application.load_job`
•   Open Metabase → connect to Postgres → build dashboards from news table.

## Example Dashboards
•	Sentiment distribution (Positive/Negative/Neutral).
•	News volume over time.
•	Sources breakdown (which sites are more positive/negative).

## Roadmap
•	Add Airflow orchestration.
•	Schedule daily ETL runs.
•	Enrich news with tickers and market data.
