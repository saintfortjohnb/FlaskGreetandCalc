# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def addition():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def subtraction():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def multiplication():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def division():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))

operations = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div,
}

@app.route('/math/<operation>')
def math(operation):
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = operations.get(operation, None)

    if result:
        return str(result(a, b))
    else:
        return f"Invalid operation: {operation}", 400
