from backend.entities.user import User
from backend.manager import db

def createUser(data):
    try :
        user = User(username = data['username'], email = data['email']) #TODO :Password add
        db.session.add(user)
        db.session.commit()
        return user

    except Exception as e:
        return (str(e))
        