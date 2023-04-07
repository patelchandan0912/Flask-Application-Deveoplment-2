from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World"

@app.route("/mytest/")
@app.route("/mytest/<name>")  ## data in here as name pass it to html
def hello_there(name=None): 
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now() ## So when data comes here we get the data in the server not delivered to the client. So we can do lot of things here with the data.
    )

@app.route("/api/data")
def get_data():
    return "Hello data"

@app.route("/test/")
def get_test():
    return "Hello Test"