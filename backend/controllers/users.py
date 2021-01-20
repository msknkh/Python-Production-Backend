from backend.entities.user import User
from backend.manager import db
from flask_jwt_extended import create_access_token

def createUser(data):
    try :
        user = User(username = data['username'], email = data['email'], 
                    password = data['password']) 
        if "image" in data: 
            user.image = data['image']
        if "bio" in data: 
            user.bio = data['bio']
    
        user.token = create_access_token(identity=user.username)
        db.session.add(user)
        db.session.commit()
        return user.serialize()

    except Exception as e:
        if 'username' not in data:
            raise Exception("No username provided")
        if 'email' not in data:
            raise Exception("No email provided")
        if 'password' not in data:
            raise Exception("No password provided")
        if User.query.filter_by(username = data['username']) is not None:
            raise Exception("User already exists")

        raise Exception("Could not add the user to the database")

def loginUser(data):

    if 'email' not in data:
        raise Exception("No email provided")
    if 'password' not in data:
        raise Exception("No password provided")
    
    #User not registered
    user = User.query.filter_by(email = data['email']).first()
    if user is None:
        raise Exception("User does not exist")
    
    #Check if user provided correct password
    password = user.check_password(data['password'])
    if password is False:
        raise Exception("Unauthorised user")

    user.token = create_access_token(identity = user.username, fresh=False)
    return user.serialize()

def getUserByUsername(username):
    try:
        user = User.query.filter_by(username = username).first()
        return user.serialize()
    
    except Exception as e:
        if User.query.filter_by(username = data['username']) is None:
            raise Exception("User does not exists")

        raise Exception(str(e))

def updateUser(username, data):
    try:
        user = User.query.filter_by(username = username).first()
        if "email" in data: 
            user.email = data['email']
        if "username" in data: 
            user.username = data['username']
        if "password" in data: 
            user.set_password(data['password'])
        if "image" in data: 
            user.image = data['image']
        if "bio" in data: 
            user.bio = data['bio']
            
        user.token = create_access_token(identity = user.username, fresh=False)
        db.session.commit()
        return user.serialize()
    
    except Exception as e:
        if User.query.filter_by(username = data['username']) is None:
            raise Exception("User does not exists")

        raise Exception(str(e))
