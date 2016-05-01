import argparse
from didactar import create_develop_app
from didactar import create_test_app
from didactar.database import db

from didactar.utils.populate import populate_database


def parse_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--resetdb', dest='reset_db', action='store_true', default=False)
    parser.add_argument('--populate', dest='populate_db', action='store_true', default=False)
    parser.add_argument('--test', dest='test_server', action='store_true', default=False)
    parser.add_argument('--develop', dest='dev_server', action='store_true', default=False)
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    
    if args.reset_db:
        app = create_develop_app()
        with app.app_context():
            db.reflect()
            db.drop_all()
            db.create_all()

    if args.populate_db:
        populate_database()

    if args.test_server:
        app = create_test_app()
        app.run(threaded=True)

    if args.dev_server:
        app = create_develop_app()
        app.run(threaded=True)
