from flask import Flask
from configuration import Config
from flask_cors import CORS
from blueprints import register_blueprints
from database import db


def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    app.config.from_object(Config)
    db.init_app(app)
    CORS(app)
    return app
