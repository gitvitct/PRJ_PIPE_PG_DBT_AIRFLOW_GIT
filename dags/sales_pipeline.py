from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


# =========================
# DEFAULT ARGS
# =========================
default_args = {
    'owner': 'vitor',
    'retries': 3
}



# =========================
# DAG
# =========================

with DAG(
    dag_id='sales_pipeline',
    default_args=default_args,
    start_date=datetime(2026, 1, 1),
    schedule='@daily',
    catchup=False
) as dag:

    create_table = BashOperator(
        task_id='create_table',
        bash_command='python3 /opt/airflow/scripts/create_tables.py'
    )

    load_sales = BashOperator(
        task_id='load_sales',
        bash_command='python3 /opt/airflow/scripts/load_sales.py'
    )

    run_dbt = BashOperator(
        task_id='run_dbt',
        bash_command='cd /opt/airflow/dbt_project && dbt run'
    )

    create_table >> load_sales >> run_dbt