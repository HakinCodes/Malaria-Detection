import json

from flask import Flask
from flask import jsonify
from flask import render_template

app = Flask(__name__)


with open("config.json", "r") as c:
    params = json.load(c)["params"]


@app.route("/")
def landingPage():
    return render_template("index.html")


@app.route("/form")
def inputForm():
    return render_template("form.html")


@app.route("/result")
def result():
    return render_template("result.html")


@app.route("/team")
def team():
    return render_template("team.html", params=params)


@app.errorhandler(404)
# inbuilt function which takes error as parameter
def not_found(e):

    return render_template("404.html")


if __name__ == "__main__":
    try:
        app.run(debug=True)
    except:
        print("Error")
