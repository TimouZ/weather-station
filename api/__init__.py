import abc

import requests

import config

class _API(abc.ABC):

    @abc.abstractmethod
    def _update_data(self):
        """Updates data in database"""
        pass

    def _send_request(self, url, method, data=None, headers=None):
        """Process request from source API"""
        # TODO: Add logging here
        try:
            response = self._send(method=method, url=url, data=data, headers=headers)
            return response
        except Exception as ex:
            print("An exception was thrown during the request", ex)

    def _send(self, url, method, data=None, headers=None):
        """Sends a request to the data source API"""
        print(url)
        return requests.request(method=method, url=url, headers=headers, data=data, timeout=config.HTTP_TIMEOUT)
