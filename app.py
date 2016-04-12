from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import config
import json


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))

    def __init__(self, title):
        self.title = title

    @classmethod
    def new(self, title):
        event = Event(title)
        db.session.add(event)
        db.session.commit()
        return event


@app.route('/events', methods=['POST'])
def event_list():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        title = data['title']
        event = Event.new(title)
        return jsonify(title=event.title), 201


if __name__ == '__main__':
    app.run()
