# tests/integration/test_dag_tasks.py
# DagBag É como um "catálogo" de DAGs.

from airflow.models import DagBag


def test_dag_tasks():

    dagbag = DagBag()

    dag = dagbag.get_dag("sales_pipeline")

    assert dag is not None

    task_ids = dag.task_ids

    assert "create_table" in task_ids
    assert "load_sales" in task_ids
    assert "run_dbt" in task_ids