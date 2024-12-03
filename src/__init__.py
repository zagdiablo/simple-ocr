from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def App():
    app = Flask(__name__, static_folder="./static", template_folder="./templates")
    return app
