from backend.manager import db, bcrypt

class User(db.Model):
    __tablename__ = 'users'

    email = db.Column(db.String, primary_key = True)
    username = db.Column(db.String(25), unique = True, nullable = False)
    password = db.Column(db.Binary(128), nullable = False)
    bio = db.Column(db.String, nullable = True)
    image = db.Column(db.String, nullable = True)
    #articles = db.relationship("Article", backref=db.backref('articles'))
    token: str = ''


    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.set_password(password)
    
    def __repr__(self):
        return '<username {}>'.format(self.username)
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)
    
    def check_password(self, value):
        return bcrypt.check_password_hash(self.password, value)
    
    def serialize(self):
        return {"email": self.email,
                "username": self.username,
                "bio": self.bio,
                "image": self.image,
                "token": self.token}

# {
#   "user": {
#     "email": "jake@jake.jake",
#     "token": "jwt.token.here", 
#     "username": "jake",
#     "bio": "I work at statefarm",
#     "image": null
#   }
# }