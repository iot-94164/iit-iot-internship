import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

client.loop_start()

value = input("Enter sensor value: ")
client.publish("sensor/data", value)

time.sleep(1)
client.loop_stop()
client.disconnect()

print("Value sent successfully")
