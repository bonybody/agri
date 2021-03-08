import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import KoeFavorite
from .user_schema import UserSchema
from .koe_schema import KoeSchema

class KoeFavoriteSchema(ma.SQLAlchemyAutoSchema):
    Koe = ma.Nested(KoeSchema)
    user = ma.Nested(UserSchema)

    class Meta:
        model = KoeFavorite
