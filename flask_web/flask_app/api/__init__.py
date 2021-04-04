from flask_app.api.user import user_blue


def init_blueprint(app):
    app.register_blueprint(blueprint=user_blue)
