from flask_app import create_app
import json

def test_server(client):
    response = client.get('/')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'message': 'server is up!'}
    assert json_response == json_response_to_check
    