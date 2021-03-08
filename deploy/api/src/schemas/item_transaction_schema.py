import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import ItemTransaction
from .user_schema import UserSchema
from .item_schema import ItemSchema

class ItemTransactionSchema(ma.SQLAlchemyAutoSchema):
    item = ma.Nested(ItemSchema)
    seller = ma.Nested(UserSchema)
    buyer = ma.Nested(UserSchema)

    class Meta:
        model = ItemTransaction
