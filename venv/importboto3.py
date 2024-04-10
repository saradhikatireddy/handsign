import boto3
import numpy as np
from PIL import Image
from io import BytesIO

# Create an S3 client
s3 = boto3.client('s3')

# Get a list of all the PNG files in the bucket
bucket_name = 'saradhi-bucket-4'
prefix = 'Data/'
response = s3.list_objects(Bucket=bucket_name, Prefix=prefix)
png_files = [obj['Key'] for obj in response['Contents'] if obj['Key'].endswith('.png')]

# Load the PNG files into a list of NumPy arrays
images = []
for file in png_files:
    obj = s3.get_object(Bucket=bucket_name, Key=file)
    image = np.array(Image.open(BytesIO(obj['Body'].read())))
    images.append(image)

