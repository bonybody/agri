from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import  current_app
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow(current_app)


def init_db():
    db.init_app(current_app)
    Migrate(current_app, db)


