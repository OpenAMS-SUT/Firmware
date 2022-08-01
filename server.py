from flask import Flask, render_template, request

app = Flask(__name__)

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
    angle = request.args.get('angle')
    print(angle)
    return "ok"


app.run(host='0.0.0.0', port=80, debug=True)