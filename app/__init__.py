from flask import Flask
from flask_mail import Mail, Message
from config import config
# from .main import main as main_blueprint

mail = Mail()


def create_app(config_name):
    app = Flask(__name__)
    # app.register_blueprint(main_blueprint)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    return app

main = create_app('default')