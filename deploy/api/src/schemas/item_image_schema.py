import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import ItemImage

class ItemImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemImage
        # load_instance = True
