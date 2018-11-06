from flask import Blueprint

# creating the blueprint for our app
api_v1 = Blueprint('api_v1', __name__)
from . import create_parcel_order_endpoints
