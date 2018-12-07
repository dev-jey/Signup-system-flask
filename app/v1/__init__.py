'''Defines blueprints and routes for the app'''
from flask import Blueprint
from flask_restful import Api, Resource

from .views.users import Signup

BLUE = Blueprint('api', __name__, url_prefix="/api/v1")
API = Api(BLUE)

API.add_resource(Signup, '/auth/signup')
