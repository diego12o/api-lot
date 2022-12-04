import sqlite3

def location_get_all(company_api_key):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "SELECT LOCATION.ID, LOCATION.COMPANY_ID, LOCATION.LOCATION_NAME, LOCATION.LOCATION_COUNTRY, LOCATION.LOCATION_CITY, LOCATION.LOCATION_META FROM COMPANY, LOCATION WHERE LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
    result = cursor.execute(query)

    return result

def sensor_get_all(company_api_key):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    print(company_api_key)
    query = "SELECT SENSOR.ID, SENSOR.LOCATION_ID, SENSOR.SENSOR_NAME, SENSOR.SENSOR_CATEGORY, SENSOR.SENSOR_META FROM COMPANY, LOCATION, SENSOR WHERE  LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
    # COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND
    
    result = cursor.execute(query)

    return result