from app import redis_store
from flask import session, render_template
import app.controller as ctr

def is_logged():

    username = session.get('username')
    if username and redis_store.get(username):
        return True
    return False


def is_admin():

    username = session.get('username')
    user = ctr.is_admin(username)

    if user is None:
        return False
    return True


def render_admin_page():

    if is_admin():
        return render_template('admin.html', orders=ctr.get_orders())
    return render_template('admin.html')
