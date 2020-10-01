# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""Module provides receiving and processing data from a remote source"""

import datetime
import abc
import requests

import config
import logging.config
from config import logging, HTTP_TIMEOUT
import models

logging.config.dictConfig(config.LOGGING)


class _API(abc.ABC):
    """Abstract base class for all APIs"""

    # TODO: move to package __init__
    def __init__(self, logger_name):
        self.log = logging.getLogger("api")
        self.log.name = logger_name

    @abc.abstractmethod
    def get_api_data(self):
        pass

    @abc.abstractmethod
    def _parse_api_data(self, response_data):
        pass

    @abc.abstractmethod
    def _update_data(self):
        pass

    def _send_request(self, url, method, data=None, headers=None):
        """Sends request to the specified url

        Args:
            url (str): url to which the request will be made
            method (str): HTTP method type
            data:
            headers:

        Returns:
            response object
        """
        log = models.ApiLog(reqest_url=url, request_data=data, request_method=method,
                            request_headers=headers)
        # TODO: add logging to databse
        try:
            response = self._send(method=method, url=url, data=data, headers=headers)
            return response
        except Exception as ex:
            print("An exception was thrown during the request", ex)

    def _send(self, url, method, data=None, headers=None):
        """Sends request to the specified url

        Args:
            url (str): url to which the request will be made
            method (str): HTTP method type
            data:
            headers:

        Returns:
            response object
        """
        return requests.request(method=method, url=url, headers=headers, data=data, timeout=config.HTTP_TIMEOUT)


class API(_API):
    def __init__(self):
        super().__init__("Api")

    def get_api_data(self):
        """Forms a request and returns data (json) from openweathermap.com

        openweathermap.com API parameters:
            id	(required):	City ID. List of city ID 'city.list.json.gz' can be downloaded here.
            appid	(required):	Your unique API key (you can always find it on your account page under the "API key" tab)
            mode	(optional):	Response format. Possible values are xml and html. If you don't use the mode parameter
                                format is JSON by default.
            units	(optional):	Units of measurement. standard, metric and imperial units are available. If you do not use
                                the units parameter, standard units will be applied by default.
            lang	(optional):	You can use this parameter to get the output in your language.

        Returns:
            full response from openweathermap.org
        """
        openweathermap_request_url_pattern = config.DevelopmentConfig.OPENWEATHERMAP_REQUEST_URL_PATTERN
        openweathermap_request_url = openweathermap_request_url_pattern.format(
            city_id=config.DevelopmentConfig.CITY_ID,
            api_key=config.DevelopmentConfig.API_KEY
        )
        method = "get"  # If you don't use the mode parameter format is JSON by default.
        openweathermap_api_data = self._send_request(openweathermap_request_url, method)
        openweathermap_api_data_json = openweathermap_api_data.json()
        return openweathermap_api_data_json

    def _parse_api_data(self, response_data):
        """Process raw data from openweathermap.org

        Args:
            response_data (json): json object

        Returns:
            dict {"feels_like": 9.19, "humidity": 93, "pressure": 1007, "temp": 12.85, "temp_max": 13,
            "temp_min": 12.78}
        """
        data = {}
        for d in response_data.items():
            if d[0] == "main":
                data = d[1]
        return data

    def update_db_data(self):
        try:
            self._update_data()
        except Exception as e:
            print("Can`t update data", e)

    def _update_data(self):
        """Updates data in database

        Args:
            No args

        Returns:
            Updates data in DB
        """

        # TODO: add check for the existence of a current date record

        weather_data_dict = self._parse_api_data(self.get_api_data())

        temperature = models.TemperatureApi1(
            date_time=datetime.date.today().strftime("%d-%m-%Y"),
            temperature=weather_data_dict.get("temp", 0.0),
            temperature_min=weather_data_dict.get("temp_min", 0.0),
            temperature_max=weather_data_dict.get("temp_max", 0.0),
        )
        temperature.save()

        humidity = models.HumidityApi1(humidity=weather_data_dict.get("humidity", 0.0))
        humidity.save()

        pressure = models.PressureApi1(pressure=weather_data_dict.get("pressure", 0.0))
        pressure.save()


if __name__ == "__main__":
    API().get_api_data()
