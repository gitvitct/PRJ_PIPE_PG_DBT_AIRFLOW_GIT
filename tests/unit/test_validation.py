# tests/unit/test_validation.py
# from datetime import date
from scripts.validation import validate_sale

### test_validate_sale_success ####################################################################

def test_validate_sale_success():

    sale = {
        "order_id": 1,
        "customer_id": "Vitor",
        "amount": 1000,
        "purchase_date": "2026-05-26 10:30:00"
    }

    result = validate_sale(sale)

    assert result == (True, None)


### test_validate_sale_negative_amount ####################################################################
def test_validate_sale_negative_amount():

    sale = {
        "order_id": 2,
        "customer_id": "Vitor",
        "amount": -1000,
        "purchase_date": "2026-05-26 10:30:00"
    }

    result = validate_sale(sale)

    assert result == (False, "Amount inválido")





### test_validate_sale_missing_customer ####################################################################
def test_validate_sale_missing_customer():

    sale = {
        "order_id": 1,
        "amount": 100,
        "purchase_date": "2026-05-26 10:00:00"
    }

    result = validate_sale(sale)

    assert result == (False, "Campo ausente: customer_id")



### test_validate_sale_invalid_date ####################################################################

def test_validate_sale_invalid_date():

    sale = {
        "order_id": 1,
        "customer_id": "Vitor",
        "amount": 100,
        "purchase_date": "26-05-2026"
    }

    result = validate_sale(sale)

    assert result == (False, "Data inválida")






"""


### test_validate_sale_empty_customer ####################################################################
def test_validate_sale_empty_customer():

    sale = {
        "order_id": 3,
        "customer_id": "",
        "amount": 1000,
        "purchase_date": "2026-05-26 10:30:00"
    }

    result = validate_sale(sale)

    assert result == (False, "Campo ausente: customer_id")


### test_validate_sale_missing_purchase_date ####################################################################

def test_validate_sale_missing_purchase_date():

    sale = {
        "order_id": 4,
        "customer_id": "Vitor",
        "amount": 1000,
        "purchase_date": ""
    }

    result = validate_sale(sale)

    assert result == (False, "Data inválida")


    """