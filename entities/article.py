from app import db
from datetime import datetime

class Article(db.Model):
    __tablename__ = 'article'

    slug = db.Column(db.String(15), primary_key = True)
    title = db.Column(db.String(50), nullable = False)
    description = db.Column(db.String(100), nullable = False)
    body = db.Column(db.Text, nullable = False)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime)

    def __init__(self, slug, title, description, body, createdAt, updatedAt):
        self.slug = slug
        self.title = title
        self.description = description
        self.body = body
        self.createdAt = createdAt
        self.updatedAt = updatedAt
    
    def __repr__(self):
        return '<slug {}>'.format(self.slug)



# {
#   "article": {
#     "slug": "how-to-train-your-dragon",
#     "title": "How to train your dragon",
#     "description": "Ever wonder how?",
#     "body": "It takes a Jacobian",
#     "tagList": ["dragons", "training"],
#     "createdAt": "2016-02-18T03:22:56.637Z",
#     "updatedAt": "2016-02-18T03:48:35.824Z",
#     "favorited": false,
#     "favoritesCount": 0,
#     "author": {
#       "username": "jake",
#       "bio": "I work at statefarm",
#       "image": "https://i.stack.imgur.com/xHWG8.jpg",
#       "following": false
#     }
#   }
# }
