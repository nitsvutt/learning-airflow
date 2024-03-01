from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'jinja_template',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    echo_ds_nodash = BashOperator(
        task_id='echo_ds',
        bash_command="echo {{ds_nodash}}"
    )

echo_ds_nodash