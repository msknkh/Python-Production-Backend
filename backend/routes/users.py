from flask import Blueprint, request, jsonify
from backend.controllers.users import createUser, loginUser, getUserByUsername, updateUser
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

users = Blueprint('users', __name__)

#Register a new user
@users.route('/api/users/', methods = ["POST"])
def register_user():
    try: 
        data = request.get_json()
        user = createUser(data['user'])
        return jsonify(user), 201

    except Exception as e:
        return jsonify({"errors":{ "body": ["Registering the user failed", str(e)]}}), 422

#Login an existing user
@users.route('/api/users/login', methods = ["POST"])
def login():
    try: 
        data = request.get_json()
        user = loginUser(data['user'])
        return jsonify(user), 200

    except Exception as e:
        return jsonify({"errors":{ "body": ["Login the user failed", str(e)]}}), 422

#Get current user
@users.route('/api/user', methods=('GET',))
def get_user():
    try:
        # Check if header is in correct format and the token recieved is valid 
        verification = verify_jwt_in_request()
        # Access the identity of the current user with get_jwt_identity
        identity = get_jwt_identity()
        user = getUserByUsername(identity)
        return jsonify(user), 200
    except Exception as e:
        return jsonify({"errors":{"body": [str(e)]}}), 422

#Update current user PATCH
@users.route('/api/user', methods=('PATCH',))
def update_user():
    try:
        data = request.get_json()
        # Check if header is in correct format and the token recieved is valid 
        # or else throw exception
        verification = verify_jwt_in_request()
        # Access the identity of the current user with get_jwt_identity
        identity = get_jwt_identity()
        user = updateUser(identity, data['user'])
        return jsonify(user), 200

    except Exception as e:
        return jsonify({"errors":{"body": [str(e)]}}), 422
