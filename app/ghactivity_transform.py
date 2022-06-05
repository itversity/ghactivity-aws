import chunk
import uuid
from numpy import busday_count
import pandas as pd


def transform_to_parquet(file_name, bucket_name, tgt_folder):
    print(f'Transforming the {file_name} to parquet')
    df_reader = pd. \
        read_json(
            file_name,
            lines=True,
            orient='records',
            chunksize=10000
        )
    file_details = file_name.split('/')[-1].split('-')
    src_file_name = file_name.split('/')[-1].split('.')[0]
    year = file_details[0]
    month = file_details[1]
    dayofmonth = file_details[2]
    print(f'Uploading {file_name} to s3 using pattern s3://{bucket_name}/{tgt_folder}/year={year}/month={month}/dayofmonth={dayofmonth}/part-{src_file_name}')
    for df in df_reader:
        df.drop(columns=['payload'])
        tgt_file_name = f's3://{bucket_name}/{tgt_folder}/year={year}/month={month}/dayofmonth={dayofmonth}/part-{src_file_name}-{uuid.uuid1()}.snappy.parquet'
        df.to_parquet(tgt_file_name)

    return {
        'last_run_src_file_name': file_name,
        'last_run_tgt_file_pattern': f's3://{bucket_name}/{tgt_folder}/year={year}/month={month}/dayofmonth={dayofmonth}/part-{src_file_name}',
        'status_code': 200
    }
