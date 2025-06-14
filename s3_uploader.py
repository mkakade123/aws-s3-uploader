# s3_uploader.py
import boto3
import os
from botocore.exceptions import NoCredentialsError

def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3')
    try:
        s3.upload_file(local_file, bucket, s3_file)
        print(f"Upload Successful: {s3_file}")
    except FileNotFoundError:
        print("The file was not found")
    except NoCredentialsError:
        print("AWS credentials not available")


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Upload files to AWS S3 bucket')
    parser.add_argument('file_path', help='Local file path to upload')
    parser.add_argument('bucket_name', help='Target S3 bucket name')
    parser.add_argument('s3_key', help='S3 file key/name')
    args = parser.parse_args()
    upload_to_aws(args.file_path, args.bucket_name, args.s3_key)
