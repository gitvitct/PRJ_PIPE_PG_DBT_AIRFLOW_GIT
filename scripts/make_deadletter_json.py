from pathlib import Path
import json


def save_deadletter(
    deadletter,
    directory="data/deadletter",
    filename="deadletter.json"
):

    path = Path(directory)

    path.mkdir(parents=True, exist_ok=True)

    file_path = path / filename

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(deadletter, file, indent=4)

    print(f"Arquivo salvo em: {file_path}")