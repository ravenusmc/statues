from flask import Flask, jsonify, request
from flask_cors import CORS

# Files that I built
from db import *
from user import *

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# This route will allow new users to register on the site


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        db = Connection()
        post_data = request.get_json()
        user = User(post_data['firstName'], post_data['lastName'], post_data['email'], 
        post_data['userName'], post_data['password'])
        hashed = db.encrypt_pass(post_data)
        user_created = db.insert(user, hashed)
        print(user_created)
        # return jsonify(user_created)
        return jsonify('7')


if __name__ == '__main__':
    app.run()