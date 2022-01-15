from flask import Flask, url_for, request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "html/index.html"

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		return 'this is a post login'
	else:
		return 'this is a get login'

@app.route("/user/<name>")
def hello(name):
	return f"Hello, {escape(name)}!"


with app.test_request_context():
	print(url_for('hello_world'))
	print(url_for('hello', name="toi"))
	print(url_for('login'))
