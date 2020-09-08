#!/usr/bin/env python3
import os
import flask

app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

