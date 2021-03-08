from datetime import datetime, timedelta, date, time
import calendar
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from .item_transaction import ItemTransaction
from .item_favorite import ItemFavorite
from database.database import db
from sqlalchemy import desc, func, and_, or_
from flask import current_app

# week
today = datetime.combine(date.today(), time=time())
monday = datetime.combine(today, time=time()) + timedelta(days=-today.weekday())
current_app.logger.debug(monday)
sunday = monday + timedelta(days=6, hours=23, minutes=59, seconds=59)
current_app.logger.debug(sunday)

# month
month_first = today.replace(day=1)
month_last = today.replace(day=calendar.monthrange(today.year, today.month)[1])

# day
day_first = today
day_last = today + timedelta(hours=23, minutes=59, seconds=59)


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)  # 商品名
    description = db.Column(db.Text)  # 商品説明文
    period = db.Column(db.Integer, nullable=False)  # 販売日数
    remaining_days = db.Column(db.Integer, nullable=False)
    remaining_format_id = db.Column(db.Integer,
                                    db.ForeignKey('remaining_format.id', onupdate='CASCADE', ondelete='CASCADE'))
    category_id = db.Column(db.Integer,
                            db.ForeignKey('category.id', onupdate='CASCADE', ondelete='CASCADE'))  # 設定したカテゴリのID
    shipment = db.Column(db.Integer, nullable=False)  # 配送にかかる時間（日）
    price = db.Column(db.Integer, nullable=False)  # 商品の値段
    volume = db.Column(db.String(10), nullable=False)  # 商品の1セットあたりの量
    area = db.Column(db.String(50), nullable=False)
    state = db.Column(db.Integer, default=1)  # 商品の状態
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))

    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    images = db.relationship('ItemImage', backref='item', lazy="joined")
    item_transactions = db.relationship('ItemTransaction', backref='item')
    favorites = db.relationship('ItemFavorite', backref='item')

    # koes = db.relationship('Koe', backref='item')

    def __init__(self, name=None, description=None, period=None, remaining_days=None, remaining_format_id=None,
                 category_id=None,
                 shipment=None, price=None, volume='', area='', state=None, user_id=None):
        self.name = name
        self.description = description
        self.period = period
        self.remaining_days = remaining_days
        self.remaining_format_id = remaining_format_id
        self.category_id = category_id
        self.shipment = shipment
        self.price = price
        self.volume = volume
        self.area = area
        self.state = state
        self.user_id = user_id

    def postRecord(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getProductById(cls, item_id, user_id=0):
        record = db.session.query(
            cls, func.count(ItemFavorite.id), func.sum(ItemTransaction.set_count).label('remaining_set_count')
        ).select_from(cls).filter(cls.id == item_id).outerjoin(
            ItemTransaction,
            and_(ItemTransaction.item_id == cls.id,
                 or_(
                     and_(cls.remaining_format.has(name='week'),
                          ItemTransaction.created_at >= monday,
                          ItemTransaction.created_at <= sunday
                          ),
                     and_(cls.remaining_format.has(name='month'),
                          ItemTransaction.created_at >= month_first,
                          ItemTransaction.created_at <= month_last
                          ),
                     and_(cls.remaining_format.has(name='day'),
                          ItemTransaction.created_at >= day_first,
                          ItemTransaction.created_at <= day_last
                          )
                 )
                 )
        ).outerjoin(
            ItemFavorite,
            and_(ItemFavorite.item_id == cls.id, ItemFavorite.user_id == user_id)
        ).group_by(cls.id).first()
        return record

    @classmethod
    def getItemsBySearch(cls, user_id, args):
        current_app.logger.debug(args)
        order_by = False
        records = db.session.query(
            cls, func.count(ItemFavorite.id),
            func.sum(ItemTransaction.set_count).label(
                'remaining_set_count')).select_from(cls)
        for k, v in args.items():
            if (k == 'text'):
                records = records.filter(or_(cls.name.like('%' + v + '%'),
                                  cls.description.like('%' + v + '%')))
            if (k == 'category'):
                records = records.filter(cls.category_id == v)

            if (k == 'order_by'):
                order_by = v

                if (int(v) == 1):
                    current_app.logger.debug(order_by)
                    records = records.order_by(desc(cls.updated_at))

        records = records.outerjoin(
            ItemTransaction,
            and_(ItemTransaction.item_id == cls.id,
                 or_(
                     and_(cls.remaining_format.has(name='week'),
                          ItemTransaction.created_at >= monday,
                          ItemTransaction.created_at <= sunday
                          ),
                     and_(cls.remaining_format.has(name='month'),
                          ItemTransaction.created_at >= month_first,
                          ItemTransaction.created_at <= month_last
                          ),
                     and_(cls.remaining_format.has(name='day'),
                          ItemTransaction.created_at >= day_first,
                          ItemTransaction.created_at <= day_last
                          )
                 )
                 )
        ).outerjoin(
            ItemFavorite,
            and_(ItemFavorite.item_id == cls.id, ItemFavorite.user_id == user_id)
        ).group_by(cls.id).all()

        return records

    @classmethod
    def getItemsByFavorite(cls, user_id=0):
        records = db.session.query(
            cls, func.count(ItemFavorite.id),
            func.sum(ItemTransaction.set_count).label(
                'remaining_set_count')).select_from(cls).filter(cls.favorites.any(user_id=user_id)).outerjoin(
            ItemTransaction,
            and_(ItemTransaction.item_id == cls.id,
                 or_(
                     and_(cls.remaining_format.has(name='week'),
                          ItemTransaction.created_at >= monday,
                          ItemTransaction.created_at <= sunday
                          ),
                     and_(cls.remaining_format.has(name='month'),
                          ItemTransaction.created_at >= month_first,
                          ItemTransaction.created_at <= month_last
                          ),
                     and_(cls.remaining_format.has(name='day'),
                          ItemTransaction.created_at >= day_first,
                          ItemTransaction.created_at <= day_last
                          )
                 )
                 )
        ).outerjoin(
            ItemFavorite,
            and_(ItemFavorite.item_id == cls.id, ItemFavorite.user_id == user_id)
        ).group_by(cls.id).all()

        return records

    @classmethod
    def getItemsByNew(cls, user_id=0):
        records = db.session.query(
            cls, func.count(ItemFavorite.id),
            func.sum(ItemTransaction.set_count).label(
                'remaining_set_count')).select_from(cls).outerjoin(
            ItemTransaction,
            and_(ItemTransaction.item_id == cls.id,
                 or_(
                     and_(cls.remaining_format.has(name='week'),
                          ItemTransaction.created_at >= monday,
                          ItemTransaction.created_at <= sunday
                          ),
                     and_(cls.remaining_format.has(name='month'),
                          ItemTransaction.created_at >= month_first,
                          ItemTransaction.created_at <= month_last
                          ),
                     and_(cls.remaining_format.has(name='day'),
                          ItemTransaction.created_at >= day_first,
                          ItemTransaction.created_at <= day_last
                          )
                 )
                 )
        ).outerjoin(
            ItemFavorite,
            and_(ItemFavorite.item_id == cls.id, ItemFavorite.user_id == user_id)
        ).group_by(cls.id).all()

        return records

    @classmethod
    def getItemsByUserId(cls, user_id=0):
        records = db.session.query(
            cls, func.count(ItemFavorite.id),
            func.sum(ItemTransaction.set_count).label(
                'remaining_set_count')).select_from(cls).filter(cls.user_id == user_id).outerjoin(
            ItemTransaction,
            and_(ItemTransaction.item_id == cls.id,
                 or_(
                     and_(cls.remaining_format.has(name='week'),
                          ItemTransaction.created_at >= monday,
                          ItemTransaction.created_at <= sunday
                          ),
                     and_(cls.remaining_format.has(name='month'),
                          ItemTransaction.created_at >= month_first,
                          ItemTransaction.created_at <= month_last
                          ),
                     and_(cls.remaining_format.has(name='day'),
                          ItemTransaction.created_at >= day_first,
                          ItemTransaction.created_at <= day_last
                          )
                 )
                 )
        ).outerjoin(
            ItemFavorite,
            and_(ItemFavorite.item_id == cls.id, ItemFavorite.user_id == user_id)
        ).group_by(cls.id).all()

        return records
