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
import requests

import config
from api import _API


class API(_API):
    def _update_data(self):
        pass

    def get_openweathermap_api_data(self):
        openweathermap_request_url_pattern = config.DevelopmentConfig.OPENWEATHERMAP_REQUEST_URL_PATTERN
        openweathermap_request_url = openweathermap_request_url_pattern.format(
                    city_id=config.DevelopmentConfig.CITY_ID,
                    api_key=config.DevelopmentConfig.API_KEY
                    )
        method = "get"  # If you don't use the mode parameter format is JSON by default.
        self._send_request(openweathermap_request_url, method)
