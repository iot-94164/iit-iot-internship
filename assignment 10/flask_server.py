from flask import Flask
import mysql.connector
from datetime import datetime
import paho.mqtt.publish as publish

server = Flask(__name__)


def getDBConnection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="iot_soilmoisture"
    )

MQTT_BROKER = "127.0.0.1"
MQTT_TOPIC = "soil/alert"
THRESHOLD = 30

@server.get('/')
def home():
    return "Soil Moisture Server Running"

@server.post('/moisture/<int:sensor_id>/<int:moisture>')
def post_moisture(sensor_id, moisture):
    print(f"Sensor ID = {sensor_id}")
    print(f"Moisture Level = {moisture}")

    now = datetime.now()

    # Store in database
    conn = getDBConnection()
    cursor = conn.cursor()

    query = """
    INSERT INTO moisture_readings (sensor_id, moisture_level, date_time)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (sensor_id, moisture, now))
    conn.commit()

    cursor.close()
    conn.close()

    # MQTT alert
    if moisture < THRESHOLD:
        msg = f"ALERT! Low moisture {moisture} at Sensor {sensor_id}"
        publish.single(MQTT_TOPIC, msg, hostname=MQTT_BROKER)

    return f"Moisture {moisture} stored for Sensor {sensor_id}"

@server.get('/moisture')
def get_moisture():
    conn = getDBConnection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM moisture_readings")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    result = ""
    for r in rows:
        result += f"Sensor:{r[0]} | Moisture:{r[1]} | Time:{r[2]}<br>"

    return result


server.run(host='0.0.0.0', port=4000, debug=True)
