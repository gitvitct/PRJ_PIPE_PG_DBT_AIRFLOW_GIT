import sys
import os
from unittest.mock import patch

sys.path.append("/opt/airflow")
from scripts.db_connection import get_connection

# Substitui temporariamente o psycopg2.connect por um Mock
@patch("scripts.db_connection.psycopg2.connect")

def test_get_connection(mock_connect):

    get_connection()

    # Verifica se o connect foi chamado uma única vez
    # e com os parâmetros corretos
    mock_connect.assert_called_once_with(
        host=os.getenv("POSTGRES_HOST"),
        database=os.getenv("DW_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    
    #mock_connect.assert_called_once()