import sqlite3

def location_get_one(company_api_key, id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "SELECT LOCATION.ID, LOCATION.COMPANY_ID, LOCATION.LOCATION_NAME, LOCATION.LOCATION_COUNTRY, LOCATION.LOCATION_CITY, LOCATION.LOCATION_META, COMPANY.ID FROM COMPANY, LOCATION WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND LOCATION.ID = " + id
    result = cursor.execute(query)

    return result

def sensor_get_one(company_api_key, id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "SELECT SENSOR.ID, SENSOR.LOCATION_ID, SENSOR.SENSOR_NAME, SENSOR.SENSOR_CATEGORY, SENSOR.SENSOR_META, COMPANY.ID, LOCATION.ID FROM COMPANY, LOCATION, SENSOR WHERE  LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND SENSOR.ID = " + str(id)
    # COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND
    
    result = cursor.execute(query)

    return result

def sensor_data_get_one(company_api_key, ):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "SELECT SENSOR_DATA.TIME, SENSOR_DATA.HUMIDITY, SENSOR_DATA.TEMPERATURE, SENSOR_DATA.DISTANCE, SENSOR_DATA.PRESSURE, SENSOR_DATA.LIGHT_LEVEL, COMPANY.ID, LOCATION.ID, SENSOR.ID FROM COMPANY, LOCATION, SENSOR, SENSOR_DATA WHERE SENSOR.SENSOR_API_KEY = SENSOR_DATA.SENSOR_API_KEY AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND SENSOR_DATA.ID = " + str(id)