import os


class Config(object):
    '''Class to create default configurations'''
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")


class Development(Config):
    '''Class to set development mode configurations'''
    DEBUG = True


class Testing(Config):
    '''Class to set Testing mode configurations'''
    DEBUG = False

app_config = {
    "development": Development,
    "testing": Testing
}
