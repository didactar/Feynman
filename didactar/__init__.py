from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask.ext.cors import CORS

from didactar.me.api import me
from didactar.events.api import events
from didactar.topics.api import topics

from didactar.database import db


def create_app(config_object):

    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db.init_app(app)

    app.register_blueprint(me, url_prefix='/api/v1')
    app.register_blueprint(events, url_prefix='/api/v1')
    app.register_blueprint(topics, url_prefix='/api/v1')

    return app
