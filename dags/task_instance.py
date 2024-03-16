from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def _print_task_instance(**context):
    ti = context['ti']
    print(ti.execution_date)

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
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