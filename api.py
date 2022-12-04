from flask import Flask, jsonify, request
from db import create_table, get_all, get_one, delete, modify
import sqlite3

app = Flask(__name__)

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