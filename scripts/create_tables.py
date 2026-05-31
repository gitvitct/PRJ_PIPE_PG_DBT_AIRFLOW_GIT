
# scripts/create_tables.py

from scripts.db_connection import get_connection


def create_table():

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


if __name__ == "__main__":
    create_table()