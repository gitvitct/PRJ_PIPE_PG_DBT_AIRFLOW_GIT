# tests/integration/test_dbt_staging.py
# Este teste assume que existe o modelo: models/staging/stg_sales.sql

import subprocess

def test_dbt_staging(db_connection):

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

    cursor.execute("""
        SELECT COUNT(*)
        FROM public.stg_sales
    """)

    count = cursor.fetchone()[0]

    assert count == 3

    cursor.close()