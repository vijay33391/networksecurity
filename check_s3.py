import os
import sys
from NETWORKSECURITY.constants.training_pipeline import TRAINING_BUCKET_NAME
from NETWORKSECURITY.exception.exception import NetworkSecurityException

# Dummy timestamp and model folder for testing
timestamp = "test_run"
model_dir = r"E:\Network security\model"  # Change this to a real folder

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync \"{folder}\" \"{aws_bucket_url}\" --region ap-south-2"
        print("Running:", command)
        os.system(command)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync \"{aws_bucket_url}\" \"{folder}\" --region ap-south-2"
        print("Running:", command)
        os.system(command)


def sync_saved_model_dir_to_s3():
    try:
        s3_sync = S3Sync()
        aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/final_model/{timestamp}"
        s3_sync.sync_folder_to_s3(folder=model_dir, aws_bucket_url=aws_bucket_url)
    except Exception as e:
        raise NetworkSecurityException(e, sys)


if __name__ == "__main__":
    sync_saved_model_dir_to_s3()
