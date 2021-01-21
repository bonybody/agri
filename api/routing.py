from api.controllers import index, user
def register_controller_blueprint(app):
    app.register_blueprint(index.bp)
    app.register_blueprint(user.bp)
