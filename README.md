# Learning Airflow

![license](https://img.shields.io/github/license/nitsvutt/learning-airflow)
![stars](https://img.shields.io/github/stars/nitsvutt/learning-airflow)
![forks](https://img.shields.io/github/forks/nitsvutt/learning-airflow)

## Table of Contents
1. [What is Apache Airflow](#introduction)
2. [Apache Airflow architecture](#architecture)
3. [How does Apache Airflow work](#work)
4. [Set up Apache Airflow](#set-up)
5. [Cheat sheet](#cheat-sheet)


<div id="introduction"/>

## 1. What is Apache Airflow

Apache Airflow is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web interface helps manage the state of your workflows. Airflow is deployable in many ways, varying from a single process on your laptop to a distributed setup to support even the biggest workflows. ([Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/index.html))

<div id="architecture"/>

## 2. Apache Airflow architecture

<p align="center">
    <img src="https://github.com/nitsvutt/learning-airflow/blob/main/images/architecture.png" title="Apache Airflow architecture" alt="apache airflow architecture" width=600/>
</p>

This is the simplest deployment of Apache Airflow:
- **Webserver:** The UI of Apache Airflow, which is used to manage user's Directed Acyclic Graphs (DAGs), configurations, and other features of Apache Airflow.
- **Scheduler:** The most important part of Apache Airflow scheduling and orchestrating DAGs and tasks, managing their runs and their dependencies.
- **Executor:** Components that actually execute tasks.
- **Metadata Database:** The database storing metadata about DAGs, their runs' states and other configurations like users, roles, connections,...

<div id="work"/>

## 3. How does Apache Airflow work

- First, users define python files that describes the arguments, the tasks and the dependencies of the DAG and locate in the DAG folder.
- After that, the **Scheduler** reads those files, submits the defined tasks to the executor to run and writes DAG's information to the **Metadata DB**.
- Now, users can view their DAG through the **Webserver** reading DAG's information from the **Metadata DB** to illustrate, trigger those start or stop and interact with other configurations.

<div id="set-up"/>

## 4. Set up Apache Airflow

### 4.1. Quick start with Docker

For testing purpose only, you can use the provided Docker image and Docker compose file of Apache Airflow at [here](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html) or quick start with:
- Dowload the Docker compose file:
```
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.3/docker-compose.yaml'
```
- Create necessary folders and .env file:
```
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
- Init database:
```
docker compose up airflow-init
```
- Start Apache Airflow:
```
docker compose up
```

### 4.2. Standalone installation:

For production, with medium workload, standalone installation within PostgreSQL is a good choice.
- First, you have to install a Postgresql Database:
    - Update and install necessary packages:
    ```
    sudo apt update
    sudo apt install wget
    ```
    - Add the PostgreSQL repository:
    ```
    sudo sh -c 'echo "deb https://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
    ```
    - Import the repository signing key:
    ```
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
    ```
    - Update the package lists:
    ```
    sudo apt update
    ```
    - Install postgresl-16:
    ```
    sudo apt install postgresql-16
    ```
    - Start PostgreSQL service:
    ```
    sudo systemctl start postgresql
    ```
    - Enable PostgreSQL service:
    ```
    sudo systemctl enable postgresql
    ```
    - Allow PostgreSQL port through the firewall:
    ```
    sudo ufw allow 5432/tcp
    ```
    - Connect with username=postgres and set password:
    ```
    sudo -u postgres psql
    ```
    ```
    ALTER USER postgres PASSWORD 'postgres';
    ```
    - Connect again with:
    ```
    psql -h localhost -U postgres -W
    ```
    - Create airflow user and airflow database:
    ```
    CREATE USER airflow PASSWORD 'airflow';
    CREATE DATABASE airflow OWNER airlfow;
    ```
- Now, you can set up Apache Airflow with PostgreSQL metadata database:
    - Install python3:
    ```
    sudo apt install python3 python3-pip -y
    ```
    - Update pip:
    ```
    pip3 install --upgrade pip
    ```
    - Install necessary packages:
    ```
    pip install SQLAlchemy psycopg2-binary apache-airflow
    ```
    - Create and add airflow home folder:
    ```
    sudo mkdir airflow
    ```
    - Add AIRFLOW_HOME to ~/.bashrc:
    ```
    export AIRFLOW_HOME=/home/vutt/airflow
    ```
    - Init database:
    ```
    airflow db init
    ```
    - Update AIRFLOW__DATABASE__SQL_ALCHEMY_CONN to postgresql connection:
    ```
    sql_alchemy_conn = postgresql+psycopg2://airflow:airflow@localhost:5432/airflow
    ```
    - Migrate database:
    ```
    airflow db migrate
    ```
    - Create airflow user:
    ```
    airflow users create --username root --password admin --firstname root --lastname root --role Admin --email root@admin.com
    ```
    - Start **Scheduler**:
    ```
    airflow scheduler
    ```
    - Start **Webserver**:
    ```
    airflow webserver --port 8999
    ```

<div id="cheat-sheet"/>

## 5. Cheat sheet:

- [PythonOperator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/python_operator.py)
- [BashOperator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/bash_operator.py)
- [BranchPythonOperator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/branch_python_operator.py)
- [Context](https://github.com/nitsvutt/learning-airflow/blob/main/dags/context.py)
- [Dag Run](https://github.com/nitsvutt/learning-airflow/blob/main/dags/dag_run.py)
- [Task Instance](https://github.com/nitsvutt/learning-airflow/blob/main/dags/task_instance.py)
- [Jinja Template](https://github.com/nitsvutt/learning-airflow/blob/main/dags/jinja_template.py)
- [Params](https://github.com/nitsvutt/learning-airflow/blob/main/dags/params.py)
- [Xcom](https://github.com/nitsvutt/learning-airflow/blob/main/dags/xcom.py)
- [Sensor](https://github.com/nitsvutt/learning-airflow/blob/main/dags/sensor.py)
- [Deferrable Operator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/deferrable_operator.py)
- [TriggerDagRunOperator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/trigger_dag_run_dag2.py)
- [Pool](https://github.com/nitsvutt/learning-airflow/blob/main/dags/pool.py)
- [Callback](https://github.com/nitsvutt/learning-airflow/blob/main/dags/callback.py)
- [Task Group](https://github.com/nitsvutt/learning-airflow/blob/main/dags/task_group.py)
- [Dynamic DAG Generator](https://github.com/nitsvutt/learning-airflow/blob/main/dags/dynamic_dag_generator_type_1.py)