from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'end_date': datetime(2024, 1, 7),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'trigger_dag_run_dag2',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    triggered_by_dag1 = TriggerDagRunOperator(
        task_id='triggered_by_dag1',
        trigger_dag_id='trigger_dag_run_dag1'
    )
    
    echo_dag2 = BashOperator(
        task_id='echo_dag2',
        bash_command="echo dag2"
    )

triggered_by_dag1 >> echo_dag2