from DB_Access import Base
from sqlalchemy import Table, Column, Integer, String, Boolean

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    login = Column(String, unique=True)
    password = Column(String)
    isadmin = Column(Boolean)

    def __repr__(self):
        return "<User(login='%s', isAdmin='%s')>" % (self.login, self.isadmin)

    def __init__(self, login, password, isadmin):
        self.login = login
        self.password = password
        self.isadmin = isadmin

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    number = Column(String)
    destination = Column(String)

    def __repr__(self):
        return "<Order(number='%s', destination='%s')>" % \
        (self.number, self.destination)

    def __init__(self, number, destination):
        self.number = number
        self.destination = destination
