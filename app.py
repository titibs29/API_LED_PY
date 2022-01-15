from flask import Flask, url_for, request, render_template
from markupsafe import escape
import RPi.GPIO as gpio

gpio.setmode(gpio.BOARD)

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html'), 200


@app.route('/setup/out/<int:pin>')
def setupOut(pin=None):
    gpio.setup(pin, gpio.OUT)
    return 'pin setup correctly'


@app.route('/setup/in/<int:pin>')
def setupIn(pin):
    gpio.setup(pin, gpio.IN)
    return 'pin setup correctly'


@app.route('/set/<int:pin>/<int:state>')
def output(pin, state):
    gpio.output(pin, state)
    return 'value modified'


@app.route('/get/<int:pin>')
def input(pin):
    value = gpio.input(pin)
    return value


@app.route('/clean')
def cleanAll():
    gpio.cleanup()
    return 'outputs cleaned'


@app.route('/clean/<int:pin>')
def cleanOne(pin):
    gpio.cleanup(pin)
    return 'outputs cleaned'


with app.test_request_context():
    print(url_for('index'))
    print(url_for('setupOut', pin = 20))
    print(url_for('setupIn', pin = 20))
    print(url_for('output', pin = 20, state = 1))
    print(url_for('input', pin = 20))
    print(url_for('cleanAll'))
    print(url_for('cleanOne', pin = 20))
