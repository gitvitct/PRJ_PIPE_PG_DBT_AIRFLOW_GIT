# 🚀 Sales Pipeline - Airflow + PostgreSQL + dbt + Docker ###########################

Projeto de pipeline de dados utilizando:

- Apache Airflow
- PostgreSQL
- dbt
- Docker / Docker Compose
- Python

O objetivo do projeto é simular uma pipeline moderna de engenharia de dados com:

1. Criação automática de tabelas
2. Geração e carga de vendas
3. Validação de dados
4. Registro de logs
5. Tratamento de registros inválidos (Deadletter)
6. Transformações analíticas com dbt

---

# 📌 Fluxo ##########################################################################

      Gerar vendas
            ↓
      Validar vendas
            ↓
      Válida?
      ├─ SIM → INSERT PostgreSQL
      └─ NÃO → Deadletter + Log
            ↓
      Commit
            ↓
      Salvar deadletter.json


# 📌 Arquitetura #####################################################################

PRJ_PIPE_PG_DBT_AIRFLOW/
│
├── dags/
│   └── sales_pipeline.py
│
├── data/
│   └── deadletter/
│       └── deadletter.json
│
├── dbt_project/
│   ├── dbt_project.yml
│   ├── logs/dbt.log
│   ├── models/
│   └── profiles.yml
│
├── Dockers/
│   ├── docker-compose.yml
│   └── Dockerfile
│
├── logs/
│   └── pipeline.log
│
├── scripts/
│   ├── create_tables.py
│   ├── db_connection.py
│   ├── load_sales.py
│   ├── logger_config.py
│   ├── make_deadletter_json.py
│   └── validation.py
└── tests
├── __init__.py
├── __pycache__
├── airflow
│   ├── test_dag_integrity.py
│   ├── test_dag_loaded.py
│   └── test_dag_tasks.py
├── conftest.py
├── dbt
│   ├── test_dbt_mart.py
│   ├── test_dbt_models.py
│   └── test_dbt_staging.py
├── e2e
│   └── test_end_to_end_pipeline.py
├── integration
│   ├── __init__.py
│   ├── __pycache__
│   ├── test_create_tables.py
│   ├── test_insert_raw_sales.py
│   ├── test_load_sales.py
│   └── test_postgres_connection.py
└── unit
│    ├── __init__.py
│    ├── __pycache__
│    ├── test_db_connection.py
│    ├── test_deadletter.py
│    ├── test_logger.py
│    └── test_validation.py
│
│
└── README.md



# 🧪 Validação de Dados #############################################################

A pipeline possui regras simples de qualidade:

      1- Valor da venda não pode ser negativo
      2- Campos obrigatórios devem existir
      3- Registros inválidos são enviados para: data/deadletter/deadletter.json
      

# 📝 Logs ###########################################################################

Os logs da pipeline são armazenados em:

logs/pipeline.log

Exemplo:

2026-05-20 10:00:00 - INFO - Iniciando carga de vendas




# 📝 tests ###########################################################################
# docker compose exec airflow-webserver pytest -v -p no:cacheprovider

PRJ_PIPE_PG_DBT_AIRFLOW/
│
.
├── __init__.py
├── __pycache__
├── airflow
│   ├── test_dag_integrity.py
│   ├── test_dag_loaded.py
│   └── test_dag_tasks.py
├── conftest.py
├── dbt
│   ├── test_dbt_mart.py
│   ├── test_dbt_models.py
│   └── test_dbt_staging.py
├── e2e
│   └── test_end_to_end_pipeline.py
├── integration
│   ├── __init__.py
│   ├── __pycache__
│   ├── test_create_tables.py
│   ├── test_insert_raw_sales.py
│   ├── test_load_sales.py
│   └── test_postgres_connection.py
└── unit
    ├── __init__.py
    ├── __pycache__
    ├── test_db_connection.py
    ├── test_deadletter.py
    ├── test_logger.py
    └── test_validation.py



