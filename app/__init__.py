import os
import time
from datetime import datetime as dt
from util.bookmark import save_job_run_details, get_job_details, get_next_file_name
from ghactivity_ingest import upload_file_to_s3
from ghactivity_transform import transform_to_parquet


def ghactivity_ingest_to_s3():
    bucket_name = os.environ.get('BUCKET_NAME')
    folder = os.environ.get('FOLDER')
    job_details = get_job_details('ghactivity_ingest')
    job_start_time = int(time.mktime(dt.now().timetuple()))
    print(f'Job Details: {job_details}')
    next_file = get_next_file_name(job_details)
    print(f'File to be ingested: {next_file}')
    job_run_details = upload_file_to_s3(next_file, bucket_name, folder)
    print(f'Job Run Details: {job_run_details}')
    save_job_run_details(job_details, job_run_details, job_start_time)
    return job_run_details


def lambda_handler(event, context):
    job_run_details = ghactivity_ingest_to_s3()
    return {
        'statusCode': 200,
        'body': 'File Ingested Successfully',
        'jobRunDetails': job_run_details
    }

def ghactivity_transform_to_parquet(file_name):
    bucket_name = os.environ.get('BUCKET_NAME')
    tgt_folder = os.environ.get('TARGET_FOLDER')
    job_start_time = int(time.mktime(dt.now().timetuple()))
    job_details = get_job_details('ghactivity_transform')
    print(f'Job Details: {job_details}')
    job_run_details = transform_to_parquet(file_name, bucket_name, tgt_folder)
    print(f'Job Run Details: {job_run_details}')
    save_job_run_details(job_details, job_run_details, job_start_time)
    return job_run_details


def lambda_transformer(event, context):
    file_name = event['jobRunDetails']['last_run_file_name']
    job_run_details = ghactivity_transform_to_parquet(file_name)
    return {
        'statusCode': 200,
        'body': 'File Ingested Successfully',
        'jobRunDetails': job_run_details
    }