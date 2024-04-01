from flask import Flask, request, jsonify

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@app.route('/prime_check/<int:number>', methods=['GET'])
def prime_check(number):
    result = is_prime(number)
    return jsonify({'number': number, 'is_prime': result})

if __name__ == '__main__':
    app.run(debug=False,port=50004)
