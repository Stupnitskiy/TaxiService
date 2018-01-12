from DB_Access import Base
from sqlalchemy import Table, Column, Integer, String, Boolean

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    isadmin = Column(Boolean)

    def __init__(self, login, password, isadmin):
        self.login = login
        self.password = password
        self.isadmin = isadmin


class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    destination = Column(String)

    def __init__(self, number, destination):
        self.number = number
        self.destination = destination
