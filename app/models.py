from app import base
from sqlalchemy import Column, Integer, Unicode, Boolean

class User(base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(Unicode(16), unique=True)
    password = Column(Unicode(24))
    isadmin = Column(Boolean)

    def __init__(self, login, password, isadmin):
        self.login = login
        self.password = password
        self.isadmin = isadmin


class Order(base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(Unicode(13))
    destination = Column(Unicode(200))

    def __init__(self, number, destination):
        self.number = number
        self.destination = destination
