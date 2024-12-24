import pandas as pd
import boto3
import os

def download_data_from_minio(bucket_name, object_name, file_path):
    minio_endpoint = os.getenv('MINIO_ENDPOINT')
    minio_access_key = os.getenv('MINIO_ACCESS_KEY')
    minio_secret_key = os.getenv('MINIO_SECRET_KEY')

    s3_client = boto3.client(
        's3',
        endpoint_url=minio_endpoint,
        aws_access_key_id=minio_access_key,
        aws_secret_access_key=minio_secret_key
    )

    s3_client.download_file(bucket_name, object_name, file_path)

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'])
    data = data.rename(columns={'Date': 'ds', 'Close': 'y'})
    data = data[['ds', 'y']]
    return data
