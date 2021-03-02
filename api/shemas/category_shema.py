from api.database.database import ma
from api.models import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
