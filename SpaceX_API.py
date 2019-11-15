import json, requests
from flask import make_response
from flask import Flask
app = Flask(__name__)

@app.route("/next", methods=['GET'])
def next():
    response = requests.get("https://api.spacexdata.com/v3/launches/next")
    flight = json.loads(response.content)
    return make_response(flight, 200)

@app.route("/latest", methods=['GET'])
def latest():
    response = requests.get("https://api.spacexdata.com/v3/launches/latest")
    flight = json.loads(response.content)
    return make_response(flight, 200)

@app.route("/past", methods=['GET'])
def past():
    response = requests.get("https://api.spacexdata.com/v3/launches/past")
    flights = {'flights': json.loads(response.content)}
    return make_response(flights, 200)

@app.route("/upcoming", methods=['GET'])
def upcoming():
    response = requests.get("https://api.spacexdata.com/v3/launches/upcoming")
    flights = {'flights': json.loads(response.content)}
    return make_response(flights, 200)

if __name__ == "__main__":
    app.run()