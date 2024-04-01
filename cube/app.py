import logging
from flask import Flask, request, jsonify

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/cube/<int:number>', methods=['GET'])
def cube(number):
    logger.info("Cube")
    result = number ** 3
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=False, port=50003)
