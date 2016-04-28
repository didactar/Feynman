from flask import Flask
app = Flask(__name__)

import config
app.config.from_object('config.DevelopmentConfig')

from database import db
db.init_app(app)

from flask.ext.cors import CORS
CORS(app)

from me.api import me
app.register_blueprint(me)

from events.api import events
app.register_blueprint(events)

from topics.api import topics
app.register_blueprint(topics)

if __name__ == '__main__':
    app.run(threaded=True)
