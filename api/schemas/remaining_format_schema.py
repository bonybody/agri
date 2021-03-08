import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.database import ma
from models import RemainingFormat

class RemainingFormatSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RemainingFormat
