# -*- coding: utf-8 -*-
"""Data models.
"""

import datetime
from peewee import (Model, SqliteDatabase, FloatField, ForeignKeyField, DateTimeField, datetime as peewee_datetime)
from config import DATABASE_NAME

database = SqliteDatabase(DATABASE_NAME)  # Only for development


class _BaseModel(Model):
    class Meta:
        database = database


class TemperatureLocal(_BaseModel):
    """Stores temperature data from local source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    temperature = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()


class PressureLocal(_BaseModel):
    """Stores pressure data from local source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    pressure = FloatField()
    pressure_min = FloatField()
    pressure_max = FloatField()


class HumidityLocal(_BaseModel):
    """Stores humidity data from local source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    humidity = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()


class TemperatureApi1(_BaseModel):
    """Stores temperature data from remote API source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    temperature = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()


class PressureApi1(_BaseModel):
    """Stores pressure data from remote API source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    pressure = FloatField()
    pressure_min = FloatField()
    pressure_max = FloatField()


class HumidityApi1(_BaseModel):
    """Stores humidity data from remote API source"""
    date_time = DateTimeField(formats="%d-%m-%Y")
    humidity = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()


class SummaryTemperature(_BaseModel):
    temperature_local = ForeignKeyField(TemperatureLocal)
    temperature_api1 = ForeignKeyField(TemperatureApi1)


class SummaryPressure(_BaseModel):
    pressure_local = ForeignKeyField(PressureLocal)
    pressure_api1 = ForeignKeyField(PressureApi1)


class SummaryHumidity(_BaseModel):
    humidity_local = ForeignKeyField(HumidityLocal)
    humidity_api1 = ForeignKeyField(HumidityApi1)


def init_db():
    """Tables creation and test data initiation function"""
    with database:
        print("Drop tables...")
        database.drop_tables([TemperatureLocal, TemperatureApi1, PressureLocal,
                              PressureApi1, HumidityLocal, HumidityApi1])
        print("Done...")
        print("Create tables...")
        database.create_tables([TemperatureLocal, TemperatureApi1, PressureLocal,
                              PressureApi1, HumidityLocal, HumidityApi1])
        print("Done")
        print("Adding test data")
        TemperatureLocal.create(date_time="18-05-2020", temperature=25.34, temperature_min=25.56, temperature_max=26.33)
        PressureLocal.create(date_time="18-05-2020", pressure=25.34, pressure_min=25.56, pressure_max=26.33)
        HumidityLocal.create(date_time="18-05-2020", humidity=25.34, humidity_min=25.56, humidity_max=26.33)
        TemperatureApi1.create(date_time="18-05-2020", temperature=25.34, temperature=25.56, temperature=26.33)
        PressureApi1.create(date_time="18-05-2020", pressure=25.34, pressure_min=25.56, pressure_max=26.33)
        HumidityApi1.create(date_time="18-05-2020", humidity=25.34, humidity_min=25.56, humidity_max=26.33)
        print("Done")

