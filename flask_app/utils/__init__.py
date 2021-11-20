#client_id = [user,client]
import csv  
import json
import os
from werkzeug.utils import secure_filename
import pandas as pd
from datetime import datetime, timedelta



def create_file():
    data_list = []
    with open("./logs.txt") as f:
        file_content_lines = f.readlines()
        for line in file_content_lines:
            file_content_list = line.split(" ")
            datetime_str = f'{file_content_list[0]} {file_content_list[1]}'
            data = {
                "datetime": datetime.strptime(datetime_str,'%Y%m%d %H:%M:%S'),
                "servername": file_content_list[2],
                "user_id": file_content_list[3].split(":")[0][1:],
                "client_id": file_content_list[3].split(":")[1][:-1],
                "msg": " ".join(file_content_list[4:])
            }
            data_list.append(data)

    header = ['datetime','servername','user_id','client_id','msg']
    
    header_flag = True
    if os.path.isfile('./logs.csv'):
        header_flag = False
    
    with open('./logs.csv', 'a', encoding='UTF8') as f:
        writer = csv.writer(f)
        if header_flag:
            writer.writerow(header)
        for data in data_list:
            writer.writerow(
                [
                    data['datetime'],
                    data['servername'],
                    data['user_id'],
                    data['client_id'],
                    data['msg']
                ]
            )

def handle_logs(file):
    file.save(os.path.join("./logs.txt"))
    create_file()

def is_user_known(dt, data_to_check, single=True):
    data = dt.loc[dt['user_id'].str.contains(data_to_check)]    
    return data

def is_client_known(dt, data_to_check, single=True):
    data = dt.loc[dt['client_id'] == (data_to_check)]
    return data

def is_ip_known(dt, data_to_check, single=True):
    data = dt.loc[dt['msg'].str.contains(data_to_check)]
    return data

def is_ip_internal(data_to_check, single=True):
    f = open('internal_ip_list.json',)
    data = json.load(f)
    if data_to_check in data['ip_list']:
        return True
    return False

def failed_login_count_last_week(dt):
    date_from = datetime.today() - timedelta(days=7)
    date_to = datetime.today()
    data = dt.loc[ (dt['datetime'] > str(date_from)) & (dt['datetime'] < str(date_to)) & dt['msg'].str.contains('SUSPECT')]
    return data
