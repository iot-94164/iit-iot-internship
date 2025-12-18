
import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)

sensor_id = input("Enter sensor_id whose moisture level to be updated : ")
moisture_level = input("Enter moisture level : ")

query = f"update moisture_readings SET moisture_level = '{moisture_level}' where sensor_id = '{sensor_id}';"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()
