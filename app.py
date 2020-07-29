from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>welcome to my page!</h1><img src="static/111.jpg"/>'