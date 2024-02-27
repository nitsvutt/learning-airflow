from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def _print_execution_date(**kwargs):
    execution_date = kwargs['execution_date']
    print(execution_date)

def _print_external_argument(**kwargs):
    external_argument = kwargs['name']
    print(external_argument)

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'python_operator',
    default_args=default_args,
    schedule_interval='0 3 * * *',
    catchup=True
) as dag:

    print_execution_date = PythonOperator(
        task_id='print_execution_date',
        python_callable=_print_execution_date
    )

    print_external_argument = PythonOperator (
        task_id='print_external_argument',
        python_callable=_print_external_argument,
        op_kwargs={'name': 'vutt'}
    )

print_execution_date >> print_external_argument