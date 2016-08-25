from flask import Flask
from flask.ext.mail import Mail
from config import config
from .main import main as main_blueprint

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    mail.init_app(app)

    app.register_blueprint(main_blueprint)

    return app
