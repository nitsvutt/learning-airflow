from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models.dagrun import DagRun

def _print_dag_run(**kwargs):
    dr: DagRun = kwargs['dag_run']
    print(dr.queued_at)

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'dag_run',
    default_args=default_args,
    schedule_interval='@once',
    catchup=True
) as dag:
    
    print_dag_run = PythonOperator(
        task_id='print_dag_run',
        python_callable=_print_dag_run
    )

print_dag_run