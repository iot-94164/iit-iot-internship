
import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)

sensor_id = int(input("Enter id to be deleted : "))

query = f"delete from moisture_readings where sensor_id = {sensor_id};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()