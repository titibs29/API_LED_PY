from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "html/index.html"

@app.route("/<name>")
def hello(name):
	return f"Hello, {escape(name)}!"
