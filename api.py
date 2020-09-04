#!/usr/bin/env python3
"""
API module
Purpose:
- requests handling
- retrieving sensor data from MongoDB

API specification
http://[hostname]/api/v1/

Requests
GET	http://[hostname]/api/v1/sensor_data	Retrieve data list
GET	http://[hostname]/api/v1/sensor_data/[sensor_data_id]	Retrieve 1 data object
DELETE	http://[hostname]/api/v1/sensor_data/[sensor_data_id]	Delete 1 data object

"""

import json
import bson
import flask
import pymongo


# Initial settings
MONGO_CONNECTION = 'mongodb://localhost:27017'
MONGO_DB = 'mydatabase'
MONGO_COLLECTION = 'mycollection'

myclient = pymongo.MongoClient(MONGO_CONNECTION)
mydb = myclient[MONGO_DB]
mycol = mydb[MONGO_COLLECTION]

app = flask.Flask(__name__)

class JSONEncoder(json.JSONEncoder):
    """
    Custom encoder class for converting Mongo BSON docs to JSON or here (flask.jsonify) will be an error:
    TypeError: Object of type 'ObjectId' is not JSON serializable

    """
    def default(self, o):
        if isinstance(o, bson.ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@app.route('/')
def index():
    return 'This is index page'

@app.route('/api/v1/sensor_data', methods=['GET'])
def get_sensor_data_list():
    sensor_data_list = []
    for x in mycol.find():
        sensor_data_list.append(x)
    return flask.jsonify({'sensor data list:': JSONEncoder().encode(sensor_data_list)})

@app.route('/api/v1/sensor_data/<int:date>', methods=['GET'])
def get_sensor_data_one(date):
    query = 'date : {}'.format(date)
    sensor_data_one = mycol.find(query)
    return jsonify({'record:' get_sensor_data_one })
if __name__ == '__main__':
    app.run(debug=True)
