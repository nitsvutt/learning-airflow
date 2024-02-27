from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'bash_operator',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    echo_execution_date = BashOperator(
        task_id='echo_execution_date',
        bash_command="echo {{execution_date.day}}"
    )
    
    echo_environment = BashOperator(
        task_id='echo_environment',
        bash_command='echo $NAME',
        env={'NAME': 'vutt'}
    )

echo_execution_date >> echo_environment