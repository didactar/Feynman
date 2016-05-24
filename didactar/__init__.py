from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

from didactar.database import db
from didactar.config import DevelopConfig
from didactar.config import TestConfig

from didactar.me.api import me
from didactar.users.api import users
from didactar.events.api import events
from didactar.channels.api import channels
from didactar.topics.api import topics
from didactar.markings.api import markings
from didactar.participations.api import participations
from didactar.speakerships.api import speakerships 

from didactar.users.models import User
from didactar.events.models import Event
from didactar.topics.models import Topic
from didactar.channels.models import Channel
from didactar.markings.models import Marking
from didactar.participations.models import Participation
from didactar.speakerships.models import Speakership


BASE_URL = 'http://127.0.0.1:5000/api/v1/'


def create_database(app):
    with app.app_context():
        db.reflect()
        db.drop_all()
        db.create_all()


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db.init_app(app)

    blueprints = [
        me, users, events, topics, channels, 
        markings, participations, speakerships
    ]
    for b in blueprints:
        app.register_blueprint(b, url_prefix='/api/v1')
    
    return app


def create_develop_app():
    return create_app(DevelopConfig)


def create_test_app():
    return create_app(TestConfig)


def setup_test_app():
    app = create_test_app()
    ctx = app.app_context()
    ctx.push()
    models = [Event, Topic, Channel, Marking, User, Participation, Speakership]
    for model in models:
        for item in model.query.all():
            item.delete()
    return app
