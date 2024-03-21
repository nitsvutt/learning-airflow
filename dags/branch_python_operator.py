from airflow import DAG
from airflow.operators.python_operator import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta

def _check_is_actvive(is_active):
    if is_active:
        return "do_task"
    else:
        return "skip_task"

def _do_task():
    print('done task')

def _skip_task():
    print('skipped task')

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1)
}

with DAG(
    'branch_python_operator',
    default_args=default_args,
    schedule_interval=None
) as dag:

    check_is_actvive = BranchPythonOperator(
        task_id='check_is_actvive',
        python_callable=_check_is_actvive,
        op_kwargs={'is_active': 1}
    )

    do_task = PythonOperator(
        task_id='do_task',
        python_callable=_do_task
    )

    skip_task = PythonOperator(
        task_id='skip_task',
        python_callable=_skip_task
    )

check_is_actvive >> [do_task, skip_task]