import sqlite3

def insert_data(sensor_api_key, time, humidity, temperature, distance, pressure, light_level):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "INSERT INTO SENSOR_DATA (SENSOR_API_KEY, TIME, HUMIDITY, TEMPERATURE, DISTANCE, PRESSURE, LIGHT_LEVEL) VALUES ('"+ sensor_api_key +"', " + str(time) + ", "+ str(humidity) + ", " + str(temperature) + ", " + str(distance) + ", " + str(pressure) + ", "+ str(light_level) + ");"

    cursor.execute(query)

    db.commit()

    return "data created"