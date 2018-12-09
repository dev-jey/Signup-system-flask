'''This module is responsible for all database connections and tables'''
from sys import modules
import os
import psycopg2


class Db():
    '''Handles all database functions'''
    def __init__(self):
        self.conn = None

    def create_connection(self):
        '''Creates connection for the app to database'''
        try:
            if 'pytest' in modules:
                url = os.getenv("TEST_DB")
            if os.getenv("APP_SETTINGS") == "development":
                url = os.getenv("DEV_DB")
            self.conn = psycopg2.connect(database=url)
        except Exception:
            try:
                if os.getenv("APP_SETTINGS") == "production":
                    self.conn = psycopg2.connect(os.environ['DATABASE_URL'],
                                                 sslmode='require')
            except Exception:
                return "Connection Failed"
        self.conn.autocommit = True
        return self.conn

    def close_connection(self):
        '''method to close connections'''
        return self.conn.close()

    def create_tables(self):
        '''Creates all tables in the database'''
        cursor = self.create_connection().cursor()
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
        '''Destroys all tables after each test'''
        cursor = self.create_connection().cursor()
        cursor.execute(
            "SELECT table_schema,table_name FROM information_schema.tables "
            " WHERE table_schema = 'public' ORDER BY table_schema,table_name"
        )
        rows = cursor.fetchall()
        for row in rows:
            cursor.execute("drop table "+row[1] + " cascade")
        self.conn.commit()
        self.conn.close()
