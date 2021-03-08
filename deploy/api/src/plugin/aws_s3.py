import boto3

s3 = boto3.resource('s3', aws_access_key_id='AKIAJZH4JAE5WA3CUOVQ', aws_secret_access_key='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')
item_image_bucket = s3.Bucket('agri-item-images')

def getS3Buckets(app):


    for bucket in s3.buckets.all():
        app.logger.debug(bucket)

