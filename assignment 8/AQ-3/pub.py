import paho.mqtt.client as mqtt

client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
client.connect("localhost", 1883, 60)

# Take input from user
pulse = input("Enter Pulse Rate: ")
spo2 = input("Enter SpO2 Level: ")

# Publish both values
client.publish("health/pulse", pulse)
client.publish("health/spo2", spo2)

print("Pulse sent:", pulse)
print("SpO2 sent:", spo2)

client.disconnect()
