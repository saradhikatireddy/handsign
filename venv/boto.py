import boto3
import os

# Create an S3 client
s3_client = boto3.client('s3', region_name='us-east-2')

# Specify the bucket name
bucket_name = 'saradhi-bucket-4'

# Create the S3 bucket
s3_client.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'us-east-2'
    }
)

print(f'S3 bucket "{bucket_name}" created successfully.')

# Upload the data folder to the bucket
data_folder = 'handsign\Data.png'
for root, dirs, files in os.walk(data_folder):
    for file in files:
        file_path = os.path.join(root, file)
        s3_client.upload_file(file_path, bucket_name, file)
        print('Data folder uploaded successfully.')
