'''This module initializes a database connection
for other modules'''

import datetime
import psycopg2.extras

from .migrate import Db


class Connect():
    '''Initializes connection to the db'''

    def __init__(self):
        self.database_obj = Db()
        self.conn = self.database_obj.create_connection()
        self.database_obj.create_tables()
        self.cursor = self.conn.cursor(
            cursor_factory=psycopg2.extras.RealDictCursor)
        self.date = datetime.datetime.now()
