#!/usr/bin/env python3
import os
from flask import Flask
from helpers import init_db

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

init_db()
print("Init state complete")

import views
