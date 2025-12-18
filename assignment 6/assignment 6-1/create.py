import mysql.connector

connection=mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id=int(input("enter id: "))
temperature=input("enter temperature: ")
humidity=input("enter humidity: ")
timestamp=input("enter timestamp:")

query = """ 
INSERT INTO sensor_readings (id,temperature,humidity, timestamp) 
VALUES (%s, %s, %s, %s) 
"""
cursor = connection.cursor()

cursor.execute(query, (id,temperature,humidity, timestamp))

connection.commit()

cursor.close()

connection.close()

