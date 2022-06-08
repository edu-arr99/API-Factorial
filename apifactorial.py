from flask import Flask
import math

app = Flask(__name__)


@app.route('/factorial/<n>')
def factorial(n):
    n = int(n)
    result = math.factorial(n)
    return "El resultado es " + str(result)



app.run(port=5002)