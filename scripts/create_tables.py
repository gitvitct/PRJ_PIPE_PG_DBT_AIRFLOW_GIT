import psycopg2
from db_connection import get_connection


# Conexão dinâmica POSTGRE
conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS raw_sales (
    order_id INT,
    customer_id INT,
    amount NUMERIC,
    purchase_date TIMESTAMP
)
""")

conn.commit()

cursor.close()
conn.close()

print("Tabela criada com sucesso.")