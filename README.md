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

## 1. Apache Airflow architecture

<p align="center">
    <img src="https://github.com/nitsvutt/learning-airflow/blob/main/images/architecture.png" title="Apache Airflow architecture" alt="apache airflow architecture" width=600/>
</p>

This is the simplest deployment of Apache Airflow:
- **Webserver:** The UI of Apache Airflow, which is used to manage user's Directed Acyclic Graphs (DAGs), configurations, and other features of Apache Airflow.
- **Scheduler:** The most important part of Apache Airflow scheduling and orchestrating DAGs and tasks, managing their runs and their dependencies.
- **Executor:** Components that actually execute tasks.
- **Metadata Database:** The database storing metadata about DAGs, their runs' states and other configurations like users, roles, connections,...