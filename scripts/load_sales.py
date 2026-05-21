import psycopg2
import random

from datetime import datetime

from validation import validate_sale
from logger_config import logger
from db_connection import get_connection
from make_deadletter_json import save_deadletter

deadletter = []

logger.info('Iniciando carga de vendas')

# Conexão dinâmica POSTGRE
conn = get_connection()

cursor = conn.cursor()  #-- O cursor executa comandos SQL.

for i in range(1, 101):

    sale = {
        "order_id": i,
        "customer_id": random.randint(1, 20),
        "amount": round(random.uniform(-50, 500), 2),
        "purchase_date": datetime.now().strftime(
            '%Y-%m-%d %H:%M:%S'
        )
    }

    is_valid, error = validate_sale(sale)

    if not is_valid:

        logger.error(
            f'Registro inválido: {sale} - {error}'
        )

        deadletter.append({
            'record': sale,
            'error': error
        })

        continue

    cursor.execute("""
        INSERT INTO raw_sales
        VALUES (%s, %s, %s, %s)
    """, (
        sale['order_id'],
        sale['customer_id'],
        sale['amount'],
        sale['purchase_date']
    ))

logger.info('Carga finalizada')

conn.commit()

cursor.close()
conn.close()

print(f'Registros inválidos: {len(deadletter)}')



#######################################################################################################################
## Criar Deadletter JSON

save_deadletter(deadletter)