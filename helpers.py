# -*- coding: utf-8 -*-
import datetime
import random
from models import database
from models import TemperatureLocal, TemperatureApi1, PressureLocal, PressureApi1, HumidityLocal, HumidityApi1


def generate_mock_data():
    mock_data = round(random.uniform(0.00, 50.00), 2)
    return mock_data


def generate_mock_date():
    mock_date = datetime.date.today().strftime("%d-%m-%Y")
    return mock_date


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
        for test_data in range(40):
            for i in (TemperatureLocal, TemperatureApi1):
                i.create(date_time=generate_mock_date(),
                         temperature=generate_mock_data(),
                         temperature_min=generate_mock_data(),
                         temperature_max=generate_mock_data())

            for i in (PressureLocal, PressureApi1):
                i.create(date_time=generate_mock_date(),
                         pressure=generate_mock_data(),
                         pressure_min=generate_mock_data(),
                         pressure_max=generate_mock_data())

            for i in (HumidityLocal, HumidityApi1):
                i.create(date_time=generate_mock_date(),
                         humidity=generate_mock_data(),
                         humidity_min=generate_mock_data(),
                         humidity_max=generate_mock_data())
