from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma


class KoeFavorite(db.Model):
    __tablename__ = 'koe_favorite'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    koe_id = db.Column(db.Integer, db.ForeignKey('koe.id', onupdate='CASCADE', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

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

# class CategorySchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         model = Category