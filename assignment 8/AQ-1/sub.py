import paho.mqtt.client as mqtt
import mysql.connector
from datetime import datetime

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="Smarthome"
)


def on_message(client, userdata, msg):
    print("Received value:", msg.payload.decode())

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.subscribe("sensor/data")
client.on_message = on_message

client.loop_forever()
