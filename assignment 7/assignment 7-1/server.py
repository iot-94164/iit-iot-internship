
from flask import Flask, request

from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def homepage():
    return "<html><body><h1>This is home page</h1></body></html>"

@server.post('/readings')
def create_reading():
   
    id = request.form.get('id')
    temperature= request.form.get('temperature')
    humidity= request.form.get('humidity')
    timestamp = request.form.get('timestamp')

    query = f"insert into sensor_readings values({id}, '{temperature}', '{humidity}', '{timestamp}');"

    executeQuery(query=query)

    return "readings is added successfully"

@server.get('/readings')
def retrieve_readings():
    
    query = "select * from sensor_readings;"

    data = executeSelectQuery(query=query)

    return f"sensor_readings : {data}"

@server.put('/readings')
def update_readings():
    
    id = request.form.get('id')
    temperature = request.form.get('temperature')

    query = f"update sensor_readings SET temperature= '{temperature}' where id = '{id}';"

    executeQuery(query=query)

    return "temperature is updated successfully"

@server.delete('/readings')
def delete_readings():
   
    id = request.form.get('id')

    query = f"delete from sensor_readings where id = '{id}';"

    executeQuery(query=query)

    return "readings is deleted successfully"

@server.get('/readings/below')
def readings_below_threshold():
    threshold = request.form.get('temperature')

    query = f"select * from sensor_readings where temperature < '{threshold}';"

    data = executeSelectQuery(query=query)

    return f"sensor_readings below temperature {threshold}: {data}"


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)


