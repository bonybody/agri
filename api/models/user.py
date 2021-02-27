from datetime import datetime
from api.database.database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    display_name = db.Column(db.String(15), nullable=False)
    image = db.Column(db.String(255))
    name = db.Column(db.String(50), nullable=False)
    name_ruby = db.Column(db.String(50), nullable=False)
    birthday = db.Column(db.Date)
    payment = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    auth = db.relationship('Auth', backref='user')
    item = db.relationship('Item', backref='user')

    def __init__(self, display_name, image='', name='', name_ruby='', birthday='', payment=''):
        self.display_name = display_name
        self.image = image
        self.name = name
        self.name_ruby = name_ruby
        self.birthday = birthday
        self.payment = payment

    def setAttr(self, display_name, image='', name='', name_ruby='', birthday='', payment=''):
        self.display_name = display_name
        self.image = image
        self.name = name
        self.name_ruby = name_ruby
        self.birthday = birthday
        self.payment = payment

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return self
    @classmethod
    def getUserInfo(cls, user_id):
        record = cls.query.filter_by(id=user_id).first()
        return record
