from datetime import datetime
from api.database.database import db


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False) # 商品名
    description = db.Column(db.Text) # 商品説明文
    period = db.Column(db.Integer, nullable=False) # 販売日数
    category_id = db.Column(db.Integer, db.ForeignKey('category.id', onupdate='CASCADE', ondelete='CASCADE')) # 設定したカテゴリのID
    area = db.Column(db.String(255)) # 商品の配送元
    quantity = db.Column(db.Integer, nullable=False) # 販売したい商品の数
    content = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Integer, nullable=False) # 商品の値段
    image = db.Column(db.String(255)) # 商品画像
    state = db.Column(db.Integer) # 商品の状態
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, name='', contents='', period='', quantity='', category='', area='', price='', image='', state='', created_at=''):
        self.name = name
        self.contents = contents
        self.period = period
        self.quantity = quantity
        self.category = category
        self.area = area
        self.price = price
        self.image = image
        self.state = state
        self.created_at = created_at

    @classmethod
    def getProductById(cls, item_id):
        record = cls.query.filter_by(id=item_id).first()
        return record

