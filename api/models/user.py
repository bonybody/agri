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
        return {
            'id': self.id,
            'display_name': self.display_name,
            'image': self.image,
            'name': self.name,
            'name_ruby': self.name_ruby,
            'birthday': self.birthday,
            'payment': self.payment
        }

    @classmethod
    def getUserInfo(cls, user_id):
        record = cls.query.filter_by(id=user_id).first()
        return {
            'id': record.id,
            'image': record.image,
            'display_name': record.display_name
        }

