# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.engine.reflection import Inspector

db = SQLAlchemy()

def init_db(app):
    with app.app_context():
        inspector = Inspector.from_engine(db.engine)
        if 'candidate' not in inspector.get_table_names():
            db.create_all()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///candidates.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # Import routes after db is defined
    from app.routes import app_routes
    app.register_blueprint(app_routes)

    # Initialize the database
    init_db(app)

    return app
