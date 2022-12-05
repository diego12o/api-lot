import sqlite3

def modify_location(company_api_key, id, name, country, city, meta):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "UPDATE LOCATION SET LOCATION_NAME = '" + name + "', LOCATION_COUNTRY = '" + country + "', LOCATION_CITY = '" + city + "', LOCATION_META = '" + meta + "' WHERE ID = " + str(id) + " AND COMPANY_ID = (SELECT ID FROM COMPANY WHERE COMPANY_API_KEY = '" + company_api_key + "')"

    result = cursor.execute(query)

    # SAVE CHANGE
    db.commit()

    return True

def modify_sensor(company_api_key, id, name, category, meta):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = " UPDATE SENSOR SET SENSOR_NAME = '"+name+"', SENSOR_CATEGORY = '"+category+"', SENSOR_META = '"+meta+"' WHERE ID = " + str(id) + " AND LOCATION_ID = (SELECT LOCATION.ID FROM LOCATION, COMPANY WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "')"

    result = cursor.execute(query)

    # SAVE CHANGE
    db.commit()

    return True

def modify_sensor_data(company_api_key, id, humidity, temperature, distance, pressure, light_level):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "UPDATE SENSOR_DATA SET HUMIDITY = " + str(humidity) + ", TEMPERATURE = " + str(temperature) + ", DISTANCE = " + str(distance) + ", PRESSURE = " + str(pressure) + ", LIGHT_LEVEL = "+ str(light_level) + " WHERE SENSOR_API_KEY = (SELECT SENSOR_DATA.SENSOR_API_KEY FROM SENSOR, LOCATION, COMPANY WHERE LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "') AND ID = " + str(id)

    cursor.execute(query)

    db.commit()

    return True