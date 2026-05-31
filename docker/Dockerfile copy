FROM apache/airflow:2.8.1

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

RUN mkdir -p /opt/airflow/logs \
    /opt/airflow/dbt_project/logs \
    /tmp/dbt_logs

RUN chmod -R 777 /opt/airflow/logs \
    /opt/airflow/dbt_project \
    /tmp/dbt_logs

USER airflow

RUN pip install --no-cache-dir \
    dbt-core \
    dbt-postgres \
    pytest