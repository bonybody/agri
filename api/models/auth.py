from datetime import datetime
from api.database.database import db
import hashlib


class Auth(db.Model):
    __tablename__ = 'auth'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', onupdate='CASCADE', ondelete='CASCADE'))
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.now, onupdate=datetime.now)

    def __init__(self, user_id='', email='', password=''):
        self.user_id = user_id
        self.email = email
        self.password = hashlib.sha256(password.encode('utf-8')).hexdigest()

    def setAttr(self, user_id='', email='', password=''):
        self.user_id = user_id
        self.email = email
        self.password = hashlib.sha256(password.encode('utf-8'))

    def postRecord(self):
        db.session.add(self)
        db.session.commit()
        return

    @classmethod
    def getRecordsAll(cls):
        records = cls.query.all()
        return records

    @classmethod
    def getRecordByEmail(cls, email):
        record = cls.query.filter_by(email=email).first()
        return record

    @classmethod
    def getRecordsByUserId(cls, user_id):
        record = cls.query.filter_by(user_id=user_id).first()
        return record
