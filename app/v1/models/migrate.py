import psycopg2
import os
from sys import modules


class Db(object):
    def __init__(self):
        self.conn = None

    def createConnection(self):
        try:
            if 'pytest' in modules:
                URL = os.getenv("TEST_DB")
            if os.getenv("APP_SETTINGS") == "development":
                URL = os.getenv("DEV_DB")
            self.conn = psycopg2.connect(database=URL)
        except Exception:
            try:
                if os.getenv("APP_SETTINGS") == "production":
                    self.conn = psycopg2.connect(os.environ['DATABASE_URL'],
                                                 sslmode='require')
            except Exception:
                return "Connection Failed"
        self.conn.autocommit = True
        return self.conn

    def closeConnection(self):
        '''method to close connections'''
        return self.conn.close()

    def createTables(self):
        cursor = self.createConnection().cursor()
        tables = [
            """CREATE TABLE IF NOT EXISTS users(
                id serial PRIMARY KEY,
                username varchar(255) UNIQUE NOT NULL,
                email varchar(255) UNIQUE NOT NULL,
                password varchar(255) NOT NULL
                )
            """]
        for table in tables:
            cursor.execute(table)
        self.conn.commit()
        self.conn.close()

    def destroy_tables(self):
        cursor = self.createConnection().cursor()
        cursor.execute(
            "SELECT table_schema,table_name FROM information_schema.tables "
            " WHERE table_schema = 'public' ORDER BY table_schema,table_name"
        )
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute("drop table "+row[1] + " cascade")
        self.conn.commit()
        self.conn.close()