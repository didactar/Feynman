from flask import Flask
from flask.ext.cors import CORS

from database import db

from didactar.me.api import me
from didactar.users.api import users
from didactar.events.api import events
from didactar.channels.api import channels
from didactar.participations.api import participations


BLUEPRINTS = [me, users, events, channels, participations]


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db.init_app(app)
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/v1')
    return app
