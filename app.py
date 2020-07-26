from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({'message' : 'Hello!'})
@app.route("/date")
def getDate():
    import datetime
    return jsonify({'message' : datetime.datetime.utcnow().isoformat()})

if __name__ == "__main__":
    app.run(host='0.0.0.0')
