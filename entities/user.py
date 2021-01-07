from app import db

class User(db.Model):
    __tablename__ = 'user'

    email = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    bio = db.Column(db.String, nullable = True)
    image = db.Column(db.String, nullable = True)

    def __init__(self, email, username, bio, image):
        self.email = email
        self.username = username
        self.bio = bio 
        self.image = image
    
    def __repr__(self):
        return '<username {}>'.format(self.username)

# {
#   "user": {
#     "email": "jake@jake.jake",
#     "token": "jwt.token.here", //TODO
#     "username": "jake",
#     "bio": "I work at statefarm",
#     "image": null
#   }
# }