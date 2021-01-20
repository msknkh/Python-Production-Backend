from flask import Blueprint, request, jsonify
from backend.controllers.articles import createArticle
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity

articles = Blueprint('articles', __name__)

#POST /api/articles
@articles.route('/api/articles', methods = ["POST"])
def add_article():
    try: 
        data = request.get_json()
        verify_jwt_in_request()
        author_username = get_jwt_identity()
        article = createArticle(author_username, data['article'])
        return jsonify(article), 201
    
    except Exception as e:
        return jsonify({"errors":{"body": ["Adding the article failed", str(e)]}}), 422
        
#TODO: Check error code

#PUT /api/articles/:slug

#GET /api/articles

#GET /api/articles/:slug

#DELETE /api/articles/:slug

