
from flask import Flask, request

server = Flask(__name__)

@server.get('/')
def homepage():
    return "IoT Sensor Server Running"

@server.post('/upload')
def upload_data():
    temperature = request.form.get("temperature")
    light = request.form.get("light")

    with open("temperature.txt", "a") as t:
        t.write(temperature + "\n")

    with open("light.txt", "a") as l:
        l.write(light + "\n")

    return "Sensor data stored successfully"

@server.get('/temperature')
def show_temperature():
    try:
        with open("temperature.txt", "r") as t:
            data = t.read()
        return f"<h2>Temperature Readings</h2><pre>{data}</pre>"
    except:
        return "No temperature data available"

@server.get('/light')
def show_light():
    try:
        with open("light.txt", "r") as l:
            data = l.read()
        return f"<h2>Light Intensity Readings</h2><pre>{data}</pre>"
    except:
        return "No light data available"

server.run()
