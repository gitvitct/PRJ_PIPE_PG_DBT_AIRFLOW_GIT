# tests/integration/test_load_sales.py

from scripts.load_sales import load_sales


def test_load_sales(db_connection):

    load_sales()

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM public.raw_sales
    """)

    count = cursor.fetchone()[0]

    assert count > 0

    cursor.close()