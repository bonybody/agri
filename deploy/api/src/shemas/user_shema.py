from api.database.database import ma
from api.models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User