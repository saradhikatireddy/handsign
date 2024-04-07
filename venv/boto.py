import boto3
import os

# Create an S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Specify the bucket name
bucket_name = 'saradhi-bucket-2'

# Create the S3 bucket
s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

print(f'S3 bucket "{bucket_name}" created successfully.')
