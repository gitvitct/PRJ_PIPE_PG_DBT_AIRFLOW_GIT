from datetime import datetime


# Regras de Validação
#     order_id      obrigatório
#     customer_id   obrigatório
#     amount        > 0
#     timestamp     válido


def validate_sale(record):

    required_fields = [
        'order_id',
        'customer_id',
        'amount',
        'purchase_date'
    ]

    for field in required_fields:

        #if field not in record or record[field] in [None, ""]:
        if field not in record:
            return False, f'Campo ausente: {field}'

    if record['amount'] <= 0:
        return False, 'Amount inválido'

    try:
        datetime.strptime(
            str(record['purchase_date']),
            '%Y-%m-%d %H:%M:%S'
        )

    except:
        return False, 'Data inválida'

    return True, None