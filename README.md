# 🚀 Instalação e Execução – PRJ_PIPE_PG_DBT_AIRFLOW 


# 🧠 1. Visão Geral da Arquitetura 

Pipeline desenvolvido com Apache Airflow, dbt, PostgreSQL, Docker e Pytest, simulando um fluxo completo de ingestão, validação, transformação e disponibilização de dados para análise.

Este projeto implementa um pipeline moderno de dados em ambiente containerizado, integrando:

- PostgreSQL              → camada de armazenamento (DW + metadata Airflow)
- Apache Airflow          → orquestração do pipeline (DAGs)
- dbt (data build tool)   → transformação ELT (camada analítica)
- Docker Compose          → provisionamento completo do ambiente

Fluxo de dados:

      Postgres (raw_sales)
            ↓
      Airflow DAG (ingestão + validação)
            ↓
      dbt models (staging + marts)
            ↓
      tabelas analíticas (sales_summary)


# 📦 2. Pré-requisitos 

Antes da instalação:

      Docker Engine 20+
      Docker Compose v2+
      Git
      WSL2 (Windows) ou Linux/MacOS

Verificação:

      docker --version
      docker compose version
      git --version


# 📥 3. Clonagem do Repositório 

      git clone https://github.com/gitvitct/PRJ_PIPE_PG_DBT_AIRFLOW_GIT.git
      
      cd PRJ_PIPE_PG_DBT_AIRFLOW_GIT


# ⚙️ 4. Inicialização do Ambiente (Bootstrap) 

      - Permissão de execução:
            chmod +x bootstrap.sh

      - Execução do ambiente completo:
            ./bootstrap.sh


O que este script executa internamente:

      Criação do arquivo .env
      Definição de variáveis de ambiente:
      Postgres (AIRFLOW_DB + DW_DB)
      credenciais padrão (admin/admin)
      Build das imagens Docker (Airflow + dbt + Postgres)
      Inicialização do Docker Compose
      Criação de diretórios de logs e permissões
      Inicialização do Airflow metadata database
      Subida dos serviços:
      postgres
      airflow-webserver
      airflow-scheduler
      airflow-triggerer


# 🧩 5. Validação da Infraestrutura 

- Verificação dos containers:
      docker ps

- Esperado:
      postgres          (healthy)
      airflow-webserver (healthy)
      airflow-scheduler (healthy)
      airflow-triggerer (up)


# 🌐 6. Acesso à Interface Airflow 

- URL:

      http://localhost:8080

- Credenciais padrão:

      user: airflow
      password: airflow


# 🔄 7. Execução do Pipeline (DAG) 

No Airflow:

Ativar DAG:

      sales_pipeline
            Executar manualmente (Trigger DAG)

      Monitorar etapas:
            create_table      → criação de schema raw
            load_sales        → ingestão e validação de dados
            run_dbt           → transformação analítica


# 🗄️ 8. Validação no Banco de Dados 

- Acesso via CLI:

      docker exec -it docker-postgres-1 psql -U admin -d sales_dw
      psql -h postgres -p 5432 -U admin -d sales_dw


- Verificação:

      \dt
      SELECT * FROM public.raw_sales LIMIT 10;
      SELECT * FROM public.sales_summary;


            List of relations
      Schema |     Name      | Type  | Owner 
      --------+---------------+-------+-------
      public | raw_sales     | table | admin
      public | sales_summary | table | admin


# 🧪 9. Execução Manual do dbt (Opcional) 

- Acesso ao container:

      docker exec -it docker-airflow-webserver-1 bash

- Execução:

cd /opt/airflow/dbt_project

      dbt debug --profiles-dir .
      dbt run --profiles-dir .


# 📊 10. Monitoramento e Observabilidade 

- Logs Airflow:
      docker logs -f docker-airflow-scheduler-1
      docker logs -f docker-airflow-webserver-1

- Logs de pipeline customizado:
      tail -f logs/pipeline.log


# 🔁 11. Reset / Rebuild do Ambiente 

- Para reinicialização completa:

      docker compose down -v
      docker compose up --build








# 🚀 PRJ_PIPE_PG_DBT_AIRFLOW ################################################################################

Pipeline de Engenharia de Dados desenvolvido com Apache Airflow, dbt, PostgreSQL, Docker e Pytest, simulando um fluxo completo de ingestão, validação, transformação e disponibilização de dados para análise.

# 📋 Objetivo ################################################################################

O projeto tem como objetivo demonstrar a construção de um pipeline moderno de dados utilizando boas práticas de:

 - Orquestração de workflows
 - Qualidade de dados
 - ELT (Extract, Load, Transform)
 - Data Warehouse
 - Testes automatizados
 - Containerização
 - Tratamento de erros e auditoria


# 🏗️ Arquitetura ################################################################################
                +----------------+
                | Apache Airflow |
                +--------+-------+
                         |
                         v
                +----------------+
                | create_table   |
                +--------+-------+
                         |
                         v
                +----------------+
                | load_sales     |
                +--------+-------+
                         |
           +-------------+-------------+
           |                           |
           v                           v
+--------------------+     +----------------------+
| PostgreSQL         |     | Deadletter Queue     |
| raw_sales          |     | deadletter.json      |
+--------------------+     +----------------------+
           |
           v
+--------------------+
| dbt run            |
+--------------------+
           |
           v
+--------------------+
| stg_sales          |
+--------------------+
           |
           v
+--------------------+
| sales_summary      |
+--------------------+


# 🛠️ Tecnologias Utilizadas ################################################################################

Tecnologia	            Finalidade
Python 3.11	            Desenvolvimento
Apache Airflow 2.8	Orquestração
dbt Core	            Transformações
PostgreSQL 15	      Data Warehouse
Docker	            Containerização
Docker Compose	      Orquestração dos containers
Pytest	            Testes automatizados
Psycopg2	            Conexão PostgreSQL


# 📂 Estrutura do Projeto ################################################################################

PRJ_PIPE_PG_DBT_AIRFLOW/
      │
      ├── dags/
      │   └── sales_pipeline.py
      │
      ├── scripts/
      │   ├── create_tables.py
      │   ├── load_sales.py
      │   ├── validation.py
      │   ├── db_connection.py
      │   ├── logger_config.py
      │   └── make_deadletter_json.py
      │
      ├── dbt_project/
      │   ├── models/
      │   │   ├── staging/
      │   │   │   └── stg_sales.sql
      │   │   └── marts/
      │   │       └── sales_summary.sql
      │   ├── logs/
      │   │   └── dbt.log
      │   │
      │   ├── dbt_project.yml
      │   └── profiles.yml
      │
      ├── tests/
      │   ├── unit/
      │   │      ├── test_db_connection.py
      │   │      ├── test_deadletter.py
      │   │      ├── test_logger.py
      │   │      └── test_validation.py
      |   │
      │   ├── integration/
      │   │      ├── test_create_tables.py
      │   │      ├── test_insert_raw_sales.py
      │   │      ├── test_load_sales.py
      │   │      └── test_postgres_connection.py
      │   │
      │   ├── airflow/
      │   │      ├── test_dag_integrity.py
      │   │      ├── test_dag_loaded.py
      │   │      └── test_dag_tasks.py
      │   │
      │   ├── dbt/
      │   │     ├── test_dbt_mart.py
      │   │     ├── test_dbt_models.py
      │   │     └── test_dbt_staging.py
      │   │
      │   └── e2e/
      │         └── test_end_to_end_pipeline.py
      │
      ├── data/
      │   └── deadletter/
      │
      ├── logs/
      │   └── pipeline.log
      │
      ├── Dockerfile
      ├── docker-compose.yml
      ├── requirements.txt
      └── README.md


# 🔄 Fluxo do Pipeline ################################################################################

1. Criação da Tabela 

Task:

      create_table

      Cria a tabela:

            CREATE TABLE raw_sales (
            order_id INTEGER,
            customer_id INTEGER,
            amount NUMERIC,
            purchase_date TIMESTAMP
            );


2. Geração e Carga de Dados 

Task:

      load_sales

      Gera registros simulados contendo:

            ID do pedido
            ID do cliente
            Valor da compra
            Data da compra

            Exemplo:

                  {
                  "order_id": 1,
                  "customer_id": 100,
                  "amount": 250.50,
                  "purchase_date": "2026-05-30 12:00:00"
                  }


3. Validação de Dados 

As seguintes regras são aplicadas:

      Campos obrigatórios:
            order_id
            customer_id
            amount
            purchase_date

      Regras de negócio:
            amount > 0


4. Tratamento de Erros 

Registros inválidos são enviados para:

data/deadletter/deadletter.json

Exemplo:

      {
      "record": {
      "customer_id": 123,
      "amount": -50
      },
      "error": "Valor inválido"
      }


5. Transformação com dbt 

- 5.1 Camada Staging

      Modelo:

            stg_sales.sql

                  Responsável por:

                        Padronização
                        Conversões de tipo
                        Limpeza básica

                  Exemplo:

                  SELECT
                        order_id,
                        customer_id,
                        amount,
                        purchase_date::date AS purchase_day
                  FROM raw_sales


- 5.2 Camada Mart

      Modelo:

            sales_summary.sql

                  Responsável pela agregação analítica.

                  Exemplo:

                  SELECT
                        purchase_day,
                        COUNT(*)    AS total_orders,
                        SUM(amount) AS total_sales,
                        AVG(amount) AS average_ticket
                  FROM stg_sales
                  GROUP BY purchase_day



# 📊 Modelo Analítico ################################################################################

Tabela final:

      sales_summary

      Campo	                  Descrição
      purchase_day	      Data da venda
      total_orders	      Quantidade de pedidos
      total_sales	Valor       total vendido
      average_ticket	      Ticket médio


# 🧪 Testes ################################################################################

# Testes Unitários 

      Validam:

            Conexão com banco
            Logger
            Deadletter
            Regras de validação

      Execução:

            pytest tests/unit -v


# Testes de Integração

      Validam:

            PostgreSQL
            Criação de tabelas
            Inserção de dados
            Pipeline de carga

      Execução:

            pytest tests/integration -v
      

# Testes da DAG

      Validam:

            DAG carregada
            Tarefas existentes
            Dependências

      Execução:

            pytest tests/airflow -v
      

# Testes End-to-End

      Validam:

            Execução completa do pipeline

      Execução:

            pytest tests/e2e -v



# 🐳 Executando com Docker ################################################################################

      - Construir as imagens
            docker compose build --no-cache

      - Iniciar containers
            docker compose up -d

      - Verificar containers
            docker ps



# 🌐 Acessos ################################################################################

# Airflow
      http://localhost:8080

            Usuário: airflow
            Senha  : airflow

      --# Criar User no Airflow:

            '''bash     
                  cd ${PROJECT_HOME}/docker

                  docker exec -it docker-airflow-webserver-1 bash

                  airflow users create \
                  --username airflow \
                  --firstname F_name \
                  --lastname L_name \
                  --role Admin \
                  --email admin@email.com \
                  --password airflow

                  exit
		  
		

# pgAdmin
      http://localhost:5050
            DEFAULT_EMAIL	: admin@email.com
            DEFAULT_PASSWORD	: admin


# 🔍 Monitoramento ################################################################################

      - Visualizar logs do Airflow:
            docker compose logs -f airflow-scheduler

      - Visualizar logs da aplicação:
            cat logs/pipeline.log

      - Visualizar logs do dbt:
            cat dbt_project/logs/dbt.log



# 👨‍💻 Autor ################################################################################

Vitor Melo

Data Engineer | BI Engineer | Analytics Engineer

Tecnologias:
      PostgreSQL
      Airflow
      dbt
      Python
      SQL
      Docker
      Data Warehouse
      ETL / ELT
      Oracle Analytics Server (OAS)
      OBIEE
      ODI