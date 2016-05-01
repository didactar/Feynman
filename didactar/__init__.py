from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

from didactar.database import db
from didactar.config import DevelopConfig
from didactar.config import TestConfig

from didactar.me.api import me
from didactar.events.api import events
from didactar.topics.api import topics
from didactar.markings.api import markings

from didactar.events.models import Event
from didactar.topics.models import Topic
from didactar.markings.models import Marking


BASE_URL = 'http://127.0.0.1:5000/api/v1/'


def clear_database():
    events = Event.query.all()
    topics = Topic.query.all()
    markings = Marking.query.all()
    all_items = events + topics + markings
    for item in all_items:
        item.delete()


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db.init_app(app)

    prefix='/api/v1'
    app.register_blueprint(me, url_prefix=prefix)
    app.register_blueprint(events, url_prefix=prefix)
    app.register_blueprint(topics, url_prefix=prefix)
    app.register_blueprint(markings, url_prefix=prefix)
    
    return app


def create_develop_app():
    return create_app(DevelopConfig)

def create_test_app():
    return create_app(TestConfig)

def setup_test_app():
    app = create_test_app()
    ctx = app.app_context()
    ctx.push()
    clear_database()
    return app
