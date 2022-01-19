from flask import Flask, jsonify, request
from flask_cors import CORS

# Files that I built
from db import *
from user import *
from clean import *
from data import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        user = User(post_data['firstName'], post_data['lastName'], post_data['email'],
                    post_data['userName'], post_data['password'])
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(user, hashed)
        return jsonify(user_created)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        username = post_data['userName']
        password = post_data['password']
        login_values = {}
        # Checking to see if the user is in the database
        login_flag, not_found, password_no_match, user = db.check(
            username, password)
        login_values['login_flag'] = login_flag
        login_values['Not_found'] = not_found
        login_values['Password_no_match'] = password_no_match
        login_values['user'] = user
    return jsonify(login_values)


@app.route('/fetch_north_south_by_year', methods=['GET', 'POST'])
def graphOne():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        first_chart_data = data.build_north_south_graph(post_data)
    return jsonify(first_chart_data)


@app.route('/fetch_north_south_by_year_drilldown', methods=['GET', 'POST'])
def graphOneDrillDown():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        statues_data_set_by_year_drill_down = data.build_north_south_graph_drill_down(
            post_data)
    return jsonify(statues_data_set_by_year_drill_down)


@app.route('/fetch_top_five_by_year', methods=['GET', 'POST'])
def graphTwo():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        statues_data_set_by_year_drill_down = data.build_top_five_graph(
            post_data)
    return jsonify('5')


if __name__ == '__main__':
    app.run()
