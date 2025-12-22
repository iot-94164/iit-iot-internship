import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="iot_smarthome"
)
cursor = db.cursor()

def on_message(client, userdata, msg):
    topic = msg.topic
    value = msg.payload.decode()
    time = datetime.now()

    print("Received:", topic, value)

    if topic == "sensor/ldr":
        query = """
        INSERT INTO smart_home (light_status, updated_at)
        VALUES (%s, %s)
        """
        cursor.execute(query, (value, time))

    elif topic == "sensor/lm35":
        query = """
        INSERT INTO smart_home (temperature, updated_at)
        VALUES (%s, %s)
        """
        cursor.execute(query, (value, time))

    db.commit()

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("sensor/ldr")
client.subscribe("sensor/lm35")

client.on_message = on_message

print("Subscriber running...")
client.loop_forever()
