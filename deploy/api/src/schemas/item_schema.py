import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from marshmallow import Schema, post_dump
from models import Item
from .item_image_schema import ItemImageSchema
from .category_schema import CategorySchema
from .remaining_format_schema import RemainingFormatSchema
from .user_schema import UserSchema


class ItemSchema(ma.SQLAlchemyAutoSchema):
    images = ma.Nested(ItemImageSchema, many=True)
    category = ma.Nested(CategorySchema)
    user = ma.Nested(UserSchema)
    remaining_format = ma.Nested(RemainingFormatSchema)
    item_favorites = ma.Nested(RemainingFormatSchema)

    class Meta:
        model = Item


class ItemWithSetCountSchema(Schema):
    set_count = ma.Integer()
    item = ma.Nested(ItemSchema)

    @post_dump
    def unnest(self, data, many):
        for key, val in data.items():
            if key != 'Item':
                data['Item']['key'] = val
            return data['Item']

