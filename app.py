from flask import Flask, request, json
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from werkzeug.security import generate_password_hash, check_password_hash
import os

from config import config_options


db = SQLAlchemy()
bcrypt = Bcrypt()
jwt = JWTManager()


def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
