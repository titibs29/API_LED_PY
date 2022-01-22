import RPi.GPIO as gpio
from bottle import Bottle, abort, run

app = Bottle()

pins=[11, 13, 15]
states={}

@app.route('/set/<pin:int>/<state:int>')
def set(pin, state):
    if(pin not in pins):
        abort(code=404,text="pin useless")
    if(state != 1 and state != 0):
        abort(code=400, text='invalid state'+state)

    gpio.output(pin, state)
    states[pin]=state
    return "pin "+str(pin)+" changed to "+str(states[pin])



@app.get('/pins')
def allPins():
    return str(states.keys())

@app.get('/get/<pin:int>')
def get(pin):
    return str(states.get(pin))

@app.get('/get')
def getAll():
    return states

if __name__=="__main__":

    try:

        for pin in pins:
            states[pin]=0

        gpio.setmode(gpio.BOARD)
        gpio.setup(pins, gpio.OUT, initial=gpio.LOW)
        run(app, host='0', port=3000, debug=True, reloader=True)
        
    finally:
        gpio.cleanup(pins)