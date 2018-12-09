'''This module interacts with the database to 
perform CRUD operations on user data'''
from .main import Connect


class User(Connect):
    '''Handles all user data manipulation'''

    def __init__(self, username=None, email=None, password=None):
        '''Initializes a new user'''
        Connect.__init__(self)
        self.username = username
        self.email = email
        self.password = password

    def save(self):
        '''Saves/registers a user to the database'''
        self.cursor.execute("INSERT INTO users(username, email, password) VALUES(%s,%s,%s)",
                            (self.username, self.email, self.password,))

    def get(self):
        '''Gets all users from database'''
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
