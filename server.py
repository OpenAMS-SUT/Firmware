from socket import AI_PASSIVE
from time import sleep
from flask import Flask, render_template, request
from stepper import *

app = Flask(__name__)
# state description:
# 0: error
# 1: nominal, ready to accept commands
# 2: moving, wait until ready
state = 1

driver = MotorDriver()


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
    global state, position
    angle = request.args.get('angle')
    axis = request.args.get('axis')
    state = 2

    # Move motors here
    if(axis == '0'):
        driver.move_inc(MOTOR_AZ, float(angle))
    else:
        driver.move_inc(MOTOR_EL, float(angle))

    state = 1
    return "ok"


@app.route("/_checkState")
def checkState():
    # can be improved to show more states than just two, maybe even error codes
    return str(state)


@app.route("/_emergencyStop")
def emergencyStop():
    # implement emergency stop
    pass


@app.route("/_checkPosition")
def checkPosition():
    return str(round(driver.get_pos(MOTOR_AZ), 2)) + ', ' + str(round(driver.get_pos(MOTOR_EL), 2))


app.run(host='0.0.0.0', port=80, debug=True)
