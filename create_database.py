from flask import Flask
from database import db
import config

from events.api import events
from topics.api import topics

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(events)
app.register_blueprint(topics)

with app.app_context():
    db.reflect()
    db.drop_all()
    db.create_all()
