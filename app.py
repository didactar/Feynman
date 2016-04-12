from flask import Flask
from database import db
import config
from events.api import events

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db.init_app(app)

app.register_blueprint(events)


if __name__ == '__main__':
    app.run()
