ITEM_IMAGE_BASE = 'https://agri-item-images.s3-ap-northeast-1.amazonaws.com/'

from datetime import timedelta
DEBUG = True
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ENCODING = "utf8mb4"
SECRET_KEY = "123456"
JSON_AS_ASCII = False
JWT_AUTH_HEADER_PREFIX = 'Bearer'
JWT_EXPIRATION_DELTA = timedelta(seconds=6000)

import os

SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'host': os.environ['DB_HOST'],
    'db_name': os.environ['MYSQL_DATABASE']
})
