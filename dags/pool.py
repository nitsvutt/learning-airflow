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
    'pool',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    task_1 = BashOperator(
        task_id="task_1",
        bash_command="echo task_1",
        pool_slots=1,
        pool="poor_performance",
    )

    task_2 = BashOperator(
        task_id="task_2",
        bash_command="echo task_2",
        pool_slots=1,
        pool="poor_performance",
    )

    task_3 = BashOperator(
        task_id="task_3",
        bash_command="echo task_3",
        pool_slots=1,
        pool="poor_performance",
    )

    task_4 = BashOperator(
        task_id="task_4",
        bash_command="echo task_4",
        pool_slots=1,
        pool="poor_performance",
    )

    task_5 = BashOperator(
        task_id="task_5",
        bash_command="echo task_5",
        pool_slots=1,
        pool="poor_performance",
    )

    task_6 = BashOperator(
        task_id="task_6",
        bash_command="echo task_6",
        pool_slots=1,
        pool="poor_performance",
    )

    task_7 = BashOperator(
        task_id="task_7",
        bash_command="echo task_7",
        pool_slots=1,
        pool="poor_performance",
    )

    task_8 = BashOperator(
        task_id="task_8",
        bash_command="echo task_8",
        pool_slots=1,
        pool="poor_performance",
    )

    task_9 = BashOperator(
        task_id="task_9",
        bash_command="echo task_9",
        pool_slots=1,
        pool="poor_performance",
    )

    task_10 = BashOperator(
        task_id="task_10",
        bash_command="echo task_10",
        pool_slots=1,
        pool="poor_performance",
    )

[task_1, task_4, task_6] >> task_2 >> task_3
task_5 >> task_3
task_8 >> task_7 >> task_3
task_9 >> task_10 >> task_3