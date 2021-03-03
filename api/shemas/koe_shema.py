from api.database.database import ma
from api.models import Koe
from .user_shema import UserSchema
from .item_shema import ItemSchema

class KoeSchema(ma.SQLAlchemyAutoSchema):
    user = ma.Nested(UserSchema)
    item = ma.Nested(ItemSchema)

    class Meta:
        model = Koe
