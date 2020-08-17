from flask import Flask, render_template
from flask import jsonify

app = Flask(__name__)


@app.route("/")
def landingPage():
    return render_template("index.html")


@app.route("/form")
def inputForm():
    return render_template("form.html")


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True)
