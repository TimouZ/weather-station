"""
Parameters
id	required	City ID. List of city ID 'city.list.json.gz' can be downloaded here.
appid	required	Your unique API key (you can always find it on your account page under the "API key" tab)
mode	optional	Response format. Possible values are xml and html. If you don't use the mode parameter
                    format is JSON by default.
units	optional	Units of measurement. standard, metric and imperial units are available. If you do not use
                    the units parameter, standard units will be applied by default.
lang	optional	You can use this parameter to get the output in your language.
"""
import abc

import requests

import config

class _API(abc.ABC):
    # TODO: Move this class to package
    def update_data(self):
        # TODO: Add logging here

    @abc.abstractmethod
    def _update_data(self):
        pass

class API(_API):
    def _update_data(self):
        pass

    def _get_openweathermap_data(self):
    request_url = config.DevelopmentConfig.OPENWEATHERMAP_REQUEST_URL
    request_query = request_url.format(
                    city_id=config.DevelopmentConfig.CITY_ID,
                    api_key=config.DevelopmentConfig.API_KEY
                    )
    method = "get" # If you don't use the mode parameter format is JSON by default.

    def make_request():
        print(request_query)
        return requests.request(method, request_query)

