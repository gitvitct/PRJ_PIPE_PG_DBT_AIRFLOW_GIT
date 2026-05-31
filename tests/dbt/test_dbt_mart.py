# tests/integration/test_dbt_mart.py
# models/marts/sales_summary.sql

import subprocess


def test_dbt_mart(db_connection):

    cursor = db_connection.cursor()

    cursor.execute("""
        INSERT INTO raw_sales
        VALUES
        (1, 1, 100, NOW()),
        (2, 2, 200, NOW()),
        (3, 3, 300, NOW())
    """)

    db_connection.commit()


    subprocess.run(
        ["dbt", "run"],
        cwd="/opt/airflow/dbt_project",
        check=True
    )

    cursor = db_connection.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM public.sales_summary
    """)

    count = cursor.fetchone()[0]

    assert count > 0

    cursor.close()