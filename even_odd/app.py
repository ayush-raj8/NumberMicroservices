from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/even_odd/<int:number>', methods=['GET'])
def even_odd(number):
    result = 'even' if number % 2 == 0 else 'odd'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=False, port=50001)
