from flask import Flask
from flask_redis import FlaskRedis
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

app = Flask(__name__)
redis_store = FlaskRedis(app)
app.secret_key = os.urandom(24)

base = declarative_base()

from config import DB_URI
engine = create_engine(DB_URI, client_encoding='utf8')

Session = sessionmaker(bind = engine)
session = Session()

from app import views, models
