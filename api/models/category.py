from datetime import datetime
from api.database.database import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    auth = db.relationship('Product', backref='category')

    def __init__(self, name=''):
        self.name = name

    def setAttr(self, name=''):
        self.name = name

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return {
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    @classmethod
    def getCategory(cls, category_id):
        record = cls.query.filter_by(id=category_id).first()
        return record
