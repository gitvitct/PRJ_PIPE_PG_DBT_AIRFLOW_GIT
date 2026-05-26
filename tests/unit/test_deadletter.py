# tests/unit/test_deadletter.py

import json
from scripts.make_deadletter_json import save_deadletter


def test_save_deadletter(tmp_path):

    invalid_data = {
        "customer": "",
        "amount": -100
    }

    output_dir = tmp_path

    save_deadletter(invalid_data, output_dir)

    files = list(output_dir.glob("*.json"))

    assert len(files) > 0

    with open(files[0]) as f:
        content = json.load(f)

    assert content["amount"] == -100