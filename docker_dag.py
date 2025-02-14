from airflow.decorators import task, dag
from airflow.providers.docker.operators.docker import DockerOperator

from datetime import datetime

@dag(start_date=datetime(2021,1,1), schedule_interval='@daily',catchup=False)
def docker_dag():
 
    @task()
    def t1():
        pass
        
    t2 = DockerOperator(
        task_id='t2',
        image='python:3.8-slim-buster',
        command='echo "command running in the dcoker container"',
        # Or for a Python file
        #command='python3 my_script.py',
        docker_url='unix://var/run/docker.sock',
        network_mode='bridge'
        #Or can used host network_mode='host:'
    )
    
    t1() >> t2
    
dag = docker_dag()
