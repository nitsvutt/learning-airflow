import pendulum
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.task_group import TaskGroup

hcm_tz = pendulum.timezone('Asia/Ho_Chi_Minh')

def _print_arg(arg):
    print(arg)

default_args = {
    'owner': 'vutt',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1, tzinfo=hcm_tz)
}

with DAG(
    'task_group',
    default_args=default_args,
    schedule_interval=None
) as dag:
    
    task_01 = PythonOperator(
        task_id='task_01',
        python_callable=_print_arg,
        op_kwargs={'arg': 'task_01'}
    )

    with TaskGroup(
        "group_01",
        tooltip="Tasks for group_01"
    ) as group_01:
        
        group_01_task_01 = PythonOperator(
            task_id='group_01_task_01',
            python_callable=_print_arg,
            op_kwargs={'arg': 'group_01_task_01'}
        )

        group_01_task_02 = PythonOperator(
            task_id='group_01_task_02',
            python_callable=_print_arg,
            op_kwargs={'arg': 'group_01_task_01'}
        )

        group_01_task_03 = PythonOperator(
            task_id='group_01_task_03',
            python_callable=_print_arg,
            op_kwargs={'arg': 'group_01_task_01'}
        )
    
    [group_01_task_01, group_01_task_02] >> group_01_task_03

task_01 >> group_01