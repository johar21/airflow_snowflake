from airflow import DAG
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator
from datetime import datetime

# Define the SQL command to create your table
# This example creates a permanent table by default
CREATE_TABLE_SQL = """
    CREATE OR REPLACE TABLE customers (
        customer_id INT,
        name STRING,
        email STRING,
        signup_date DATE
    );
"""

with DAG(
    dag_id='create_snowflake_table',
    start_date=datetime(2026, 1, 1),
    schedule="0 0 * * *",  # Set your desired schedule
    catchup=False
) as dag:

    create_table_task = SnowflakeOperator(
        task_id='create_customers_table',
        sql=CREATE_TABLE_SQL,
        snowflake_conn_id='snowflake_default',                   # Optional: Overrides connection setting
    )
