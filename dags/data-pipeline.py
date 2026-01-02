import sys
from pathlib import Path
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from scripts.bronze_ingest import run_bronze_ingestion

with DAG(dag_id="data-pipeline", start_date=datetime(2026, 1, 1), schedule="0 0 * * *") as dag:
    
    bronze = PythonOperator(
        task_id="bronze_ingest",
        python_callable=run_bronze_ingestion,
    )