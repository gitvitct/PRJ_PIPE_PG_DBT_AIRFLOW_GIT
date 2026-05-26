# tests/conftest.py

import os
import psycopg2
import pytest


@pytest.fixture
def db_connection():

    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        database=os.getenv("DW_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

    yield conn

    conn.close()