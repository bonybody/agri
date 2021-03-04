from api.database.database import ma
from api.models import RemainingFormat

class RemainingFormatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RemainingFormat
