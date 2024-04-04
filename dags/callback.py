import pendulum
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

hcm_tz = pendulum.timezone('Asia/Ho_Chi_Minh')

def _error_print(**context):
    print(context['dss'])

def _executed_alert(context):
    print(f"executed at {(context['dag_run'].queued_at).astimezone(hcm_tz).strftime('%Y-%m-%d %H:%M:%S')}")

def _succeeded_alert(context):
    print(f"succeeded at {(context['dag_run'].queued_at).astimezone(hcm_tz).strftime('%Y-%m-%d %H:%M:%S')}")

def _failed_alert(context):
    print(f"failed at {(context['dag_run'].queued_at).astimezone(hcm_tz).strftime('%Y-%m-%d %H:%M:%S')}")

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1, tzinfo=hcm_tz)
}

with DAG(
    'callback',
    default_args=default_args,
    schedule_interval=None
) as dag:
    
    error_print = PythonOperator(
        task_id='error_print',
        python_callable=_error_print,
        on_execute_callback=_executed_alert,
        on_success_callback=_succeeded_alert,
        on_failure_callback=_failed_alert
    )

error_print