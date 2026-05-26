FROM apache/airflow:2.8.1

USER root

RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev

# Diretórios dbt
RUN mkdir -p /opt/airflow/dbt_project/logs && \
    chmod -R 777 /opt/airflow/dbt_project

# Logs alternativos
RUN mkdir -p /tmp/dbt_logs && \
    chmod -R 777 /tmp/dbt_logs

USER airflow

RUN pip install --no-cache-dir \
    dbt-core \
    dbt-postgres \
    pytest