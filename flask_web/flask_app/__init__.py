from flask import Flask

from flask_session import Session

from flask_app import settings
from flask_app.api import init_blueprint
from flask_app.ext import init_ext

flasksession = Session()


def create_app(env_name):
    app = Flask(__name__)
    app.config.update(RESTFUL_JSON=dict(ensure_ascii=False))
    init_blueprint(app)
    app.config.from_object(settings.config.get(env_name))
    init_ext(app)
    flasksession.init_app(app)
    return app
