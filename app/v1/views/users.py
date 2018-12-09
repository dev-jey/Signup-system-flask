'''This module manages all user endpoints(signup, login, logout etc)'''
from flask import jsonify, make_response
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from .resources import Initialize
from ..models.user import User
from ..utils.users import Validation


class Signup(Resource, Initialize):
    '''Handles user registration'''
    @staticmethod
    def post():
        '''User signup endpoint'''
        data = Initialize.get_json_data()
        validate = Validation(data)
        validate.check_empty_keys()
        validate.check_empty_values()
        validate.check_number_of_fields()
        validate.check_signup_credentials()
        validate.check_already_exists()
        password = generate_password_hash(
            data["password"], method='sha256').strip()
        user = User(data["username"].strip(),
                    data["email"].lower().strip(), password)
        user.save()
        return make_response(jsonify({"message": "Account created successfully"}), 201)
