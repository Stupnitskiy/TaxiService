|   Project status|  |
| ------------- |:-------------|
| Build status  | [![Build Status](https://travis-ci.org/Stupnitskiy/TaxiService.svg?branch=master)](https://travis-ci.org/Stupnitskiy/TaxiService) |
| Project Certification     |[![Codacy Badge](https://api.codacy.com/project/badge/Grade/96ca3fb17fe64e7186207069ef76c04d)](https://www.codacy.com/app/Stupnitskiy/TaxiService?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=Stupnitskiy/TaxiService&amp;utm_campaign=Badge_Grade)    |
| Code coverage | [![codecov](https://codecov.io/gh/Stupnitskiy/TaxiService/branch/master/graph/badge.svg)](https://codecov.io/gh/Stupnitskiy/TaxiService)      |



This is a GIT repository for taxi service.
Technologies:
	- Flask
	- Python 3.6
	- PostgreSQL
	- Redis

Application was developed using virtual environment and should be launched with it. For work you need to create PostgreSQL user and database (or use existing one), and install Redis server ([Redis quickstart](https://redis.io/topics/quickstart)).

### Type your user and db in DB_Access file:


```python
import sqlalchemy
from sqlalchemy import Table, Column, Integer, String, Boolean

# Connect with your PostgreSQL
USER = 'postgres'
PASSWORD = 'password'
DB = 'my_database'
```

### Run Redis server:

```
$ redis-server
```

### Start virtual environment:

```
$ cd ~/path/to/app_root
$ . venv/bin/activate
$ python app.py
```
