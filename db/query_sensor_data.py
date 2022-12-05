import sqlite3

def query_sensor_data(from_, to, sensor_id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY

    data = []

    data_json = []

    for id in sensor_id:
        query = "SELECT SENSOR_DATA.TIME, SENSOR_DATA.HUMIDITY, SENSOR_DATA.TEMPERATURE, SENSOR_DATA.DISTANCE, SENSOR_DATA.PRESSURE, SENSOR_DATA.LIGHT_LEVEL, COMPANY.ID, LOCATION.ID, SENSOR.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE SENSOR.SENSOR_API_KEY = SENSOR_DATA.SENSOR_API_KEY AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND SENSOR.ID = " + str(id) + " AND SENSOR_DATA.TIME <= " + str(to) + " AND SENSOR_DATA.TIME >= " + str(from_)

        result = cursor.execute(query)
        for row in result:
            data.append(row)
        
        json = {
            id: data
        }

        data_json.append(json)
    return data_json
