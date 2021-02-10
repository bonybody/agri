from datetime import datetime
from api.database.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image = db.Column(db.String(255))
    name = db.Column(db.String(50), nullable=False)
    name_ruby = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date, unique=True)
    payment = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    # auth = db.relationship('auth')
    def __init__(self, image='', name='', name_ruby='', birthday='', payment=''):
        self.image = image
        self.name = name
        self.name_ruby = name_ruby
        self.birthday = birthday
        self.payment = payment

    def registerUser(self, user):
        record = User(
            image=user['image'],
            name=user['name'],
            name_ruby=user['name_ruby'],
            birthday=user['birthday']
        )
        db.session.add(record)
        db.session.commit()

        return user
