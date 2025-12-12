
import os

import os

class S3Sync:
    def sync_folder_to_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {folder} {aws_bucket_url} --region ap-south-2"
        print("Running command:", command)
        os.system(command)

    def sync_folder_from_s3(self, folder, aws_bucket_url):
        command = f"aws s3 sync {aws_bucket_url} {folder} --region ap-south-2"
        print("Running command:", command)
        os.system(command)

