import mysql.connector 

def getDBConnection():
    connection=mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="root",
        database="iot_soilmoisture",
        use_pure=True
    )

    return connection
