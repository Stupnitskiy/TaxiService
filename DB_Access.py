import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Boolean

# Connect with your PostgreSQL
USER = 'postgres'
PASSWORD = 'password'
DB = 'my_database'

def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    engine = sqlalchemy.create_engine(url, client_encoding='utf8')

    con = engine.connect()
    #con = sqlalchemy.create_engine(url, client_encoding='utf8')

    return con

def create_tables():
    con = connect(USER, PASSWORD, DB)
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    orders = Table('orders', meta,
        Column('id', Integer, primary_key=True),
        Column('number', String),
        Column('destination', String)
    )

    users = Table('users', meta,
        Column('id', Integer, primary_key=True),
        Column('login', String),
        Column('password', String),
        Column('isadmin', Boolean)
    )

    # Create the above tables
    meta.create_all(con)
    con.close()
    del meta

def delete_tables():
    con = connect(USER, PASSWORD, DB)
    con.execute("drop table users")
    con.execute("drop table orders")
    con.close()

def insert_in_users(insertion):
    con = connect(USER, PASSWORD, DB)

    con.execute("insert into users(login, password, isadmin) values ('%s', '%s', %s)" % (insertion[0], insertion[1], insertion[2]))

    con.close()

def insert_in_orders(insertion):
    con = connect(USER, PASSWORD, DB)

    con.execute("insert into orders(number, destination) values ('%s', '%s')" \
    % (insertion[0], insertion[1]))

    con.close()

def find_user(login, password):
    con = connect(USER, PASSWORD, DB)

    return con.execute("select * from users where (login='%s') and \
    (password='%s')" % (login, password)).fetchall()

    con.close()

def find_orders():
    con = connect(USER, PASSWORD, DB)

    return con.execute("select * from orders").fetchall()

    con.close()

def isAdmin(request):
    con = connect(USER, PASSWORD, DB)

    username = request.cookies.get('username')
    result = con.execute("select * from users where (login='%s') and \
    (isadmin='t')" % (username)).fetchone()

    con.close()

    if result:
        print('isAdmin')
        return True
    print('not isAdmin')
    return False

try:
    #delete_tables()
    create_tables()
    insert_in_users(["admin", "admin", True])
    insert_in_users(["user", "user", False])
    insert_in_orders(["+380971234567", "ул. Красноармейская, 22"])
except:
    print("Oops, i know, app starts a lot of time")
