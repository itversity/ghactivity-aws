import uuid
import pandas as pd


def transform_to_parquet(file_name, bucket_name, tgt_folder):
    print(f'Creating JSON Reader for {file_name}')
    df_reader = pd.read_json(
        f's3://{bucket_name}/landing/ghactivity/{file_name}',
        lines=True,
        orient='records',
        chunksize=10000
    )
    year = file_name.split('-')[0]
    month = file_name.split('-')[1]
    dayofmonth = file_name.split('-')[2]
    hour = file_name.split('-')[3].split('.')[0]
    print(f'Transforming JSON to Parquet for {file_name}')
    for idx, df in enumerate(df_reader):
        target_file_name = f'part-{year}-{month}-{dayofmonth}-{hour}-{uuid.uuid1()}.snappy.parquet'
        print(f'Processing chunk {idx} of size {df.shape[0]} from {file_name}')
        df.drop(columns=['payload']). \
        to_parquet(
            f's3://{bucket_name}/{tgt_folder}/year={year}/month={month}/dayofmonth={dayofmonth}/{target_file_name}',
            index=False
        )

    return {
        'last_run_src_file_name': file_name,
        'last_run_tgt_file_pattern': f's3://{bucket_name}/{tgt_folder}/year={year}/month={month}/dayofmonth={dayofmonth}/part-{year}-{month}-{dayofmonth}-{hour}',
        'status_code': 200
    }