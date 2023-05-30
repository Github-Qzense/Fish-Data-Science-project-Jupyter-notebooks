import os
import boto3
from datetime import date
from tqdm import tqdm


# Set the environment variables
os.environ['AWS_ACCESS_KEY_ID'] = 'AKIA2QMGQOEAQFMTHGXR'
os.environ['AWS_SECRET_ACCESS_KEY'] = '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'



def download_s3_bucket(bucket_name, download_path):
    today = date.today()
    today = str(today)
    download_path = download_path+"\\"+today

    if "\\" in download_path: #path for windows
        download_path = download_path.replace("\\", "/")

    if not download_path.endswith("/"):
        download_path = download_path + "/"

    # Create the new folder if it doesn't exist
    os.makedirs(download_path, exist_ok=True)
    
    # Create a Boto3 client for S3
    s3 = boto3.client('s3')

    # List all objects in the bucket
    objects = s3.list_objects_v2(Bucket=bucket_name)['Contents']

    # Iterate over each object and download it
    for obj in tqdm(objects):
        key = obj['Key']
        file_name = os.path.join(download_path, key).replace(" /", "/")
        directory_path = os.path.dirname(file_name) 
        
        # Create the download directory if it doesn't exist
        os.makedirs(directory_path, exist_ok=True)
        
        # Download the object
        s3.download_file(bucket_name, key, file_name)
        print(f"Downloaded: {file_name}")
        
        
        
# Provide the bucket name and download path
bucket_name = 'fish-data-collection'
download_path = r"C:\Users\sowmy\Downloads\Fish Classification\Dataset\train_data\warehouse_data\Data\s3_data"

# Call the function to download the bucket objects
download_s3_bucket(bucket_name, download_path)