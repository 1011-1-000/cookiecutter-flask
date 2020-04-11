import commands
import logging.config
import os

from flask import Blueprint, Flask
from flask_restplus import Api

from config import BASE_DIR
from exts import cors, db, migrate

from app.user.controller.auth_controller import api as auth_ns
from app.user.controller.check_controller import api as check_ns
from app.user.controller.user_controller import api as user_ns


blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='FLASK　RestPlus API Server', version='0.1',
          description='a boilerplate for flask restplus web service')


def create_app(config_object="config"):
    register_logger()
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprint(app)
    register_namespace(app)
    register_commands(app)

    return app


def register_blueprint(app):
    app.register_blueprint(blueprint)


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)


def register_namespace(app):
    api.add_namespace(auth_ns, path='/api/auth')
    api.add_namespace(user_ns, path='/api/user')
    api.add_namespace(check_ns, path='/api/user')


def register_commands(app):
    """Register Click commands."""
    app.cli.add_command(commands.test)


def register_logger():
    import yaml
    with open(os.path.join(BASE_DIR, 'logger_config.yaml'), 'r') as f:
        dict_conf = yaml.load(f, Loader=yaml.FullLoader)
    logging.config.dictConfig(dict_conf)
