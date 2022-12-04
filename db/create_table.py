import sqlite3

def create_tables():
    DB_NAME = 'db/api_db'

    # CONNECT TO DB
    db = sqlite3.connect(DB_NAME)

    # CURSOR DEFINITION
    cursor = db.cursor()

    # CREATE TABLES
    cursor.executescript(
    '''
        CREATE TABLE IF NOT EXISTS ADMIN(
            USERNAME TEXT PRIMARY KEY,
            PASSWORD TEXT
        );

        CREATE TABLE IF NOT EXISTS COMPANY(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPANY_NAME TEXT,
            COMPANY_API_KEY TEXT
        );

        CREATE TABLE IF NOT EXISTS LOCATION(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            COMPANY_ID INTEGER,
            LOCATION_NAME TEXT,
            LOCATION_COUNTRY TEXT,
            LOCATION_CITY TEXT,
            LOCATION_META TEXT,
            FOREIGN KEY (COMPANY_ID) 
                REFERENCES COMPANY (ID) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        );

        CREATE TABLE IF NOT EXISTS SENSOR(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            LOCATION_ID INTEGER,
            SENSOR_NAME INTEGER,
            SENSOR_CATEGORY TEXT,
            SENSOR_META TEXT,
            SENSOR_API_KEY TEXT,
            FOREIGN KEY (LOCATION_ID) 
                REFERENCES LOCATION (ID) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        );

        CREATE TABLE IF NOT EXISTS SENSOR_DATA(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            SENSOR_API_KEY TEXT,
            TIME INTEGER,
            HUMIDITY REAL,
            TEMPERATURE REAL,
            DISTANCE REAL,
            PRESSURE REAL,
            LIGHT_LEVEL REAL,
            FOREIGN KEY (SENSOR_API_KEY) 
                REFERENCES SENSOR (SENSOR_API_KEY) 
                    ON DELETE CASCADE 
                    ON UPDATE NO ACTION
        )
    '''
    )

    # query = '''
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('diego', '123');
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('diego1', '123');
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('diego2', '123');
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('nico', '123');
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('nico1', '123');
    #     INSERT INTO ADMIN(USERNAME, PASSWORD) VALUES ('nico2', '123');
    # '''

    # cursor.executescript(query)

    db.commit()
