from airflow import DAG
from airflow.sensors.python import PythonSensor
from datetime import datetime, timedelta

def _wait_event():
    return False

default_args = {
    'owner': 'vutt',
    'depends_on_past': True,
    'start_date': datetime(2024, 1, 1),
    'retries': 2,
    'retry_delay': timedelta(hours=1)
}

with DAG(
    'sensor',
    default_args=default_args,
    schedule_interval='@once',
    catchup=True
) as dag:
    
    wait_event = PythonSensor(
        task_id='wait_event',
        python_callable=_wait_event,
        mode = 'reschedule',
        poke_interval = 60
    )

wait_event

# https://docs.astronomer.io/learn/what-is-a-sensor
# https://airflow.apache.org/docs/apache-airflow/stable/_modules/airflow/example_dags/example_sensors.html