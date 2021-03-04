from api.database.database import ma
from api.models import Item
from .item_image_shema import ItemImageSchema
from .category_shema import CategorySchema
from .remaining_format_shema import RemainingFormatSchema
from .user_shema import UserSchema

class ItemSchema(ma.SQLAlchemyAutoSchema):
    images = ma.Nested(ItemImageSchema, many=True)
    category = ma.Nested(CategorySchema)
    user = ma.Nested(UserSchema)
    remaining_format = ma.Nested(RemainingFormatSchema)

    class Meta:
        model = Item
