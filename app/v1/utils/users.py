'''This module contains validations for user data'''
import re
from flask import abort

from ..models.user import User


class Validation():
    '''Contains all validations for user data'''
    def __init__(self, data=None):
        self.data = data
        self.user = User()

    def check_empty_keys(self):
        '''Check is the dictionary keys are given correctly'''
        if not self.data:
            abort(400, "Enter your registration credentials")
        if 'username' not in self.data:
            abort(400, "Username is a required field")
        if 'email' not in self.data:
            abort(400, "Email is a required field")
        if 'password' not in self.data:
            abort(400, "Password is a required field")

    def check_signup_credentials(self):
        '''Validates legitimacy of a person's signup email and password'''
        if not re.match(r"(^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-z]+$)",
                        self.data["email"]):
            abort(400, "Enter a valid email")
        elif len(self.data["password"]) < 6:
            abort(400, "Password must be long than 6 characters")

    def check_number_of_fields(self):
        '''Checks if the number of fields provided is exactly as expected'''
        if len(self.data) > 3:
            abort(400, "Only 3 fields are required")

    def check_empty_values(self):
        '''checks if a user leaves any field empty'''
        if self.data['username'] == "":
            abort(400, "Enter a username")
        if self.data['email'] == "":
            abort(400, "Enter an email")
        if self.data['password'] == "":
            abort(400, "Enter a password")

    def check_already_exists(self):
        '''Checks if a user is already registered or not'''
        users = self.user.get()
        for user in users:
            if user["username"].lower().strip() == self.data['username'].lower().strip():
                abort(406, "Username already taken")

            elif user["email"].lower().strip() == self.data['email'].lower().strip():
                abort(406, "Email already taken")
