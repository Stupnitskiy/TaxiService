from app import base, engine, session
import app.controller as ctr

try:
    base.metadata.create_all(engine)
    ctr.user_add('user', 'user', False)
    ctr.user_add('admin', 'admin', True)
    ctr.order_add('+380971234567', 'ул. Крещатик, 1')
except:
    session.rollback()
    print("Oops, i know, app starts a lot of times")
