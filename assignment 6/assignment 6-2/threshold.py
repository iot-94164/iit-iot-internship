import mysql.connector

connection=mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_soilmoisture",
    use_pure = True
)

query = "select * from moisture_readings where moisture_level >50";

cursor = connection.cursor()

cursor.execute(query)

moisture_readings = cursor.fetchall()

for readings in moisture_readings:
    print(readings)
   
cursor.close()

connection.close()