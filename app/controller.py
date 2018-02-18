from app import session
from app.models import User, Order


def order_add(number, adress):

    new_order = Order(number, adress)
    session.add(new_order)
    session.commit()
    return new_order


def user_add(username, password, is_admin):

    new_user = User(username, password, is_admin)
    session.add(new_user)
    session.commit()
    return new_user


def get_orders():

    orders = session.query(Order).all()
    return orders


def get_user(username, passw):

    return session.query(User).filter(
        User.login == username, User.password == passw
    ).one_or_none()


def is_admin(username):

    return session.query(User).filter(
        User.login == username, User.isadmin == True
    ).one_or_none()
