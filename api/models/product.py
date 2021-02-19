from datetime import datetime
from api.database.database import db


class Product(db.Model):
    __tablename__ = 't_product'
    p_code = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_name = db.Column(db.String(20), nullable=False)
    p_contents = db.Column(db.String(255))
    p_period = db.Column(db.Integer(2), nullable=False)
    p_quantity = db.Column(db.Integer(5), nullable=False)
    p_category = db.Column(db.String(255))
    p_tag = db.Column(db.String(255))
    p_area = db.Column(db.String(255))
    p_price = db.Column(db.Integer(10), nullable=False)
    p_exhibit = db.Column(db.DateTime, nullable=False, default=datetime.now)
    p_image = db.Column(db.String(255))
    p_state = db.Column(db.String(10))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, p_code, p_name='', p_contents='', p_period='', p_quantity='', p_category='', p_tag='', p_area='', p_price='', p_exhibit='', p_image='', p_state=''):
        self.p_name = p_name
        self.p_contents = p_contents
        self.p_period = p_period
        self.p_quantity = p_quantity
        self.p_category = p_category
        self.p_tag = p_tag
        self.p_area = p_area
        self.p_price = p_price
        self.p_exhibit = p_exhibit
        self.p_image = p_image
        self.p_state = p_state

    @classmethod
    def getUserInfo(cls, user_id):
        record = cls.query.filter_by(id=user_id).first()
        return {
            'id': record.id,
            'image': record.image,
            'display_name': record.display_name
        }

