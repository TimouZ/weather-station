# -*- coding: utf-8 -*-
"""Config file for app
Sections:
Env config - django like setup approach
Log config - configuration for logger
"""

import os
import logging

basedir = os.path.abspath(os.path.dirname(__file__))
DATABASE_NAME = 'weather_station.db'

"""Env config"""
class Config:
    """Here is a base class that the other config classes inherit from"""
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


"""Log config"""
LOGGING = {
    "version": 1,
    "formatters": {
        "default": {
            "format": "[%(asctime)s] [%(levelname)s] - %(name)s: %(message)s",
        },
    },

    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "class": "logging.FileHandler",
            "formatter": "default",
            "filename": "new.log",
        },
    },
    "loggers": {
        "weather-station": {
            "handlers": ["file", "console"],
            "level": logging.DEBUG
        },
        "mock": {
            "handlers": ["file", "console"],
            "level": logging.DEBUG
        },
    },
}
