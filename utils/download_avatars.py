import requests
from slugify import slugify
import json
import shutil


def download(name, avatar):
    print('downloading avatar for ' + user['name'])
    r = requests.get(avatar) 
    if r.status_code == 200:
        username = slugify(name, to_lower=True)
        with open('./users/' + username, 'wb') as f:
            #r.raw.decode_content = True
            #shutil.copyfileobj(r.raw, f)      
            f.write(r.content)


filename = './users_old.json'
with open(filename) as f:    
    for user in json.load(f):
        download(user['name'], user['avatar'])
