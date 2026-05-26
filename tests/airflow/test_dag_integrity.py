# tests/airflow/test_dag_integrity.py

from airflow.models import DagBag


def test_dag_loaded():

    dagbag = DagBag()

    assert dagbag.import_errors == {}


def test_sales_pipeline_exists():

    dagbag = DagBag()

    dag = dagbag.get_dag("sales_pipeline")

    assert dag is not None


def test_tasks_exist():

    dagbag = DagBag()

    dag = dagbag.get_dag("sales_pipeline")

    expected_tasks = [
        "create_table",
        "load_sales",
        "run_dbt"
    ]

    for task in expected_tasks:
        assert task in dag.task_ids


def test_task_dependencies():

    dagbag = DagBag()

    dag = dagbag.get_dag("sales_pipeline")

    create_table = dag.get_task("create_table")

    assert create_table.downstream_task_ids == {"load_sales"}