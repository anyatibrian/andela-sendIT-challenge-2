from flask import Flask
from config import config
from flask_jwt_extended import JWTManager


def create_app(config_name):
    """the create app method that creates an app instance"""
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'no-form-against-me-shall-prosper'
    app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'
    # initializes jwt object
    jwt = JWTManager(app)
    app.config.from_object(config[config_name])
    # registering the blue print object
    from Api.Api_v1 import api_v1
    app.register_blueprint(api_v1, url_prefix='/api/v1')
    return app
