from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin

import json

from database.populate import get_all_freelancers_from_database
from apscheduler.schedulers.background import BackgroundScheduler

# from scheduler.scheduled_work import scheduled_work

sched = BackgroundScheduler()
sched.start()

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'


def get_data_from_json():
    with open("scrappers/yodo/yodo_data.json", "r") as read_file:
        yodo_data = json.load(read_file)

    with open("scrappers/uslugi/yandex_uslugi_data.json", "r") as read_file:
        yandex_uslugi_data = json.load(read_file)

    with open("scrappers/profi/profi_data.json", "r") as read_file:
        profi_data = json.load(read_file)

    return yodo_data["Репетиторы и обучение"] + yandex_uslugi_data + profi_data


def get_data_from_database():
    freelancers = get_all_freelancers_from_database()
    serializable_freelancers = []

    for freelancer in freelancers:
        new_freelancer = {
            'id': freelancer.id,
            'name_text': freelancer.name_text,
            'url': freelancer.url,
            'skills': freelancer.skills,
            'image': freelancer.image
        }

        serializable_freelancers.append(new_freelancer)

    return serializable_freelancers


# freelancers = get_data_from_database()


# job = sched.add_job(scheduled_work, 'interval', days=1)


@app.route('/')
def hello():
    return "Hello, it is my app!"


@app.route('/sections/')
@cross_origin()
def get_sections():
    with open("sections/sections.json", "r") as read_file:
        sections = json.load(read_file)

    return sections


@app.route('/freelancers/')
@cross_origin()
def get_results():
    freelancers = get_data_from_database()

    return jsonify(freelancers)


# @app.route('/freelancer/')
# @cross_origin()
# def get_results():
#     id = request.args.get('id')
#
#     return jsonify(freelancers)


if __name__ == '__main__':
    app.run()
