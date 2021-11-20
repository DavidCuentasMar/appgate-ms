import os
from flask_app import create_app
import json

def test_log_failed(client):
    response = client.post('/log', data=dict())
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': 'file is required'}
    assert json_response == json_response_to_check

def test_log_success(client):
    testing_file = open('tests/test_logs.txt', 'rb')
    response = client.post('/log', data=dict(file=testing_file))
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'message': 'server is up!'}
    assert json_response == json_response_to_check

def test_is_user_know(client):
    response = client.get('/metrics/isuserknown?username=test_user_id')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': True}
    assert json_response == json_response_to_check

def test_is_client_know(client):
    response = client.get('/metrics/isclientknown?client=test_client_id')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': True}
    assert json_response == json_response_to_check

def test_is_ip_internal(client):
    response = client.get('/metrics/isipinternal?ip=1.2.3.4')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': False}
    assert json_response == json_response_to_check

def test_is_ip_internal2(client):
    response = client.get('/metrics/isipinternal')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': 'ip is required'}
    assert json_response == json_response_to_check

def test_is_ip_internal3(client):
    response = client.get('/metrics/isipinternal?ip=0.0.0.0')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': True}
    assert json_response == json_response_to_check     

def test_is_ip_know(client):
    response = client.get('/metrics/isipknown?ip=1.2.3.4')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': True}
    assert json_response == json_response_to_check    

def test_failing_attemps(client):
    response = client.get('/metrics/failedlogincountlastweek')
    json_response_to_check = json.loads(response.data.decode('utf-8'))
    json_response = {'result': 0}
    assert json_response == json_response_to_check    
    

        