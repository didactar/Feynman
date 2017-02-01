from feynman.me.api import me
from feynman.users.api import users
from feynman.events.api import events
from feynman.workshops.api import workshops
from feynman.participations.api import participations


BLUEPRINTS = [me, users, events, workshops, participations]


def register_blueprints(app):
    for blueprint in BLUEPRINTS:
        app.register_blueprint(blueprint, url_prefix='/api/v1')
