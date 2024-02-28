from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta
from typing import Any
import asyncio
from airflow.sensors.base import BaseSensorOperator
from airflow.triggers.temporal import TimeDeltaTrigger
from airflow.utils.context import Context

class WaitAMinuteTrigger(BaseSensorOperator):
    def execute(self, context: Context) -> None:
        trigger=TimeDeltaTrigger(timedelta(minutes=1))
        self.defer(trigger=trigger, method_name='execute_complete')
    def execute_complete(self, context: Context, event=None) -> None:
        return None

def _print_reach_event():
    print('reach event')

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'retries': 0
}

with DAG(
    'deferrable_operator',
    default_args=default_args,
    schedule_interval=None,
    catchup=True
) as dag:
    
    wait_event = WaitAMinuteTrigger(
        task_id='wait_event'
    )

    print_reach_event = PythonOperator(
        task_id='print_reach_event',
        python_callable=_print_reach_event
    )

wait_event >> print_reach_event