from time import sleep
from flask import Flask, render_template, request
#import stepper

app = Flask(__name__)
# state description:
# 0: error
# 1: nominal, ready to accept commands
# 2: moving, wait until ready
state = 1
#stepper = stepper.MotorDriver

@app.route("/")
@app.route("/panel")
def pageMain():
    return render_template('panel.html')


@app.route("/info")
def pageInfo():
    return render_template('info.html')

@app.route("/settings")
def pageSettings():
    return render_template('settings.html')

@app.route("/_moveSteppers")
def moveSteppers():
    global state
    angle = request.args.get('angle')
    print(angle)
    state = 2
    #move motors here
    #stepper.move()
    sleep(int(angle)) #just for testing
    state = 1
    return "ok"

@app.route("/_checkState")
def checkState():
    #can be improved to show more states than just two, maybe even error codes
    return str(state)

@app.route("/_emergencyStop")
def emergencyStop():
    #implement emergency stop
    pass


app.run(host='0.0.0.0', port=80, debug=True)