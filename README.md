

This is a GIT repository for taxi service.
Technologies:
	- Flask
	- Python 3.6
	- PostgreSQL
	- Redis

Application was developed using virtual environment and should be launched with it. For work you need to create PostgreSQL user and database (or use existing one), and install Redis server ([Redis quickstart](https://redis.io/topics/quickstart)).


### Confiure new virtual environment:
Type it to create venv, that works with Python 3.6:
```
$ cd ~/path/to/app_root
~/path/to/app_root$ virtualenv -p python3.6 venv
```

Then you need to activate venv and install into some libraries, enumerated in req.txt:
```
~/path/to/app_root$ . venv/bin/activate
(venv)...~/path/to/app_root$ pip install -r req.txt
```


### Type your user and db in DB_Access file:
```python
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Boolean

# Connect with your PostgreSQL
USER = 'postgres'
PASSWORD = 'password'
DB = 'my_database'
```

### Install/Run Redis server:
```
$ sudo apt install -y redis-server
$ redis-server
```

### Start application:
```
(venv)...~/path/to/app_root$ python app.py
```
