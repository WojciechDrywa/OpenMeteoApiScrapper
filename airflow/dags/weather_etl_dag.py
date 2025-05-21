from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__) + "/.."))

from weather_data_loader.weather_data_loader import run_etl_pipline

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'storage')))

default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='weather_etl_dag',
    default_args=default_args,
    description='ETL DAG for weather data',
    start_date=datetime(2025, 5, 16),
    schedule_interval='@daily',
    catchup=False,
    tags=['weather', 'etl'],
) as dag:
    
    run_etl = PythonOperator(
        task_id='run_weather-etl',
        python_callable=run_etl_pipline
    )
    
    run_etl
