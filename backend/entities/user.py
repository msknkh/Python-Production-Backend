from backend.manager import db

class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    bio = db.Column(db.String, nullable = True)
    image = db.Column(db.String, nullable = True)

    def __init__(self, email, username):
        self.email = email
        self.username = username
    
    def __repr__(self):
        return '<username {}>'.format(self.username)
    
    def serialize(self):
        return {"email": self.email,
                "username": self.username,
                "bio": self.bio,
                "image": self.image}

# {
#   "user": {
#     "email": "jake@jake.jake",
#     "token": "jwt.token.here", //TODO
#     "username": "jake",
#     "bio": "I work at statefarm",
#     "image": null
#   }
# }