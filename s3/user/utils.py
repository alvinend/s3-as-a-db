import boto3
import pandas
import os
import settings
from io import StringIO

s3_resource = boto3.resource('s3')
s3_client = boto3.client('s3')

def get_df():
    res = s3_client.get_object(Bucket=settings.BUCKET_NAME, Key="user.csv")

    df = pandas.read_csv(res.get("Body"))

    return df

def save_to_s3(df):
    csv_buffer = StringIO()
    df.to_csv(csv_buffer, index=False)
    s3_resource.Object(settings.BUCKET_NAME, 'user.csv').put(Body=csv_buffer.getvalue())
