from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma


class Address(db.Model):
    __tablename__ = 'address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postal_code = db.Column(db.Integer, nullable=False)
    prefecture = db.Column(db.String(50))
    municipalities = db.Column(db.String(255), nullable=False)
    other = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, postal_code='', prefecture='', city='', municipalities='', other=''):
        self.postal_code = postal_code
        self.prefecture = prefecture
        self.city = city
        self.municipalities = municipalities
        self.other = other

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return {
            'id': self.id,
            'postal_code': self.postal_code,
            'prefecture': self.prefecture,
            'city': self.city,
            'municipalities': self.municipalities,
            'other': self.other
        }
