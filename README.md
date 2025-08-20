# Finance News ETL (MVP)

Minimal ETL to pull financial news, score sentiment, and load to Postgres. UI via Metabase.

## Services
- Postgres: `localhost:5432`
- Adminer: http://localhost:8081
- Metabase: http://localhost:3000

## Quickstart
1. Install Docker Desktop
2. Copy `.env.example` to `.env` and fill values (DB + NEWSAPI_KEY)
3. `docker compose up -d` (from project root)
4. Create and activate a virtualenv for Python 3.11+
5. `pip install -r requirements.txt`
6. Run `python src/application/extract_job.py` (first run will create a CSV)
7. Run `python src/application/transform_job.py`
8. Run `python src/application/load_job.py`
9. Open Metabase and connect to Postgres; build the dashboard queries from the plan.

Airflow will be added after MVP is working.
