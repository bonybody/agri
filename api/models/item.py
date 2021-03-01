from datetime import datetime
from api.database.database import db, ma
from .item_image import ItemImageSchema


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
    state = db.Column(db.Integer)  # 商品の状態
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    images = db.relationship('ItemImage', backref='item', lazy="joined")

    def __init__(self, name=None, description=None, period=None, remaining_days=None, remaining_format_id=None,
                 category_id=None,
                 shipment=None, price=None, state=None, user_id=None):
        self.name = name
        self.description = description
        self.period = period
        self.remaining_days = remaining_days
        self.remaining_format_id = remaining_format_id
        self.category_id = category_id
        self.shipment = shipment
        self.price = price
        self.state = state
        self.user_id = user_id

    def postRecord(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def getProductById(cls, item_id):
        record = cls.query.filter_by(id=item_id).first()
        return record


class ItemSchema(ma.SQLAlchemyAutoSchema):
    images = ma.Nested(ItemImageSchema, many=True)

    class Meta:
        model = Item
        # load_instance = True
