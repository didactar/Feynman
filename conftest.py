import pytest
from database import db
from factory import create_app


@pytest.fixture(scope='session')
def app():
    _app = create_app()
    with _app.app_context():
        yield _app
 

@pytest.yield_fixture(scope='function')
def session(app):
    db.create_all()
    yield
    db.drop_all()


URL_PREFIX = 'http://localhost:5000/api/v1/'
