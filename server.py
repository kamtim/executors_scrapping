from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

import json

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

with open("yodo_data.json", "r") as read_file:
    yodo_data = json.load(read_file)

with open("yandex_uslugi_data.json", "r") as read_file:
    yandex_uslugi_data = json.load(read_file)

with open("profi_data.json", "r") as read_file:
    profi_data = json.load(read_file)

data = yodo_data + yandex_uslugi_data + profi_data


@app.route('/')
def hello():
    return "Hello, it is my app!"


@app.route('/results/')
@cross_origin()
def get_results():
    print(jsonify(data))
    return jsonify(data)

if __name__ == '__main__':
    app.run()
