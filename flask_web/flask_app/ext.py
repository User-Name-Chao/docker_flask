from flask_login import LoginManager
from flask_migrate import Migrate
from flask_cors import CORS

from flask_app.models import db

migrate = Migrate(db=db)

login_manager = LoginManager()


def init_ext(app):
    db.init_app(app)
    migrate.init_app(app)
    CORS(app, supports_credentials=True)
    login_manager.init_app(app)
