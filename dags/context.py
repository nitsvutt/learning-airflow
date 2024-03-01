from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def _print_ds(**context):
    print(context['ds'])

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'context',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    print_ds = PythonOperator(
        task_id='print_ds',
        python_callable=_print_ds
    )

print_ds