import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from database.database import ma
from models import Category

class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
