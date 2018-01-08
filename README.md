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
