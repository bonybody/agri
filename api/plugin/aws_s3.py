import boto3

s3 = boto3.resource('s3')
item_image_bucket = s3.Bucket('agri-item-images')

def getS3Buckets(app):


    for bucket in s3.buckets.all():
        app.logger.debug(bucket)

