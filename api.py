from flask import Flask, jsonify, request
from db import create_table, get_all, get_one, delete, modify, admin
import sqlite3
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)

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

    return jsonify("OK")


# LOCATION

@app.route('/location/get/all', methods=['GET'])
def location_get_all():
    req = request.get_json()

    company_api_key = req['company_api_key']

    result = get_all.location_get_all(company_api_key)

    data = []
    for row in result:
        data_json = {
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
def location_get_one(id):
    req = request.get_json()

    company_api_key = req['company_api_key']

    result = get_one.location_get_one(company_api_key, id)

    data = []
    for row in result:
        data_json = {
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
def location_modify():
    req = request.get_json()
    
    company_api_key = req['company_api_key']
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
def location_delete():
    req = request.get_json()

    company_api_key = req['company_api_key']
    id = req['location_id']

    result = delete.delete_location(company_api_key, id)
    
    response = {
        "result": result
    }
    return jsonify(response)

# SENSOR

@app.route('/sensor/get/all', methods=['GET'])
def sensor_get_all():
    req = request.get_json()

    company_api_key = req['company_api_key']

    result = get_all.sensor_get_all(company_api_key)

    data = []
    for row in result:
        data_json = {
            'ID': row[0],
            'LOCATION_ID': row[1],
            'SENSOR_NAME': row[2],
            'SENSOR_CATEGORY': row[3],
            'SENSOR_META': row[4]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor/get/<id>', methods=['GET'])
def sensorget_one(id):
    req = request.get_json()

    company_api_key = req['company_api_key']

    result = get_one.sensor_get_one(company_api_key, id)

    data = []
    for row in result:
        data_json = {
            'ID': row[0],
            'LOCATION_ID': row[1],
            'SENSOR_NAME': row[2],
            'SENSOR_CATEGORY': row[3],
            'SENSOR_META': row[4]
        }
        data.append(data_json)

    return jsonify(data)

@app.route('/sensor', methods=['PUT'])
def sensor_modify():
    req = request.get_json()

    company_api_key = req['company_api_key']
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
def sensor_delete():
    req = request.get_json()

    company_api_key = req['company_api_key']
    id = req['sensor_id']

    result = delete.delete_sensor(company_api_key, id)
    
    response = {
        "result": result
    }
    return jsonify(response)

# SENSOR DATA

# @app.route('/sensor_data/get/all', methods=['GET'])
# def sensor_data_get_all():
#     req = request.get_json()

#     company_api_key = req['company_api_key']

#     result = get_all.get_all(company_api_key)

#     data = []
#     for row in result:
#         data.append(row)

#     return jsonify(data)

# @app.route('/sensor_data/get/<id>', methods=['GET'])
# def sensor_data_get_one(id):
#     result = get_one.get_one('SENSOR_DATA', id)

#     data = []
#     for row in result:
#         data.append(row)

#     return jsonify(data)

# # FALTA MODIFY SENSOR DATA

# @app.route('/sensor_data/<id>', methods=['DELETE'])
# def sensor_data_delete(id):
#     result = delete.delete('SENSOR_DATA', id)

#     response = {
#         "result": result
#     }
#     return jsonify(response)


if __name__ == '__main__':
    create_table.create_tables()
    app.run(debug=True, port=5000)