import sys
from pathlib import Path
from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

from scripts.bronze_ingest import read_data

with DAG(dag_id="data-pipeline", start_date=datetime(2026, 1, 1), schedule="*/1 * * * *") as dag:
    
    bronze = PythonOperator(
        task_id="bronze_ingest",
        python_callable=read_data,
    )