#!/usr/bin/env python3
import os

import logging
from logging.config import dictConfig

from flask import Flask

from config import LOGGING
from helpers import init_db

dictConfig(LOGGING)
app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

app.logger = logging.getLogger("weather-station")


init_db()
app.logger.info("Init state complete")

import views
