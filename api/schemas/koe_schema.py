import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import Koe
from .user_schema import UserSchema
from .item_schema import ItemSchema

class KoeSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    item = ma.Nested(ItemSchema)

    class Meta:
        model = Koe
