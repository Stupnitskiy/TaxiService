from app import session
from app.models import User, Order

def safe_session(function):

    def wrapped(*args, **kwargs):
        temp_session = session()
        result = function(temp_session, *args, **kwargs)
        temp_session.commit()
        temp_session.close()
        return result
    return wrapped


@safe_session
def order_add(session, number, adress):

    new_order = Order(number, adress)
    session.add(new_order)


@safe_session
def user_add(session, username, password, is_admin):

    new_user = User(username, password, is_admin)
    session.add(new_user)


@safe_session
def get_orders(session):

    orders = session.query(Order).all()
    list_of_orders = []
    for order in orders:
        list_of_orders.append([order.id, order.number, order.destination])

    return list_of_orders


@safe_session
def get_user(session, log, passw):

    return session.query(User).filter_by(login = log, password = passw).first()


@safe_session
def is_admin(session, username):

    return session.query(User).filter_by(login=username, isadmin=True).first()
