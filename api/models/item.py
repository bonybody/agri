from datetime import datetime
from api.database.database import db
from sqlalchemy import desc


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
    state = db.Column(db.Integer)  # 商品の状態
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    images = db.relationship('ItemImage', backref='item', lazy="joined")
    item_transactions = db.relationship('ItemTransaction', backref='item')

    def __init__(self, name=None, description=None, period=None, remaining_days=None, remaining_format_id=None,
                 category_id=None,
                 shipment=None, price=None, volume='' ,area='', state=None, user_id=None):
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
    def getProductById(cls, item_id):
        record = cls.query.filter_by(id=item_id).first()
        return record

    @classmethod
    def getItemsByNew(cls):
        records = cls.query.order_by(desc(Item.updated_at)).all()
        return records

# from api.models import ItemImageSchema, CategorySchema, UserSchema, RemainingFormatSchema
# # from .item_image import ItemImageSchema, ItemImage
# # from .item_transaction import ItemTransaction
# # from .category import CategorySchema
# # from .remaining_format import RemainingFormatSchema
# # from .user import UserSchema
#
# class ItemSchema(ma.SQLAlchemyAutoSchema):
#     images = ma.Nested(ItemImageSchema, many=True)
#     category = ma.Nested(CategorySchema)
#     user = ma.Nested(UserSchema)
#     remaining_format = ma.Nested(RemainingFormatSchema)
#
#     class Meta:
#         model = Item
