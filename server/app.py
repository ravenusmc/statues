from flask import Flask, jsonify, request
from flask_cors import CORS

# Files that I built
from db import *
from user import *
from clean import *
from data import *
from support import *

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
        support = Support()
        post_data = request.get_json()
        statues_data_set_by_year_drill_down = data.build_north_south_graph_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(
            statues_data_set_by_year_drill_down)
    return jsonify(drill_down_data)


@app.route('/fetch_top_five_by_year', methods=['GET', 'POST'])
def graphTwo():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        second_chart_data = data.build_top_five_graph(
            post_data)
    return jsonify(second_chart_data)


@app.route('/fetch_north_south_by_state_drilldown', methods=['GET', 'POST'])
def graphTwoDrillDown():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        statues_data_set_by_year_drill_down_two = data.build_graph_two_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(
            statues_data_set_by_year_drill_down_two)
    return jsonify(drill_down_data)


@app.route('/fetch_Statues_Single_State', methods=['GET', 'POST'])
def graphThree():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        third_chart_data = data.build_singe_state_graph(
            post_data)
    return jsonify(third_chart_data)


@app.route('/fetch_drilldown_graph_three', methods=['GET', 'POST'])
def graphThreeDrillDown():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        statues_data_drill_down_three = data.build_graph_three_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(statues_data_drill_down_three)
    return jsonify(drill_down_data)

@app.route('/fetch_drilldown_graph_four', methods=['GET', 'POST'])
def graphFourDrillDown():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        statues_data_drill_down_four = data.build_graph_four_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(statues_data_drill_down_four)
    return jsonify(drill_down_data)

@app.route('/fetch_drilldown_graph_five', methods=['GET', 'POST'])
def graphFiveDrillDown():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        statues_data_drill_down_five = data.build_graph_five_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(statues_data_drill_down_five)
    return jsonify(drill_down_data)

@app.route('/fetch_data_for_graph_six', methods=['GET', 'POST'])
def graphSix():
    if request.method == 'POST':
        data = Data()
        post_data = request.get_json()
        sixth_chart_data = data.build_graph_six_data(
            post_data)
    return jsonify(sixth_chart_data)

@app.route('/fetch_drilldown_graph_six', methods=['GET', 'POST'])
def graphSixDrillDown():
    if request.method == 'POST':
        data = Data()
        support = Support()
        post_data = request.get_json()
        statues_data_drill_down_six = data.build_graph_six_drill_down(
            post_data)
        drill_down_data = support.build_drill_down_rows(statues_data_drill_down_six)
    return jsonify(drill_down_data)

@app.route('/get_specific_discussion_data', methods=['GET', 'POST'])
def get_specific_discussion_data():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        selected_graph_number = post_data['selectedGraphDiscussion']
        graph_discussion_points = db.get_specific_discussion_by_graph(selected_graph_number)
    return jsonify(graph_discussion_points)

@app.route('/add_discussion_post', methods=['GET', 'POST'])
def add_discussion_post():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        db.insert_new_discussion_point(post_data)
        selected_graph_number = post_data['graph_number']
        graph_discussion_points = db.get_specific_discussion_by_graph(selected_graph_number)
    return jsonify(graph_discussion_points)


if __name__ == '__main__':
    app.run()
