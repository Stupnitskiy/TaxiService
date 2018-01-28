#!venv/bin/python
from app import app, Base, Engine, session
from app.models import User, Order

try:
    Base.metadata.create_all(Engine)
    user = User('user', 'user', False)
    admin = User('admin', 'admin', True)
    order = Order('+380971234567', 'Come here, dude')
    session.add(user)
    session.add(admin)
    session.add(order)
except:
    print("Oops, i know, app starts a lot of time")

app.config['DEBUG'] = True
app.run(port=8000)
