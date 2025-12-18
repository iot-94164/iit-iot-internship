# import mysql connector
import mysql.connector

# establish connection with mysql server
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)

# form a query to be executed
sensor_id = int(input("Enter id : "))
moisture_level = input("Enter moisture level: ")
date_time = input("Enter date and time : ")

query = """ 
INSERT INTO moisture_readings (sensor_id, moisture_level, date_time) 
VALUES (%s, %s, %s) 
"""

cursor = connection.cursor()

cursor.execute(query, (sensor_id, moisture_level, date_time))

connection.commit()

cursor.close()

connection.close()
