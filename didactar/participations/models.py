from didactar.database import db


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
    def event_participation_count(self, event):
        return Participation.query.filter_by(event_id=event.id).count()

    @classmethod
    def filter_by_event(self, event):
        return Participation.query.filter_by(event_id=event.id)

    @classmethod
    def filter_by_user(self, user):
        return Participation.query.filter_by(user_id=user.id)

    def get_event_id(self):
        return self.event_id

    def get_user_id(self):
        return self.user_id

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
