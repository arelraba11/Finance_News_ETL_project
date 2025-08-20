from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    "owner": "arel",
    "depends_on_past": False,
    "retries": 0,
}

with DAG(
    dag_id="dag_news_etl",
    start_date=datetime(2025, 8, 1),
    schedule_interval="0 7 * * *",
    default_args=default_args,
    catchup=False,
    tags=["etl","news"],
) as dag:

    extract = BashOperator(
        task_id="extract_news",
        bash_command="python -m src.application.extract_job",
    )

    transform = BashOperator(
        task_id="transform_sentiment",
        bash_command="python -m src.application.transform_job",
    )

    load = BashOperator(
        task_id="load_postgres",
        bash_command="python -m src.application.load_job",
    )

    extract >> transform >> load
