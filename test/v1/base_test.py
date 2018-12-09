import unittest
import json
from app import create_app

from app.v1.models.migrate import Db


class TestsForApi(unittest.TestCase):
    '''Set up method to create an attendant, admin, product,
    and a sales table for use in other tests and authentication'''

    def setUp(self):
        self.database_obj = Db()
        self.database_obj.create_connection()
        self.database_obj.create_tables()
        self.app = create_app(config_name="testing")
        self.test_client = self.app.test_client()
        self.context = self.app.app_context()
        self.context.push()

        self.header = {'content-type': 'application/json'}
    
    def tearDown(self):
        '''Method to clear all tables
        before another test is undertaken'''
        self.database_obj.destroy_tables()
        self.database_obj.close_connection()
        self.context.pop()