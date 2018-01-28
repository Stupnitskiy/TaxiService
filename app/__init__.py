from flask import Flask
from flask_redis import FlaskRedis
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
redis_store = FlaskRedis(app)

from config_database import USER, PASSWORD, DB
Base = declarative_base()

Engine = sqlalchemy.create_engine('postgresql://{}:{}@localhost:5432/{}'\
.format(USER, PASSWORD, DB), client_encoding='utf8')

Session = sessionmaker(bind = Engine, autocommit = True)
session = Session()

from app import views, models
