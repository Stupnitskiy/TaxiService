from app import base, engine
import app.controller as ctr

try:
    base.metadata.create_all(engine)
    ctr.user_add('user', 'user', False)
    ctr.user_add('admin', 'admin', True)
    ctr.order_add('+380971234567', 'ул. Крещатик, 1')
except:
    print("Oops, i know, app starts a lot of times")
