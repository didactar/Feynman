from didactar.database import db
from didactar.events.models import Event
from didactar.users.models import User

class Participation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data):
        self.event_id = data['event']['id']
        self.user_id = data['user']['id']

    @classmethod
    def get(self, id):
        return Participation.query.filter_by(id=id).first()

    @classmethod
    def filter_by_event(self, slug):
        event_id = Event.get(slug).id
        return Participation.query.filter_by(event_id=event_id)

    @classmethod
    def filter_by_user(self, username):
        user_id = User.get(username).id
        return Participation.query.filter_by(user_id=user_id)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
