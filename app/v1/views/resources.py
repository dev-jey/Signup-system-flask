'''This module is designed to store methods for other 
views, and ensure code is DRY'''
from flask import jsonify, request

from ..models.user import User


class Initialize():
    '''This class contains helper methods for the views modules'''

    def __init__(self):
        self.user = User()
        self.login_first = jsonify({"message": "login to continue"})

    @staticmethod
    def get_json_data():
        '''Gets json data from user'''
        return request.get_json()
