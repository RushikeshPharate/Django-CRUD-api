

import requests
import json

URL='http://127.0.0.1:8000/student/'

def get_data(id=None):
    data = {}
    if id is not None:
        data = {
            'id':id
        }
    
    json_data=json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    json_data=r.json()
    print(json_data)

def create_student():
    data = {
        'name':'Ram',
        'city':'Varanasi',
        'mob':8641
    }
    json_data=json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    msg = r.json()
    print(msg)

def update_student():
    data={
        'id':2,
        'name':'Amir',
        'city':'Hyderabad'
    }
    json_data=json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    msg=r.json()
    print(msg)

def delete_student():
    data={
        'id':2
        }
    json_data=json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    msg=r.json()
    print(msg)

# get_data(4)
# create_student()
# update_student()
delete_student()
