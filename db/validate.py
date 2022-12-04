import sqlite3

def validate(company_api_key, id):
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # QUERY
    query = "SELECT COMPANY_API_KEY FROM COMPANY WHERE COMPANY_API_KEY = '"+ company_api_key+"' "
    result = cursor.execute(query)

    return True