from flask import Blueprint, request, jsonify
from backend.controllers.users import createUser

users = Blueprint('users', __name__)

#Register a new user
@users.route('/api/users/', methods = ["POST"])
def register_user():
    try: 
        data = request.get_json()
        user = createUser(data['user'])
        return jsonify(user.serialize()), 201

    except Exception as e:
        return jsonify({"errors":{ "body": ["Registering the user failed"]}}), 422

#Login an existing user
@users.route('/api/users/login', methods = ["POST"])
def login():
    return "From the user login page"

#Get current user
@users.route('/api/user', methods=('GET',))
def get_user():
    return "From the get user page"

#Update current user
@users.route('/api/user', methods=('PUT',))
def update_user():
    return "From the update user page"
