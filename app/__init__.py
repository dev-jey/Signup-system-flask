'''This module creates the app using a function, 
and determines the configuration settings to use'''
from flask import Flask, Blueprint, make_response, jsonify
from flask_cors import CORS

from instance.config import app_config
from .v1 import BLUE as version1


def create_app(config_name):
    '''Main function to create the flask app and
    set configurations'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')
    app.register_blueprint(version1)
    CORS(app, resources={r"/api/*": {"origins": "*"}})

    @app.errorhandler(404)
    def not_found(e):
        '''Defining a custom message for not found'''
        return make_response(jsonify({
            "message": "Oops! wrong url"
        }), 404)

    @app.errorhandler(500)
    def server_error(e):
        return make_response(jsonify({
            "message": "An internal error occured"
        }), 500)

    return app
