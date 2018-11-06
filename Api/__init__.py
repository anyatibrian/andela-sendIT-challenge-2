from flask import Flask
from config import config


def create_app(config_name):
    """the create app method that creates an app instance"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    # registering the blue print object
    from Api.Api_v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    return app
