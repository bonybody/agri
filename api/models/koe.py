from datetime import datetime
from api.database.database import db


class Koe(db.Model):
    __tablename__ = 'koe'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(25), nullable=False)
    text = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    item_id = db.Column(db.Integer, db.ForeignKey('item.id', onupdate='CASCADE', ondelete='CASCADE'))
    item = db.relationship('Item', primaryjoin='Koe.item_id==Item.id', backref='koes')

    def __init__(self, title='', text='', user_id='', item_id=''):
        self.title = title
        self.text = text
        self.user_id = user_id
        self.item_id = item_id

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return self

    @classmethod
    def getRecordById(cls, koe_id):
        record = cls.query.filter_by(id=koe_id).first()
        return record

    @classmethod
    def getRecordsByItem(cls, item_id):
        record = cls.query.filter_by(item_id=item_id).all()
        return record

    @classmethod
    def getRecordsByPostUser(cls, user_id):
        record = cls.query.filter_by(user_id=user_id).all()
        return record

    @classmethod
    def getRecordsByCatchUser(cls, user_id):
        record = cls.query.filter(cls.item.has(user_id=user_id)).all()
        return record

    @classmethod
    def getRecordsByNew(cls):
        record = cls.query.all()
        return record

    @classmethod
    def addTestData(cls):
        categories = []
        data_lists = ['grain', 'vegetable', 'fruit', 'other']
        for data in data_lists:
            categories.append(cls(data))

        db.session.add_all(categories)
        db.session.commit()
