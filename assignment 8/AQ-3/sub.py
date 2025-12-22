import paho.mqtt.client as mqtt
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="healthcare_iot"
)
cursor = db.cursor()

pulse_value = None
spo2_value = None

def on_message(client, userdata, message):
    global pulse_value, spo2_value

    topic = message.topic
    payload = message.payload.decode()

    # Handle alert topic
    if topic == "health/alert":
        print("Doctor Alert:", payload)
        return

    value = int(payload)

    if topic == "health/pulse":
        pulse_value = value
        print("Pulse =", pulse_value)

        if pulse_value > 100:
            alert_msg = f"ALERT: Pulse above threshold ({pulse_value})"
            client.publish("health/alert", alert_msg)

    elif topic == "health/spo2":
        spo2_value = value
        print("SpO2 =", spo2_value)

        if spo2_value < 95:   # ✅ FIXED
            alert_msg = f"ALERT: SpO2 below threshold ({spo2_value})"
            client.publish("health/alert", alert_msg)

    # Insert into DB only when both values are received
    if pulse_value is not None and spo2_value is not None:
        query = "INSERT INTO health_data (pulse, spo2) VALUES (%s, %s)"
        cursor.execute(query, (pulse_value, spo2_value))
        db.commit()

        print("✅ Data stored in database")

        pulse_value = None
        spo2_value = None

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.on_message = on_message

client.connect("localhost", 1883, 60)
client.subscribe("health/pulse")
client.subscribe("health/spo2")
client.subscribe("health/alert")

print("Subscriber running...")
client.loop_forever()
