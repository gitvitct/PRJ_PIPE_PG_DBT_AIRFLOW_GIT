import os
import psycopg2

from logger_config import logger


def get_connection():

    try:

        conn = psycopg2.connect(
            host=os.getenv('POSTGRES_HOST'),
            database=os.getenv('POSTGRES_DB'),
            user=os.getenv('POSTGRES_USER'),
            password=os.getenv('POSTGRES_PASSWORD')
        )

        logger.info('Conexão com PostgreSQL realizada com sucesso')

        return conn

    except Exception as e:

        logger.error(
            f'Erro ao conectar no PostgreSQL: {e}'
        )

        raise