import sqlite3

def delete_location(company_api_key, id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()


    # QUERY
    query = "DELETE FROM LOCATION WHERE LOCATION.ID IN (SELECT LOCATION.ID FROM COMPANY, LOCATION WHERE LOCATION.ID = " + str(id) + " AND LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "')"
    # query = "DELETE FROM COMPANY, LOCATION WHERE LOCATION.ID = " + str(id) + " AND LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
    result = cursor.execute(query)

    # SAVE CHANGE
    db.commit()

    return True

def delete_sensor(company_api_key, id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()


    # QUERY
    query = "DELETE FROM SENSOR WHERE SENSOR.ID IN (SELECT SENSOR.ID FROM COMPANY, LOCATION, SENSOR WHERE  LOCATION.COMPANY_ID = COMPANY.ID AND SENSOR.LOCATION_ID = LOCATION.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "' AND SENSOR.ID = " + str(id) + ")"
    # query = "DELETE FROM COMPANY, LOCATION WHERE LOCATION.ID = " + str(id) + " AND LOCATION.COMPANY_ID = COMPANY.ID AND COMPANY.COMPANY_API_KEY = '" + company_api_key + "'"
    result = cursor.execute(query)

    # SAVE CHANGE
    db.commit()

    return True