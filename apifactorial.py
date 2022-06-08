from flask import Flask
import math

app = Flask(__name__)


@app.route('/factorial/<n>')
def factorial(n):
    n = int(n)
    result = math.factorial(n)
    return "El resultado es " + str(result)

@app.route('/fibonacci/<n>')
def fibonacci(n):
    #return str(round(1.61803**(int(n)) / 5**0.5))
    n = int(n)
    lis=[1, 1]
    for i in range(n-2):
        lis.append(lis[-1] + lis[-2])
    return str(lis[-1])



app.run(port=5002)
