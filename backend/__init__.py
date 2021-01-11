import os
from flask import Flask
from backend.routes.users import users
from backend.manager import db, migrate

def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(os.environ['APP_SETTINGS'])

    # registering the blueprints
    app.register_blueprint(users)

    #ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # initializing the db
    db.init_app(app)
    migrate.init_app(app, db)

    return app