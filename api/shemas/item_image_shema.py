from api.database.database import ma
from api.models import ItemImage

class ItemImageSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = ItemImage
        # load_instance = True
