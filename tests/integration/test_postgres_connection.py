# tests/integration/test_postgres_connection.py

def test_postgres_connection(db_connection):

    cursor = db_connection.cursor()

    cursor.execute("SELECT 1")

    result = cursor.fetchone()

    assert result[0] == 1