from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    items = db.relationship('Item', backref='category')

    def __init__(self, name='', category_id=1):
        self.name = name
        self.id = category_id
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
        data_lists = {1: '米・穀物', 2:'野菜', 3:'果物', 4:'その他'}
        for k,v in data_lists.items():
            categories.append(cls(name=v, category_id=k))

        db.session.add_all(categories)
        db.session.commit()

# class CategorySchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Category