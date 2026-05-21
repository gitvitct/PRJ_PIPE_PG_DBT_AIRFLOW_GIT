FROM apache/airflow:2.8.1

USER root

RUN apt-get update && apt-get install -y gcc python3-dev

USER airflow

RUN pip install --no-cache-dir dbt-core dbt-postgres