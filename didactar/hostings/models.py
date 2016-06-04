from database import db


class Hosting(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data):
        self.event_id = data.get('event').get('id')
        self.user_id = data.get('user').get('id')

    @classmethod
    def get_by_id(self, id):
        return Hosting.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
