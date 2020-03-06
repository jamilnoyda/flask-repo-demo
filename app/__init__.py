from flask import Flask
from config import Config
from flask import render_template
from flask import request, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import render_template, flash, redirect, url_for


app = Flask(__name__)

app.config.from_object(Config)


db = SQLAlchemy()
db.init_app(app)

migrate = Migrate()
migrate.init_app(app, db)

from app import routes
from app import models

