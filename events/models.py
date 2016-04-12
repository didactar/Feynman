from database import db

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
