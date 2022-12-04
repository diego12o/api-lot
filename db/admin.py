import sqlite3
import secrets

def company_create(company_name):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # COMPANY CREATION
    company_api_key = secrets.token_hex(10)
    query = "INSERT INTO COMPANY(COMPANY_NAME, COMPANY_API_KEY) VALUES ('"+ company_name +"','"+ company_api_key +"');"

    cursor.execute(query)

    db.commit()

    return "company created"

def location_create(company_id, location_name, location_country, location_city, location_meta):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # COMPANY VERIFY
    query_validate_company = "SELECT * FROM COMPANY WHERE ID = "+ str(company_id)

    cursor.execute(query_validate_company)
    rows = cursor.fetchone()

    if rows is None:
        return "invalid company"

    # LOCATION CREATION
    query = "INSERT INTO LOCATION(COMPANY_ID, LOCATION_NAME, LOCATION_COUNTRY, LOCATION_CITY, LOCATION_META) VALUES (" + str(company_id) + ", '" + location_name + "', '" + location_country + "', '" + location_city + "', '" + location_meta + "');"

    cursor.execute(query)

    db.commit()

    return "location created"

def sensor_create(location_id, sensor_name, sensor_category, sensor_meta):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()


    # LOCATION VERIFY
    query_validate_company = "SELECT * FROM LOCATION WHERE ID = "+ str(location_id)

    cursor.execute(query_validate_company)
    rows = cursor.fetchone()

    if rows is None:
        return "invalid company"

    # SENSOR CREATION

    sensor_api_key = secrets.token_hex(10)

    query = "INSERT INTO SENSOR(LOCATION_ID, SENSOR_NAME, SENSOR_CATEGORY, SENSOR_META, SENSOR_API_KEY) VALUES (" + str(location_id) + ", '" + sensor_name + "', '" + sensor_category + "', '" + sensor_meta + "', '" + sensor_api_key + "')"

    cursor.execute(query)

    db.commit()

    return "sensor created"
    