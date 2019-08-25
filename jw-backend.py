from flask import Flask, jsonify, request
from gevent.pywsgi import WSGIServer
import random

app = Flask(__name__)

wrong_reasons = [
    "Definitely.",
    "Does a bear shit in the woods?",
    "Big wrong.",
    "Bongus Wrongus.",
    "Yurp",
    "Is a frog's ass water tight?",
    "Is a bear catholic?",
    "Does the pope shit in the woods?",
    "Is the pope catholic?",
    "Does a Polish rifle shoot white flags?",
    "Is the atomic weight of Cobalt 58.9?",
    "Is the space pope reptilian?",
    "Beeg Beeg",
    "Wrongo Bongo" ]

# Add cors headers after the fact
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    if request.method == 'OPTIONS':
        response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
        headers = request.headers.get('Access-Control-Request-Headers')
        if headers:
            response.headers['Access-Control-Allow-Headers'] = headers
    return response
app.after_request(add_cors_headers)

@app.route('/wrong-reason')
def wrong_reason():
    idx = random.randint(0,len(wrong_reasons)-1)
    response = {
        'reason': wrong_reasons[idx]
    }

    return jsonify(response)

if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()