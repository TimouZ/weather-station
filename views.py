# -*- coding: utf-8 -*-

from flask import render_template, url_for, redirect
from weather_station import app
import controllers


@app.route('/')
@app.route("/index")
def index():
    data = controllers.GetAllTemperatureData().call()
    return render_template("index.html", context=data)


@app.route("/local_temperature")
def show_local_temperature_data():
    data = controllers.GetLocalTemperatureData().call()
    return render_template("local_temperature.html", context=data)


@app.route("/remote_temperature")
def show_remote_temperature_data():
    data = controllers.GetRemoteAPITemperatureData().call()
    return render_template("remote_temperature.html", context=data)


@app.route("/update_latest")
def update_latest():
    controllers.UpdateLatest().call()
    return redirect(url_for('show_remote_temperature_data'))





@app.route("/test_data")
def test_data():
    data = controllers.GetRemoteAPITemperatureData().call()
    return data
