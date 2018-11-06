from flask import Flask
from config import config


def create_app(config_name):
    """the create app method that creates an app instance"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    return app
