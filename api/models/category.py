from datetime import datetime
from api.database.database import db


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    item = db.relationship('Item', backref='category')

    def __init__(self, name=''):
        self.name = name

    def setAttr(self, name=''):
        self.name = name

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def getCategory(cls, category_id):
        record = cls.query.filter_by(id=category_id).first()
        return record

    @classmethod
    def addTestData(cls):
        categories = []
        data_lists = ['grain', 'vegetable', 'fruit', 'other']
        for data in data_lists:
            categories.append(cls(data))

        db.session.add_all(categories)
        db.session.commit()
