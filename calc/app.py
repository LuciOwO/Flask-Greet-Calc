from flask import Flask, request
from operations import MathOperations

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <h1>Home Page</h1>
    """
    return html

@app.route('/add')
def do_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    x = MathOperations(a, b)
    result = x.add()

    return str(result)

@app.route('/sub')
def do_sub():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    x = MathOperations(a, b)
    result = x.sub()

    return str(result)

@app.route('/mult')
def do_mult():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    x = MathOperations(a, b)
    result = x.mult()

    return str(result)

@app.route('/div')
def do_div():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    x = MathOperations(a, b)
    result = x.div()

    return str(result)