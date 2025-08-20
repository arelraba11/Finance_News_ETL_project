# Finance News ETL (MVP)

Minimal ETL pipeline to pull financial market news, apply sentiment scoring, and load into Postgres.  
Visualization and analysis through Metabase.

---

## Services
- **Postgres** → `localhost:5432`
- **Adminer** → [http://localhost:8081](http://localhost:8081)
- **Metabase** → [http://localhost:3000](http://localhost:3000)

---

## Quickstart
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop).
2. Copy `.env.example` → `.env` and set values (`DB_URL`, `NEWSAPI_KEY`).
3. Start services: `docker compose up -d`
4. Create & activate a virtualenv (Python 3.11+).
5. Install deps: `pip install -r requirements.txt`
6. Run ETL jobs in sequence: `python -m src.application.extract_job
python -m src.application.transform_job
python -m src.application.load_job`
7. Open Metabase → connect to Postgres → build dashboards from the news table.
