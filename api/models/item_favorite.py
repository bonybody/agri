from datetime import datetime
import sys
import os
from flask import current_app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma


class ItemFavorite(db.Model):
    __tablename__ = 'item_favorite'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', onupdate='CASCADE', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)


    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)
        return self

    @classmethod
    def getRecordByUserAndItemId(cls, item_id, user_id):
        record = cls.query.filter_by(user_id=user_id, item_id=item_id).first()
        current_app.logger.debug(record)
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