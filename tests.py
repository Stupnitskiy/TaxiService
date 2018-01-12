
import unittest

from app import app
import sqlalchemy
from models import User, Order
from DB_Access import *

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['CSRF_ENABLED'] = False
        self.app = app.test_client()

        DB = 'my_test_database'
        Engine = sqlalchemy.create_engine('postgresql://{}:{}@localhost:5432/{}'\
        .format(USER, PASSWORD, DB), client_encoding='utf8')

        Session = sessionmaker(bind = Engine)
        create_tables();

    def tearDown(self):
        delete_tables();

    def login(self, login, password):
        return self.app.post(
            '/login',
            data=dict(login=login, password=password),
            follow_redirects=True
        )

    def logout(self):
        return self.app.get(
            '/logout',
            follow_redirects=True
        )

    def test_insert_and_find_order(self):
        insert_in_orders(['+380971234567', 'Any street'])
        order = find_orders()
        assert order[0][1] == '+380971234567'

    def test_insert_and_find_user(self):
        insert_in_users(['admin', 'admins', True])
        user = find_user('admin', 'admin')
        assert user is None


if __name__ == '__main__':
    unittest.main()
