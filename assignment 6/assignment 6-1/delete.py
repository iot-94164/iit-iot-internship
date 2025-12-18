import mysql.connector

connection=mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "iot_data",
    use_pure = True
)

temperature= int(input("Enter temperature of id to be deleted : "))

query = f"delete from sensor_readings where temperature = {temperature};"

cursor = connection.cursor()

cursor.execute(query)

connection.commit()

cursor.close()

connection.close()

