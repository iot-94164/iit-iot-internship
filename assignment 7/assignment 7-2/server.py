
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/readings')
def create_reading():

    sensor_id = request.form.get('sensor_id')
    moisture_level= request.form.get('moisture_level')
    date_time= request.form.get('date_time')

    query = f"insert into moisture_readings values({sensor_id}, '{moisture_level}', '{date_time}');"

    executeQuery(query=query)

    return "readings is added successfully"

@server.get('/readings')
def retrieve_readings():
    
    query = "select * from moisture_readings;"

    data = executeSelectQuery(query=query)

    return f" moisture_readings : {data}"

@server.put('/readings')
def update_readings():
    
    sensor_id = request.form.get('sensor_id')
    moisture_level = request.form.get('moisture_level')

    query = f"update moisture_readings SET moisture_level= '{moisture_level}' where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "moisture_level is updated successfully"

@server.delete('/readings')
def delete_readings():

    sensor_id = request.form.get('sensor_id')

    query = f"delete from moisture_readings where sensor_id = '{sensor_id}';"

    executeQuery(query=query)

    return "readings is deleted successfully"

@server.get('/readings/below')
def readings_below_threshold():
    threshold = request.form.get('moisture_level')

    query = f"select * from moisture_readings where moisture_level < '{threshold}';"

    data = executeSelectQuery(query=query)

    return f"moisture_readings below moisture_level {threshold}: {data}"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)


