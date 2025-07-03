#for initializing project

from flask import Flask
from backend.models import db


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///household__app_db.sqlite3"
    db.init_app(app)
    return app

app = create_app()

from backend.routes import *

#the server is running only if we want to run app.py file 
if __name__ =="__main__":
    app.run(debug=True)