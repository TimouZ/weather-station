from flask import render_template
from weather_station import app
from controllers import get_all_temperature_data, get_local_temperature_data, get_remote_api_temperature_data


@app.route('/')
@app.route("/index")
def index():
    query_data = get_all_temperature_data()
    return render_template("index.html", query_data=query_data)


@app.route("/local_temperature")
def show_local_temperature_data():
    query_data = get_local_temperature_data()
    return render_template("local_temperature.html", query_data=query_data)


@app.route("/remote_temperature")
def show_remote_temperature_data():
    query_data = get_remote_api_temperature_data()
    return render_template("remote_temperature.html", query_data=query_data)

