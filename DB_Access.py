import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, ForeignKey

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
        Column('password', String)
    )

    # Create the above tables
    meta.create_all(con)
    con.close()
    del meta

def delete_tables():
    con = connect(USER, PASSWORD, DB)
    con.execute("drop table users")
    con.execute("drop table orders")

def insert_in_users(insertion):
    con = connect(USER, PASSWORD, DB)

    con.execute("insert into users(login, password) values (%s, %s)" % \
    (insertion[0], insertion[1]))

    con.close()

def insert_in_orders(insertion):
    con = connect(USER, PASSWORD, DB)

    con.execute("insert into orders(number, destination) values (%s, %s)" % \
    (insertion[0], insertion[1]))

    con.close()

def select_all(table):
    con = connect(USER, PASSWORD, DB)

    result = con.execute("select * from %s" % table)
    for row in result:
        print(row)

    con.close()

delete_tables()
create_tables()
insert_in_users(["'Dimitry'", "'456'"])
insert_in_orders(["'097-8888888'", "'ул. Красноармейская, 22'"])
select_all('orders')
select_all('users')
