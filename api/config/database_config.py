import os

SQLALCHEMY_DATABASE_URI = 'mysql://{user}:{password}@{host}/{db_name}?charset=utf8'.format(**{
    'user': os.environ['MYSQL_USER'],
    'password': os.environ['MYSQL_PASSWORD'],
    'host': os.environ['DB_HOST'],
    'db_name': os.environ['MYSQL_DATABASE']
})
