from datetime import datetime
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import db, ma
from sqlalchemy import desc, and_, func
from flask import current_app

class ItemTransaction(db.Model):
    __tablename__ = 'item_transaction'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', onupdate='CASCADE', ondelete='CASCADE'))  # 出品者id
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))  # 出品者id
    buyer_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))  # 購入者id
    set_count = db.Column(db.Integer, nullable=False)  # 販売数
    state = db.Column(db.Integer, nullable=False, default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    seller = db.relationship(
        'User',
        primaryjoin="ItemTransaction.seller_id==User.id")
    buyer = db.relationship(
        'User',
        primaryjoin="ItemTransaction.buyer_id==User.id")

    def __init__(self, item_id='', seller_id='', buyer_id='', set_count='', state=0):
        self.item_id = item_id
        self.seller_id = seller_id
        self.buyer_id = buyer_id
        self.set_count = set_count
        self.state = state

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        db.session.refresh(self)

    @classmethod
    def getRecordById(cls, transaction_id):
        record = cls.query.filter_by(id=transaction_id).first()
        return record

    @classmethod
    def getRecordsByItemId(cls, item_id):
        records = cls.query.filter_by(item_id=item_id).all()
        return records

    @classmethod
    def getRecordsBySellerIdStateSold(cls, seller_id):
        records = cls.query.filter_by(seller_id=seller_id, state=2).all()
        return records

    @classmethod
    def getRecordsBySellerId(cls, seller_id):
        records = cls.query.filter_by(seller_id=seller_id).all()
        return records

    @classmethod
    def getRecordsByBuyerId(cls, buyer_id):
        records = cls.query.filter_by(buyer_id=buyer_id).all()
        return records

    @classmethod
    def getSalesDetailBySellerId(cls, seller_id, item_model):
        record = db.session.query(func.sum(item_model.price * cls.set_count)).\
            select_from(cls).\
            filter_by(seller_id=seller_id).\
            outerjoin(item_model, item_model.id == cls.item_id).\
            group_by(cls.buyer_id).\
            first()
        return record

