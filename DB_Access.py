import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# Connect with your PostgreSQL
USER = 'postgres'
PASSWORD = 'password'
DB = 'my_database'

Base = declarative_base()
from models import User, Order

Engine = sqlalchemy.create_engine('postgresql://{}:{}@localhost:5432/{}'\
.format(USER, PASSWORD, DB), client_encoding='utf8')

Session = sessionmaker(bind = Engine)

def create_tables():
    # Create the above tables
    Base.metadata.create_all(Engine)

def delete_tables():
    session = Session()

    User.__table__.drop(Engine)
    Order.__table__.drop(Engine)

    session.commit()
    session.close()

def insert_in_users(insertion):
    session = Session()

    new_user = User(insertion[0], insertion[1], insertion[2])
    session.add(new_user)

    session.commit()
    session.close()

def insert_in_orders(insertion):
    session = Session()

    new_order = Order(insertion[0], insertion[1])
    session.add(new_order)

    session.commit()
    session.close()

def find_user(_login, _password):
    session = Session()

    user = session.query(User).filter_by(login=_login, password=_password)\
    .first()

    session.commit()
    session.close()
    return user

def find_orders():
    session = Session()

    result = []
    orders = session.query(Order).all()
    for order in orders:
        result.append([order.id, order.number, order.destination])

    session.commit()
    session.close()
    return result

def isAdmin(request):
    session = Session()

    username = request.cookies.get('username')
    user = session.query(User).filter_by(login=username, isadmin=True)\
    .first()

    session.commit()
    session.close()

    if user is None:
        print('not isAdmin')
        return False
    print('isAdmin')
    return True


#try:
    #delete_tables()
    #create_tables()
    #session = Session()
    #admin = User('admin', 'admin', True)
    #user = User('user', 'user', False)
    #order = Order('+380971234567', 'Come here, dude')
    #session.add(user)
    #session.add(admin)
    #session.add(order)
    #session.commit()
    #insert_in_users(["admin", "admin", True])
    #insert_in_users(["user", "user", False])
    #insert_in_orders(["+380971234567", "ул. Красноармейская, 22"])
#except:
    #print("Oops, i know, app starts a lot of time")
