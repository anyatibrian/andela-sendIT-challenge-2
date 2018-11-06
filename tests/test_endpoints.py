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
    assert b'some fields are empty please' in response.data
