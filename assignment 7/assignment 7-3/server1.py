from flask import Flask, request
from utils.executeQuery import executeQuery
from utils.executeSelectQuery import executeSelectQuery

server = Flask(__name__)

@server.get('/')
def home():
    return "<h1>Smart Home Monitoring System</h1>"


@server.route('/update', methods=['POST'])
def update_status():
    data = request.get_json()

    light_status = data.get('light_status')   # ON / OFF
    fan_status = data.get('fan_status')       # ON / OFF
    temperature = data.get('temperature')

    query = f"""
        INSERT INTO smart_home (light_status, fan_status, temperature)
        VALUES ('{light_status}', '{fan_status}', {temperature});
    """

    executeQuery(query=query)

    return "Smart home data updated successfully"

@server.route('/status', methods=['GET'])
def get_status():
    query = """
        SELECT light_status, fan_status, temperature
        FROM smart_home
        ORDER BY updated_at DESC
        LIMIT 1;
    """

    data = executeSelectQuery(query=query)

    if not data:
        return "No data available"

    status = data[0]

    return {
        "light_status": status[0],
        "fan_status": status[1],
        "temperature": status[2]
    }

if __name__ == '__main__':
    server.run(host='0.0.0.0', port=4000, debug=True)
