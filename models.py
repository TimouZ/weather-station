# -*- coding: utf-8 -*-
"""Data models.
"""

from peewee import (Model, SqliteDatabase, FloatField, DateTimeField)
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
