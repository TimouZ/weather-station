#!/usr/bin/env python3
"""
Main module
Purpose:
- saving sensor data
"""

import datetime
import time
import pymongo
import sensor


# Initial settings
MONGO_CONNECTION = 'mongodb://localhost:27017'
MONGO_DB = 'mydatabase'
MONGO_COLLECTION = 'mycollection'
SENSOR_TIME = 5

myclient = pymongo.MongoClient(MONGO_CONNECTION)
mydb = myclient[MONGO_DB]
mycol = mydb[MONGO_COLLECTION]

sens = sensor.Sensor(1, 10)
now = datetime.datetime.now()


while True:
    sens_data = {'date': now.strftime("%d/%m/%y %H:%M:%S"),
                 'sensor data': sens.get_data(),
                 'type': 'temp',
                 'ID': 'DHT11',
                 'location': 'HTP11'}
    sens_data_id = mycol.insert_one(sens_data)
    print('Record {} inserted succesfull'.format(sens_data_id))
    time.sleep(5)
