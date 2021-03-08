from .index import index_bp
from .item import item_bp
from .item_transaction import item_transaction_bp
from .test import test_bp
from .user import user_bp
from .koe import koe_bp
from .favorite import favorite_bp
from .search import search_bp
def register_controller_blueprint(app):
    app.register_blueprint(index_bp)
    app.register_blueprint(item_bp)
    app.register_blueprint(test_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(item_transaction_bp)
    app.register_blueprint(koe_bp)
    app.register_blueprint(favorite_bp)
    app.register_blueprint(search_bp)

__all__ = [
    register_controller_blueprint
]
