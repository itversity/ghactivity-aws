from datetime import datetime as dt
from datetime import timedelta as td
import time

import boto3


def get_job_details(job_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('jobs')
    job_details = table.get_item(Key={'job_id': job_name})['Item']
    return job_details


def get_job_start_time():
    return int(time.mktime(dt.now().timetuple()))


def get_next_file_name(job_details):
    job_start_time = get_job_start_time()
    job_run_bookmark_details = job_details.get('job_run_bookmark_details')
    baseline_days = int(job_details['baseline_days'])
    if job_run_bookmark_details:
        dt_part = job_run_bookmark_details['last_run_file_name'].split('.')[0].split('/')[-1]
        next_file_name = f"{dt.strftime(dt.strptime(dt_part, '%Y-%m-%d-%H') + td(hours=1), '%Y-%m-%d-%-H')}.json.gz"
    else:
        next_file_name = f'{dt.strftime(dt.now().date() - td(days=baseline_days), "%Y-%m-%d")}-0.json.gz'
    return job_start_time, next_file_name


def save_job_run_details(job_details, job_run_details, job_start_time):
    dynamodb = boto3.resource('dynamodb')
    job_run_details_item = {
        'job_id': job_details['job_id'],
        'job_run_time': job_start_time,
        'job_run_bookmark_details': job_run_details,
        'create_ts': int(time.mktime(dt.now().timetuple()))
    }
    job_run_details_table = dynamodb.Table('job_run_details')
    job_run_details_table.put_item(Item=job_run_details_item)
    
    job_details_table = dynamodb.Table('jobs')
    job_details['job_run_bookmark_details'] = job_run_details
    job_details_table.put_item(Item=job_details)