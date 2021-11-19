import os
from flask import Flask, jsonify, json, request
import utils
import pandas as pd

app = Flask(__name__)
file_stop_flag = True
    
#Basic Testing Route
@app.route('/')
def ping():
    return jsonify({'message': 'server is up!'}), 200

@app.route('/log', methods=['POST'])
def log():
    file_stop_flag = True
    file = request.files['file']
    utils.handle_logs(file)
    file_stop_flag = False
    return jsonify({'message': 'server is up!'}), 200    

@app.route('/metrics', methods=['GET'])
def metrics():
    dt = pd.read_csv('logs.csv')

    is_user_known_data = request.args.get('IsUserKnown')
    is_client_known_data = request.args.get('isclientknown')
    is_ip_known_data = request.args.get('isipknown')
    is_ip_internal_data = request.args.get('isipinternal')
    is_ip_internal_flag = False 
    
    data_to_response = {'result': False}

    current_dt = None

    if is_user_known_data:
        current_dt = utils.is_user_known(dt, is_user_known_data)        
    if is_client_known_data:
        current_dt = utils.is_client_known(current_dt, is_client_known_data)
    if is_ip_known_data:
        current_dt = utils.is_ip_known(current_dt, is_ip_known_data)

    
    if len(current_dt)>0:
        data_to_response['result']=True
    
    return jsonify(data_to_response), 200

@app.route('/metrics/isuserknown', methods=['GET'])
def user_known():
    dt = pd.read_csv('logs.csv')

    data_to_check = request.args.get('username')
    
    data_to_response = {'result': False}

    if not data_to_check:
        data_to_response['result'] = 'username is required'
        return jsonify(data_to_response), 400

    if len(utils.is_user_known(dt, data_to_check)) > 0:
        data_to_response['result'] = True
    
    return jsonify(data_to_response), 200

@app.route('/metrics/isclientknown', methods=['GET'])
def client_known():
    dt = pd.read_csv('logs.csv')

    data_to_check = request.args.get('client')
    
    data_to_response = {'result': False}

    if not data_to_check:
        data_to_response['result'] = 'ip is required'
        return jsonify(data_to_response), 400  

    if len(utils.is_client_known(dt, data_to_check)) > 0:
        data_to_response['result'] = True
    
    return jsonify(data_to_response), 200  

@app.route('/metrics/isipknown', methods=['GET'])
def ip_known():
    dt = pd.read_csv('logs.csv')

    data_to_check = request.args.get('ip')
    
    data_to_response = {'result': False}

    if not data_to_check:
        data_to_response['result'] = 'ip is required'
        return jsonify(data_to_response), 400  

    if len(utils.is_ip_known(dt, data_to_check)) > 0:
        data_to_response['result'] = True
    
    return jsonify(data_to_response), 200      

@app.route('/metrics/isipinternal', methods=['GET'])
def ip_internal():
    dt = pd.read_csv('logs.csv')

    data_to_check = request.args.get('ip')
    
    data_to_response = {'result': False}

    if not data_to_check:
        data_to_response['result'] = 'ip is required'
        return jsonify(data_to_response), 400  

    if utils.is_ip_internal(data_to_check):
        data_to_response['result'] = True
    
    return jsonify(data_to_response), 200 

@app.route('/metrics/failedlogincountlastweek', methods=['GET'])
def failed_logging_attemps():
    dt = pd.read_csv('logs.csv')
    data_to_response = {'result': False}
    if len(utils.failed_login_count_last_week(dt)) > 0:
        data_to_response['result'] = len(utils.failed_login_count_last_week(dt))
    
    return jsonify(data_to_response), 200  


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True
    )
