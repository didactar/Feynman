from flask import jsonify
from didactar.users.models import User
from didactar.hostings.models import Hosting
from didactar.participations.models import Participation
from didactar.channels.models import Channel



class EventSerializer():
    
    @classmethod
    def detail(self, event):
        s = event_dict(event)
        return jsonify(s)


    @classmethod
    def list(self, events):
        data = [event_dict(event) for event in events]
        return jsonify(data=data)


    def event_dict(event):
        channel = Channel.get_by_id(event.channel_id) 
        hostings = Hosting.filter_by_event(event)
        return {
            'id': event.id, 
            'title': event.title, 
            'slug': event.slug,
            'channel': {
                'id': channel.id,
                'slug': channel.slug,
                'name': channel.name,
                'avatar': channel.avatar
            },
            'description': event.description,
            'participationCount': Participation.event_participation_count(event),
            'hosts': [host_dict(s) for s in hostings]
        }


    def host_dict(hosting):
        user_id = hosting.get_user_id()
        user = User.get_by_id(user_id)
        return {
            'id': hosting.id,
            'user': {
                'username': user.username,
                'name': user.name,
                'about': user.about,
                'avatar': user.avatar
            }
        }
