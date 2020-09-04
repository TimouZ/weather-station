import datetime
from peewee import (Model, SqliteDatabase, DateField, FloatField, ForeignKeyField, datetime as peewee_datetime)

database_name = 'weather_station.db'


database = SqliteDatabase(database_name)  # Only for development


class BaseModel(Model):
    class Meta:
        database = database


class TemperatureLocal(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    temperature = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()


class PressureLocal(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    pressure = FloatField()
    pressure_min = FloatField()
    pressure_max = FloatField()


class HumidityLocal(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    humidity = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()


class TemperatureApi1(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    temperature = FloatField()
    temperature_min = FloatField()
    temperature_max = FloatField()


class PressureApi1(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    pressure = FloatField()
    pressure_min = FloatField()
    pressure_max = FloatField()


class HumidityApi1(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    humidity = FloatField()
    humidity_min = FloatField()
    humidity_max = FloatField()

    def to_dict(self):
        return self._data


class WeatherStation(BaseModel):
    date = DateField(formats="%d-%m-%Y")
    temperature_local = ForeignKeyField(TemperatureLocal)
    temperature_api1 = ForeignKeyField(TemperatureApi1)
    pressure_local = ForeignKeyField(PressureLocal)
    pressure_api1 = ForeignKeyField(PressureApi1)
    humidity_local = ForeignKeyField(HumidityLocal)
    humidity_api1 = ForeignKeyField(HumidityApi1)


def init_db():
    with database:
        database.drop_tables([TemperatureLocal, TemperatureApi1, PressureLocal,
                              PressureApi1, HumidityLocal, HumidityApi1, WeatherStation])
        database.create_tables([TemperatureLocal, TemperatureApi1, PressureLocal,
                                PressureApi1, HumidityLocal, HumidityApi1, WeatherStation])
