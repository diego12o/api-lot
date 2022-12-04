import sqlite3

def modify_location(company_api_key, id, name, country, city, meta):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "UPDATE LOCATION SET LOCATION_NAME = '" + name + "', LOCATION_COUNTRY = '" + country + "', LOCATION_CITY = '" + city + "', LOCATION_META = '" + meta + "' FROM COMPANY WHERE LOCATION.ID = " + str(id) + " AND LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
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
    query = " UPDATE SENSOR SET SENSOR_NAME = '"+name+"', SENSOR_CATEGORY = '"+category+"', SENSOR_META = '"+meta+"' FROM COMPANY, LOCATION WHERE SENSOR.ID = " + str(id) + " AND LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
    result = cursor.execute(query)

    # SAVE CHANGE
    db.commit()

    return True

# FALTA SENSOR DATA