from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

def _xcom_push(**context):
    ti = context['ti']
    ti.xcom_push(key='name', value='vutt')

def _xcom_pull(**context):
    ti = context['ti']
    print(ti.xcom_pull(task_ids='xcom_push', key='name'))

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'xcom',
    default_args=default_args,
    schedule_interval='@once',
    catchup=True
) as dag:

    xcom_push = PythonOperator(
        task_id='xcom_push',
        python_callable=_xcom_push
    )

    xcom_pull = PythonOperator (
        task_id='xcom_pull',
        python_callable=_xcom_pull
    )

    xcom_bash_pull = BashOperator (
        task_id='xcom_bash_pull',
        bash_command="echo {{ti.xcom_pull(task_ids='xcom_push', key='name')}}"
    )

xcom_push >> xcom_pull >> xcom_bash_pull