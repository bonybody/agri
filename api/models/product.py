from datetime import datetime
from api.database.database import db


class Product(db.Model):
    __tablename__ = 't_product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    contents = db.Column(db.String(255))
    period = db.Column(db.Integer(2), nullable=False)
    quantity = db.Column(db.Integer(5), nullable=False)
    category = db.Column(db.String(255))
    area = db.Column(db.String(255))
    price = db.Column(db.Integer(10), nullable=False)
    image = db.Column(db.String(255))
    state = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, id, name='', contents='', period='', quantity='', category='', area='', price='', image='', state='', created_at=''):
        self.name = name
        self.contents = contents
        self.period = period
        self.quantity = quantity
        self.category = category
        self.area = area
        self.price = price
        self.image = image
        self.state = state
        self.created_at = created_at

    @classmethod
    def getUserInfo(cls, user_id):
        record = cls.query.filter_by(id=user_id).first()
        return {
            'id': record.id,
            'image': record.image,
            'display_name': record.display_name
        }

