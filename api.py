from flask import Flask, jsonify, request
from db import create_table, get_all, get_one, delete, modify, admin, sensor_data_insert, query_sensor_data
import sqlite3
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
import time

app = Flask(__name__)

auth_company_api_key = HTTPTokenAuth()

@auth_company_api_key.verify_token
def verify_company_api_key(company_api_key):
    if not (company_api_key):
        return False
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # USERNAME AND PASSWORD VALIDATION
    query = "SELECT * FROM COMPANY WHERE COMPANY_API_KEY = '" + company_api_key + "'"

    row = cursor.execute(query)

    row = cursor.fetchone()

    if row is not None:
        return True
    else:
        return False

# ADMIN FUNCTIONS

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    if not (username and password):
        return False
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # USERNAME AND PASSWORD VALIDATION
    query = "SELECT * FROM ADMIN WHERE USERNAME = '" + username +"' AND PASSWORD = '" + password + "'"

    row = cursor.execute(query)

    row = cursor.fetchone()

    query

    if row is not None:
        return True
    else:
        return False

@app.route('/create_company', methods=['POST'])
@auth.login_required
def create_company():
    req = request.get_json()

    response = {
        "response": admin.company_create(req['company_name'])
    }

    return jsonify(response)

@app.route('/create_location', methods=['POST'])
@auth.login_required
def create_location():
    req = request.get_json()

    company_id = req['company_id']
    location_name = req['location_name']
    location_country = req['location_country']
    location_city = req['location_city']
    location_meta = req['location_meta']

    response = {
        "response": admin.location_create(company_id, location_name, location_country, location_city, location_meta)
    }

    return jsonify(response)

@app.route('/create_sensor', methods=['POST'])
@auth.login_required
def create_sensor():
    req = request.get_json()

    location_id = req['location_id']
    sensor_name = req['sensor_name']
    sensor_category = req['sensor_category']
    sensor_meta = req['sensor_meta']

    response = {
        "response": admin.sensor_create(location_id, sensor_name, sensor_category, sensor_meta)
    }

    return jsonify(response)

@app.route('/see_tables', methods=['POST'])
@auth.login_required
def see_tables():
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # COMPANY
    query = "SELECT * FROM COMPANY"
    rows = cursor.execute(query)

    print("---------- COMPANY ----------")
    for row in rows:
        print(row)

    # LOCATION
    query = "SELECT * FROM LOCATION"
    rows = cursor.execute(query)

    print("---------- LOCATION ----------")
    for row in rows:
        print(row)
    
    # SENSOR
    query = "SELECT * FROM SENSOR"
    rows = cursor.execute(query)

    print("---------- SENSOR ----------")
    for row in rows:
        print(row)

    # SENSOR DATA
    query = "SELECT * FROM SENSOR_DATA"
    rows = cursor.execute(query)

    print("---------- SENSOR DATA ----------")
    for row in rows:
        print(row)

    print("-------------- END --------------")

    return jsonify("OK")

# LOCATION

@app.route('/location/get/all', methods=['GET'])
@auth_company_api_key.login_required
def location_get_all():
    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")

    result = get_all.location_get_all(company_api_key)

    data = []
    for row in result:
        data_json = {
            'COMPANY_ID': row[6],
            'ID': row[0],
            'COMPANY_ID': row[1],
            'LOCATION_NAME': row[2],
            'LOCATION_COUNTRY': row[3],
            'LOCATION_CITY': row[4],
            'LOCATION_META': row[5]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/location/get/<id>', methods=['GET'])
@auth_company_api_key.login_required
def location_get_one(id):
    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")


    result = get_one.location_get_one(company_api_key, id)

    data = []
    for row in result:
        data_json = {
            'COMPANY_ID': row[6],
            'ID': row[0],
            'COMPANY_ID': row[1],
            'LOCATION_NAME': row[2],
            'LOCATION_COUNTRY': row[3],
            'LOCATION_CITY': row[4],
            'LOCATION_META': row[5]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/location', methods=['PUT'])
@auth_company_api_key.login_required
def location_modify():
    req = request.get_json()

    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['location_id']
    name = req['location_name']
    country = req['location_country']
    city = req['location_city']
    meta = req['location_meta']
    
    result = modify.modify_location(company_api_key, id, name, country, city, meta)

    
    response = {
        "result": result
    }

    return jsonify(response)

@app.route('/location', methods=['DELETE'])
@auth_company_api_key.login_required
def location_delete():
    req = request.get_json()
    print(request.headers)
    company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['location_id']


    result = delete.delete_location(company_api_key, id)
    
    response = {
        "result": result
    }
    return jsonify(response)

# SENSOR

@app.route('/sensor/get/all', methods=['GET'])
@auth_company_api_key.login_required
def sensor_get_all():
    company_api_key = request.headers['Authorization'].replace("Bearer ", "")

    result = get_all.sensor_get_all(company_api_key)

    data = []
    for row in result:
        data_json = {
            'COMPANY_ID': row[5],
            'LOCATION_ID': row[6],
            'ID': row[0],
            'LOCATION_ID': row[1],
            'SENSOR_NAME': row[2],
            'SENSOR_CATEGORY': row[3],
            'SENSOR_META': row[4]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor/get/<id>', methods=['GET'])
@auth_company_api_key.login_required
def sensorget_one(id):
    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")

    result = get_one.sensor_get_one(company_api_key, id)

    data = []
    for row in result:
        data_json = {
            'COMPANY_ID': row[5],
            'LOCATION_ID': row[6],
            'ID': row[0],
            'LOCATION_ID': row[1],
            'SENSOR_NAME': row[2],
            'SENSOR_CATEGORY': row[3],
            'SENSOR_META': row[4]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor', methods=['PUT'])
@auth_company_api_key.login_required
def sensor_modify():
    req = request.get_json()

    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['sensor_id']
    name = req['sensor_name']
    category = req['sensor_category']
    meta = req['sensor_meta']
    
    result = modify.modify_sensor(company_api_key, id, name, category, meta)

    
    response = {
        "result": result
    }
    return jsonify(response)

@app.route('/sensor', methods=['DELETE'])
@auth_company_api_key.login_required
def sensor_delete():
    req = request.get_json()

    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['sensor_id']

    result = delete.delete_sensor(company_api_key, id)
    
    response = {
        "result": result
    }
    return jsonify(response)

# SENSOR DATA

@app.route('/sensor_data/get/all', methods=['GET'])
@auth_company_api_key.login_required
def sensor_data_get_all():
    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")

    result = get_all.sensor_data_get_all(company_api_key)

    data = []
    for row in result:
        data_json = {
            "COMPANY_ID": row[6],
            "LOCATION_ID": row[7],
            "SENSOR_ID": row[8],
            "TIME": row[0],
            "HUMIDITY": row[1],
            "TEMPERATURE": row[2],
            "DISTANCE": row[3],
            "PRESSURE": row[4],
            "LIGHT_LEVEL": row[5]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor_data/get/<id>', methods=['GET'])
@auth_company_api_key.login_required
def sensor_data_get_one(id):
    company_api_key = request.headers['Authorization'].replace("Bearer ", "")

    result = get_one.sensor_data_get_one(company_api_key, id)

    data = []
    for row in result:
        data_json = {
            "COMPANY_ID": row[6],
            "LOCATION_ID": row[7],
            "SENSOR_ID": row[8],
            "ID": row[9],
            "TIME": row[0],
            "HUMIDITY": row[1],
            "TEMPERATURE": row[2],
            "DISTANCE": row[3],
            "PRESSURE": row[4],
            "LIGHT_LEVEL": row[5]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor_data', methods=['PUT'])
@auth_company_api_key.login_required
def sensor_data_modify():
    req = request.get_json()

    company_api_key = company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['id']
    humidity = req['humidity']
    temperature = req['temperature']
    distance = req['distance']
    pressure = req['pressure']
    light_level = req['light_level']

    response = {
        "response": modify.modify_sensor_data(company_api_key, id, humidity, temperature, distance, pressure, light_level)
    }

    return jsonify(response)

@app.route('/sensor_data', methods=['DELETE'])
@auth_company_api_key.login_required
def sensor_data_delete():
    req = request.get_json()

    company_api_key = request.headers['Authorization'].replace("Bearer ", "")
    id = req['sensor_id']

    response = {
        "result": delete.delete_sensor_data(company_api_key, id)
    }
    return jsonify(response)

auth_sensor_data = HTTPTokenAuth(scheme='Bearer')

@auth_sensor_data.verify_token
def verify_token(sensor_api_key):
    if not (sensor_api_key):
        return False
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # USERNAME AND PASSWORD VALIDATION
    query = "SELECT * FROM SENSOR WHERE SENSOR_API_KEY = '" + sensor_api_key + "'"

    row = cursor.execute(query)

    row = cursor.fetchone()

    if row is not None:
        return True
    else:
        return False

@app.route('/api/v1/sensor_data', methods=['POST'])
@auth_sensor_data.login_required
def insertion_sensor_data():
    req = request.get_json()

    # ENVIAR COMO 'NULL' SI NO APLICA
    print(request.headers)
    sensor_api_key = request.headers['Authorization'].replace("Bearer ", "")
    time_epoch = time.time()
    humidity = req['humidity']
    temperature = req['temperature']
    distance = req['distance']
    pressure = req['pressure']
    light_level = req['light_level']

    response = {
        "response": sensor_data_insert.insert_data(sensor_api_key, time_epoch, humidity, temperature, distance, pressure, light_level)
    }

    return jsonify(response)

@app.route('/api/v1/sensor_data', methods=['GET'])
@auth_company_api_key.login_required
def query_sensor():
    req = request.get_json()
    
    from_ = req['from']
    to = req['to']
    sensor_id = req['sensor_id']

    response = query_sensor_data.query_sensor_data(from_, to, sensor_id)

    return jsonify(response)


if __name__ == '__main__':
    create_table.create_tables()
    app.run(port=5000)