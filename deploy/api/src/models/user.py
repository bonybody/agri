from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import db, ma

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
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
    items = db.relationship('Item', backref='user')
    koes = db.relationship('Koe', backref='user')
    item_favorites = db.relationship('ItemFavorite', backref='user')
    koe_favorites = db.relationship('KoeFavorite', backref='user')

    def __init__(self, display_name='', image='', name='', name_ruby='', birthday='', payment=''):
        self.display_name = display_name
        self.image = image
        self.name = name
        self.name_ruby = name_ruby
        self.birthday = birthday
        self.payment = payment

    def setAttr(self, display_name='', image='', name='', name_ruby='', birthday='', payment=''):
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

    def getUserInfo(self, user_id):
        record = db.session.query(self).filter_by(id=user_id).first()
        return record




    @classmethod
    def getUserInfo(cls, user_id):
        record = db.session.query(cls).filter_by(id=user_id).first()
        return record

# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = User