from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home_page():
    html = """
    <h1>Home Page</h1>
    """
    return html

@app.route('/welcome')
def welcome():
    html = """
    <h1>Welcome</h1>
    """
    return html

@app.route('/welcome/home')
def welcome_home():
    html = """
    <h1>Welcome Home</h1>
    """
    return html

@app.route('/welcome/back')
    html = """
    <h1>Welcome Back</h1>
    """
    return html