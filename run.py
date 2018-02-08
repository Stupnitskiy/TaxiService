#!venv/bin/python
from app import app

app.config.from_object('config')
if app.debug:
    import db_startup

app.run(port=8000)
