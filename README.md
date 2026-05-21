# 🚀 Sales Pipeline - Airflow + PostgreSQL + dbt + Docker

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

# 📌 Arquitetura

Fluxo da pipeline:

```text
Python → PostgreSQL → Airflow → dbt

PRJ_PIPE_PG_DBT/
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
│   ├── logs/dbt.log
│   ├── dbt_project.yml
│   └── profiles.yml
│
├── data/
│   └── deadletter/
│       └── deadletter.json
│
├── logs/
│   └── pipeline.log
│
│
├── Dockers/
│   ├── docker-compose.yml
│   └── Dockerfile
│
│
└── README.md


#################################################################################################
#################################################################################################
🧪 Validação de Dados

A pipeline possui regras simples de qualidade:

Valor da venda não pode ser negativo
Campos obrigatórios devem existir
Registros inválidos são enviados para:
data/deadletter/deadletter.json


#################################################################################################
#################################################################################################
📝 Logs

Os logs da pipeline são armazenados em:

logs/pipeline.log

Exemplo:

2026-05-20 10:00:00 - INFO - Iniciando carga de vendas



#################################################################################################
#################################################################################################

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

#################################################################################################
#################################################################################################