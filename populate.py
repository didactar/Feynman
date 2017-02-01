from database import db
from factory import create_app

from feynman.users.utils.populate import populate_users
from feynman.workshops.utils.populate import populate_workshops
from feynman.events.utils.populate import populate_events
from feynman.participations.utils.populate import populate_participations



def populate_db():
    print('populating users...')
    users = populate_users()
    print('populating workshops...')
    workshops = populate_workshops()
    for workshop in workshops:
        print('  populating events...')
        events = populate_events(workshop)
        for event in events:
            print('    populating participations...')
            populate_participations(event, users, 5)



def reset_db():
    db.reflect()
    db.drop_all()
    db.create_all()


if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        reset_db()
        populate_db()
