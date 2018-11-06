from flask import request, jsonify
from ..Api_v1 import api_v1


@api_v1.route('/parcels', methods=['POST'])
def post_parcels():
    return jsonify({'message': 'parcel order page'})