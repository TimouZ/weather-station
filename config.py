# -*- coding: utf-8 -*-
"""Config file for app to deal with the different environments.

Django like setup approach
Here is a base class that the other config classes inherit from
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_NAME = 'weather_station.db'


class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = "SecretKey"

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True



