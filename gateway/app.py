import logging
from flask import Flask, request, jsonify
import requests

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

EVEN_ODD_MICROSERVICE_URL = 'http://even_odd:50001'
SQUARE_MICROSERVICE_URL = 'http://square:50002'
CUBE_MICROSERVICE_URL = 'http://cube:50003'
PRIME_MICROSERVICE_URL = 'http://prime:50004'

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify("hello")

@app.route('/list_all')
def list_all():
    services = {
        'even_odd': EVEN_ODD_MICROSERVICE_URL,
        'square': SQUARE_MICROSERVICE_URL,
        'cube': CUBE_MICROSERVICE_URL,
        'prime_check': PRIME_MICROSERVICE_URL
    }

    return jsonify(services)

@app.route('/process')
def process():
    logger.info("Process")
    operation = request.args.get('operation')
    number = request.args.get('number')
    logger.info(f"Process {operation} & {number}")
    if operation == 'even_odd':
        response = requests.get(f'{EVEN_ODD_MICROSERVICE_URL}/even_odd/{number}')
    elif operation == 'square':
        response = requests.get(f'{SQUARE_MICROSERVICE_URL}/square/{number}')
    elif operation == 'cube':
        response = requests.get(f'{CUBE_MICROSERVICE_URL}/cube/{number}')
    elif operation == 'prime_check':
        response = requests.get(f'{PRIME_MICROSERVICE_URL}/prime_check/{number}')
    else:
        return jsonify({'error': 'Invalid operation'})

    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=False, port=50000)
