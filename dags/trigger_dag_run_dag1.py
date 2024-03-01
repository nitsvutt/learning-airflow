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
    'trigger_dag_run_dag1',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    echo_dag1 = BashOperator(
        task_id='echo_dag1',
        bash_command="echo dag1"
    )

echo_dag1