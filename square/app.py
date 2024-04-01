from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/square/<int:number>', methods=['GET'])
def square(number):
    result = number ** 2
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=False, port=50002)
