import boto3
import os

s3 = boto3.resource('s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'], aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'])
item_image_bucket = s3.Bucket('agri-item-images')

def getS3Buckets(app):


    for bucket in s3.buckets.all():
        app.logger.debug(bucket)

