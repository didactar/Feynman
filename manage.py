import os
import argparse
from didactar import create_develop_app
from didactar import create_test_app
from didactar import create_database
from didactar.database import db

from utils.populate import populate_database


def parse_commandline_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--createdb', dest='create_db', action='store_true', default=False)
    parser.add_argument('--populate', dest='populate_db', action='store_true', default=False)
    parser.add_argument('--test', dest='test_server', action='store_true', default=False)
    parser.add_argument('--develop', dest='dev_server', action='store_true', default=False)
    parser.add_argument('--cleandirs', dest='clean_dirs', action='store_true', default=False)
    return parser.parse_args()


if __name__ == '__main__':

    args = parse_commandline_arguments()
    
    if args.create_db:
        app = create_develop_app()
        create_database(app)
        app = create_test_app()
        create_database(app)

    if args.populate_db:
        populate_database()

    if args.test_server:
        app = create_test_app()
        app.run(threaded=True)

    if args.dev_server:
        app = create_develop_app()
        app.run(threaded=True)

    if args.clean_dirs:
        os.system("rm `find . -type f -name '*.pyc'`")
        os.system("rm `find . -type f -name '.*.swp'`")
