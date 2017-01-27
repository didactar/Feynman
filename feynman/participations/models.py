from database import db


class Participation(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, data):
        self.event_id = data.get('event').get('id')
        self.user_id = data.get('user').get('id')

    @classmethod
    def get_by_id(self, id):
        return Participation.query.filter_by(id=id).first()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def serialize(self):
        return {
            'id': self.id,
            'event': {'id': self.event.id},
            'user': {'id': self.user.id}
       }

    @classmethod
    def serialize_event_participations_list(self, participations):
        return {
            'data': [{
                'id': p.id,
                'user': {
                    'id': p.user.id,
                    'username': p.user.username,
                    'name': p.user.name,
                    'about': p.user.about,
                    'avatar': p.user.avatar
                }
            } for p in participations]
        }

    @classmethod
    def serialize_user_participations_list(self, participations):
        return {
            'data': [{
                'id': p.id,
                'event': {
                    'id': p.event.id, 
                    'title': p.event.title, 
                    'slug': p.event.slug,
                    'channel': {
                        'id': p.event.channel.id,
                        'slug': p.event.channel.slug,
                        'name': p.event.channel.name,
                        'avatar': p.event.channel.avatar
                    },
                    'description': p.event.description,
                    'participationCount': p.event.participations_count
                }
            } for p in participations]
        }
