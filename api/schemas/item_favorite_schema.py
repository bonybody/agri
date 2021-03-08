import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import ItemFavorite
from .user_schema import UserSchema
from .item_schema import ItemSchema

class ItemFavoriteSchema(ma.SQLAlchemyAutoSchema):
    item = ma.Nested(ItemSchema)
    user = ma.Nested(UserSchema)

    class Meta:
        model = ItemFavorite
