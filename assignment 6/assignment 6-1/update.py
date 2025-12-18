import mysql.connector

connection=mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

id = input("Enter id whose humidity to be updated : ")
humidity= input("Enter new humidity : ")

query = f"update sensor_readings SET humidity = {humidity} where id = {id};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()