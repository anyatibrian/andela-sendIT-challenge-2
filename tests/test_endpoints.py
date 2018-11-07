import pytest
from Api import create_app
import json
from tests import test_data


@pytest.fixture(scope='module')
def client():
    app = create_app('Testing')
    # creating the test client
    test_client = app.test_client()
    # setting up the application client client upon which testing can be done
    cxt = app.app_context()
    cxt.push()
    yield test_client
    cxt.pop()


# checks whether the users has posted empty fields
def test_post_parcel_orders_empty_fields(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.empty_fields))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'some fields are empty'


# checks for bad input types in the field
def test_check_invalid_fields_in_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.bad_data))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'parcel_name, description, destination, pick_up should be strings'


# checks whether the post parcel field contains white spaces
def test_white_spaces_in_post_parcel_orders(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.empty_space))
    assert response.status_code == 400
    assert json.loads(response.data)['error'] == 'your fields contains white spaces'


# test post parcel order endpoint
def test_post_parcel_orders_endpoint(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.good_data))
    assert response.status_code == 201
    assert json.loads(response.data)['message'] == 'parcel delivery orders created successfully'


# test get all products endpoint
def test_get_all_products_products(client):
    response = client.post('api/v1/parcels', data=json.dumps(test_data.good_data))
    assert response.status_code == 201
    response = client.get('api/v1/parcels')
    assert response.status_code == 200
    assert json.loads(response.data)['parcel_orders'][0]['parcel_id'] == 1
