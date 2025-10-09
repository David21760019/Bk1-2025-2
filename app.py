from flask import Flask
from flask import render_template
app = Flask(__name__)
from flask import Flask, jsonify

data = {
    "name":"alice",
    "age":30,
    "city":"New York",
    "is_student": False,
    "hobbies": ["reading","coding"]
    }

@app.route("/")
def hello_world():
    return  "<queen><h1><Holaaaaaa /h1<</queen>"
@app.route("/jason")
def saluda():
    return data

@app.route("/json")
def saludajson():
    return jsonify(data)

@app.route("/index")
@app.route("/index/<name>")
def pagina(name=None):
    return render_template('index.html', person=name)
