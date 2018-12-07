import unittest
import json
from app import create_app

from app.v1.models.migrate import Db


class TestsForApi(unittest.TestCase):
    '''Set up method to create an attendant, admin, product,
    and a sales table for use in other tests and authentication'''

    def setUp(self):
        self.db = Db()
        self.db.createConnection()
        self.db.createTables()
        self.app = create_app(config_name="testing")
        self.test_client = self.app.test_client()
    
    def tearDown(self):
        '''Method to clear all tables
        before another test is undertaken'''
        self.db.destroy_tables()
        self.db.closeConnection()