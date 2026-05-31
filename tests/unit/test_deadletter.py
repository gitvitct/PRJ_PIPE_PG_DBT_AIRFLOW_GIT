# tests/unit/test_deadletter.py

import json
from scripts.make_deadletter_json import save_deadletter


###  tmp_path = /tmp/pytest-123/test_save_deadletter0///// cria uma pasta temporária exclusiva para o teste.
###  tmp_path é um fixture nativo do pytest.

def test_save_deadletter(tmp_path):

    invalid_data = {
        "customer": "",
        "amount": -100
    }

    output_dir = tmp_path
    #print(output_dir)
    #print("teste  teste")

    save_deadletter(invalid_data, output_dir)

    files = list(output_dir.glob("*.json"))

    assert len(files) > 0       ## Verifica se o arquivo foi criado

    with open(files[0]) as f:
        content = json.load(f)

    assert content["amount"] == -100