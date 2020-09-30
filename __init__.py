# -*- coding: utf-8 -*-

import abc
import importlib
import logging

import requests
import traceback


from config import logging, LOGGING, HTTP_TIMEOUT
import models

logging.config.dictConfig(LOGGING)

class _API(abc.ABC):
    def __init__(self, logger_name):
        self.log = logging.getLogger("api")
        self.log.name = logger_name

    @abc.abstractmethod
    def _update_data(self):
        """Updates data in database"""
        pass

    def _send_request(self, url, method, data=None, headers=None):
        """Process request from source API"""
        log = models.ApiLog(reqest_url=url, request_data=data, request_method=method,
                            request_headers=headers)
        try:
            response = self._send(method=method, url=url, data=data, headers=headers)
            return response
        except Exception as ex:
            print("An exception was thrown during the request", ex)

    def _send(self, url, method, data=None, headers=None):
        """Sends a request to the data source API"""
        print(url)
        return requests.request(method=method, url=url, headers=headers, data=data, timeout=config.HTTP_TIMEOUT)

print("----------------api __init__ initialised-------------------")