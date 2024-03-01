from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models.taskinstance import TaskInstance

def _print_task_instance(**kwargs):
    ti: TaskInstance = kwargs['task_instance']
    print(ti.execution_date)

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'task_instance',
    default_args=default_args,
    schedule_interval='@once',
    catchup=True
) as dag:
    
    print_task_instance = PythonOperator(
        task_id='print_task_instance',
        python_callable=_print_task_instance
    )

print_task_instance