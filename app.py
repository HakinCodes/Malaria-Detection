from flask import Flask, jsonify

app = Flask(__name__)

"""@app.route("/")
def hello():
    return jsonify({'message' : 'Hello!'})
@app.route("/date")
def getDate():
    import datetime
    return jsonify({'message' : datetime.datetime.utcnow().isoformat()})"""


@app.route("/")
def landingPage():
    return jsonify({"message": "Hello! this is the landing page."})


@app.route("/form")
def inputForm():
    return jsonify({"message": "This form contains only one required input field."})


@app.route("/result")
def result():
    return jsonify(
        {
            "message": "The Result is either presented as a Malarial Cell or not a Malarial Cell."
        }
    )


if __name__ == "__main__":
    app.run(debug=True)
