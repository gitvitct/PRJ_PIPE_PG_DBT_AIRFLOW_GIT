# tests/unit/test_db_connection.py

from unittest.mock import patch
from scripts.db_connection import get_connection


@patch("scripts.db_connection.psycopg2.connect")
def test_get_connection(mock_connect):

    get_connection()

    mock_connect.assert_called_once() 