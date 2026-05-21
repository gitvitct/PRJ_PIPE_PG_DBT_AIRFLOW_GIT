from pathlib import Path
import json


def save_deadletter(deadletter, 
                    directory='/opt/airflow/data/deadletter', 
                    filename='deadletter.json'):
    """
    Salva o conteúdo da deadletter em um arquivo JSON.
    """

    path = Path(directory)
    path.mkdir(parents=True, exist_ok=True)

    with open(path / filename, 'w') as file:
        json.dump(deadletter, file, indent=4)

    print(f'Arquivo salvo em: {path / filename}')