import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("localhost", 1883, 60)

appliance = input("Enter appliance name (Light/Fan/AC): ")
status = input("Enter status (ON/OFF): ")

message = f"{appliance},{status}"
client.publish("home/appliance/control", message)

print("Command sent:", message)

client.disconnect()
