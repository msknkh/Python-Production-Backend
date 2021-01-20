from backend.entities.article import Article
from backend.entities.user import User
from backend.manager import db 

def createArticle(username, data):
    try: 
        user = User.query.filter_by(username = username).first()
        article = Article(title = data['title'], description = data['description'], 
                            body = data['body'], author = user)
        db.session.add(article)
        db.session.commit()
        return article.serialize()

   #TODO: handle exceptions
    except Exception as e:
        if User.query.filter_by(username = username) is None:
            raise Exception("No such user exists")
        if 'title' not in data:
            raise Exception("No title provided")
        if 'description' not in data:
            raise Exception("No description provided")
        if 'body' not in data:
            raise Exception("No body provided")
        
        raise Exception(e) 