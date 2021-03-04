from api.database.database import ma
from api.models import ItemTransaction
from .user_shema import UserSchema
from .item_shema import ItemSchema

class ItemTransactionSchema(ma.SQLAlchemyAutoSchema):
    item = ma.Nested(ItemSchema)
    seller = ma.Nested(UserSchema)
    buyer = ma.Nested(UserSchema)

    class Meta:
        model = ItemTransaction
