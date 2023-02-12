import RPi.GPIO as gpio
from bottle import Bottle, abort, run, static_file

defaultState = gpio.LOW


app = Bottle()

pins = [11, 13, 15]
states = {}


@app.route('/set/<pin:int>/<state:int>')
def set(pin, state):
    if pin not in pins:
        abort(code=404, text="pin useless")
    if not state in (1, 0):
        abort(code=400, text='invalid state '+str(state))

    gpio.output(pin, state)
    states[pin] = state
    return "pin "+str(pin)+" changed to "+str(states[pin])

@app.get('/setAll/<state:int>')
def setAll(state):
    gpio.output(pins, state)
    for pin in states:
        states[pin] = state
    return "all pins changed to "+str(state)


@app.get('/pins')
def allPins():
    return str(pins)


@app.get('/get/<pin:int>')
def get(pin):
    if pin not in pins:
        abort(code=404, text="pin useless")
    return str(states.get(pin))


@app.get('/get')
def getAll():
    return states


@app.get('/switch/<pin:int>')
def switch(pin):
    if not pin:
        abort(code=404, text="pin not provided")
    if pin not in pins:
        abort(code=404, text="pin useless")
    states[pin] = not states[pin]
    gpio.output(pin, states[pin])
    return str(states[pin])


@app.get('/')
def index():
    return static_file("index.html", root="static")


if __name__ == "__main__":

    try:
        # filling the states list
        for pin in pins:
            states[pin] = defaultState

        #setting up the pins
        gpio.setmode(gpio.BOARD)
        gpio.setup(pins, gpio.OUT, initial=defaultState)

        #main server
        run(app, server='paste', host='0', port=3000)

    finally:
        gpio.cleanup(pins)
