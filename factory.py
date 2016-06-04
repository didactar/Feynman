from flask import Flask
from flask.ext.cors import CORS

from database import db

from didactar.me.api import me
from didactar.users.api import users
from didactar.events.api import events
from didactar.channels.api import channels
from didactar.topics.api import topics
from didactar.markings.api import markings
from didactar.participations.api import participations
from didactar.hostings.api import hostings 


BLUEPRINTS = [me, users, events, topics, channels, markings, 
              participations, hostings]


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    CORS(app)
    db.init_app(app)
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/v1')
    return app
