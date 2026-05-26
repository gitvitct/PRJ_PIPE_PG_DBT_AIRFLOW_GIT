# tests/integration/test_insert_raw_sales.py

from datetime import datetime


def test_insert_raw_sale(db_connection):

    cursor = db_connection.cursor()

    insert_sql = """
        INSERT INTO raw_sales (
            customer,
            product,
            quantity,
            amount,
            created_at
        )
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        "Vitor",
        "Mouse",
        2,
        150,
        datetime.now()
    )

    cursor.execute(insert_sql, values)

    db_connection.commit()

    cursor.execute("""
        SELECT customer, product
        FROM raw_sales
        WHERE customer = 'Vitor'
    """)

    result = cursor.fetchone()

    assert result[0] == "Vitor"
    assert result[1] == "Mouse"