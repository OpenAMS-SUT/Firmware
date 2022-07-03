from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def pageMain():
    return render_template('test.html')


app.run(host='0.0.0.0', port=80, debug=True)