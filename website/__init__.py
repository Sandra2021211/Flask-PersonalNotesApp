from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db=SQLAlchemy()
DB_NAME="database.db"


def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='absoipoi'

    db_path = os.path.join(os.path.dirname(__file__), DB_NAME)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"

    db.init_app(app)

    from .views import views
    from .auth import auth 

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import Note,User

    create_database(app, db_path)

    return app


def create_database(app, full_db_path):
    if not os.path.exists(full_db_path):
        with app.app_context():
            db.create_all()
            print("Created database at:", full_db_path)