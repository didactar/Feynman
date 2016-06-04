import pytest
from database import db
from config import TestConfig
from factory import create_app


@pytest.yield_fixture(scope='session')
def app():
    config_object = TestConfig()
    app = create_app(config_object)
    ctx = app.app_context()
    ctx.push()
    db.app = app
    db.drop_all()
    yield
    ctx.pop()


@pytest.yield_fixture(scope='function')
def session(app):
    db.create_all()
    yield
    db.drop_all()
