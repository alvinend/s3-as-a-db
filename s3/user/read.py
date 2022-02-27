import boto3
import pandas
import settings

s3_client = boto3.client('s3')

def read(
    query,
    select='*'
):
    # Use S3 Select to Query CSV
    res = s3_client.select_object_content(
        Bucket = settings.BUCKET_NAME,
        Key = 'user.csv',
        ExpressionType = 'SQL',
        Expression =f"Select {select} from S3Object s " + query,
        InputSerialization = {
            'CompressionType': 'NONE',
            'CSV' : {
                'FileHeaderInfo' : 'Use',
                'RecordDelimiter' : '\n',
                'FieldDelimiter' : ','
            }
        },
        OutputSerialization = {
            'CSV' : {
                'RecordDelimiter' : '\n',
                'FieldDelimiter' : ','
            }
        }
    )

    records = ''

    for event in res['Payload']:
        if 'Records' in event:
            records = event['Records']['Payload'].decode('utf-8')

    # Change String to Array 1, "Name1, Address1\n 2, Name2, Address2\n" -> ["1, Name1, Address1", "2, Name2, Address2", ""]
    records = records.split('\n')

    # Remove Empty String Element ["1, Name1, Address1", "2, Name2, Address2", ""] -> ["1, Name1, Address1", "2, Name2, Address2"]
    records = filter(len, records)

    # Change Elemnt to be String [["1", "Name1", "Address1"], ["2", "Name2", "Address2"]]
    records = list(map(lambda x: x.replace('\r', '').split(','), records))

    return records

