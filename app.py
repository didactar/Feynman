from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
db = SQLAlchemy(app)


if __name__ == '__main__':
    app.run()
