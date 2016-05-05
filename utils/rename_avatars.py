import json
from slugify import slugify


def new_avatar_name(user):
    extension = ''
    avatar = user.get('avatar')
    if avatar:
        if avatar[-4] == '.':
            extension = avatar[-4:]
        elif avatar[-5] == '.':
            extension = avatar[-5:]
    name = user.get('name', None)
    username = slugify(name, to_lower=True)
    return username + extension


def reformat(user):
    name = user.get('name')
    avatar = user.get('avatar')
    return {
        'name': name,
        'avatar': slugify(name, to_lower=True),
        'avatarURL': avatar
    }


with open('./users_old.json') as f:    
    with open('./users_new.json', 'w') as new_f:
        users = json.load(f)
        new_users= [reformat(user) for user in users]
        json.dump(new_users, new_f, indent=4) 
