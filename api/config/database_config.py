import os

SQLALCHEMY_DATABASE_URI = 'postgresql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.environ['POSTGRES_USER'],
    'password': os.environ['POSTGRES_PASSWORD'],
    'host': os.environ['DB_HOST'],
    'db_name': os.environ['POSTGRES_DATABASE']
})
