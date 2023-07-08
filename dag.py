from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from etl import etl_pipeline

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 5),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'hotel_booking_etl',
    default_args=default_args,
    description='An ETL pipeline for hotel booking data',
    schedule_interval='* * * * *',
)

with dag:
    etl_task = PythonOperator(
        task_id='etl',
        python_callable=etl_pipeline,
        op_kwargs={
            'csv_file': 'files/hotel_data_simple.csv',
            'json_file': 'files/hotels.json',
        },
    )

    print_task = PythonOperator(
        task_id='print',
        python_callable=lambda: print(open('hotels.json').read()),
    )

    etl_task >> print_task
