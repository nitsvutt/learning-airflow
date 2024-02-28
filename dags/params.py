from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from airflow.models.param import Param

def _print_sum(**context):
    x = context['params']['x']
    y = context['params']['y']
    print(x + y)

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'params',
    default_args=default_args,
    schedule_interval=None,
    catchup=True,
    params={
        'x': Param(0, type='integer'),
        'y': Param(0, type='integer')
    }
) as dag:
    
    print_sum = PythonOperator(
        task_id='print_sum',
        python_callable=_print_sum
    )

print_sum