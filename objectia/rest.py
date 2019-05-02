import requests
import logging
import json

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

from objectia.errors import APIConnectionError, APITimeoutError, ResponseError
from objectia.version import VERSION

USER_AGENT = "objectia-python/{0}".format(VERSION)


class RestClient:
    def __init__(self, api_key=None, api_base_url=None, timeout=None):
        """
        @param kwargs: Optional parameters
        """
        self.api_key = api_key
        self.api_base_url = api_base_url
        self.timeout = timeout

    def get(self, path):
        """
        Execute a HTTP GET
        """
        return self.execute("GET", path)

    def post(self, path, data):
        """
        Execute a HTTP POST
        """
        return self.execute("POST", path, data)

    def patch(self, path, data):
        """
        Execute a HTTP PATCH
        """
        return self.execute("PATCH", path, data)

    def put(self, path, data):
        """
        Execute a HTTP PUT
        """
        return self.execute("PUT", path, data)

    def delete(self, path):
        """
        Execute a HTTP DELETE
        """
        return self.execute("DELETE", path)

    def execute(self, method, path, data={}):
        """
        Execute a HTTP request
        """
        logging.debug("Sending HTTP request")

        url = self.api_base_url + quote(path)

        headers = {
            "Authorization": "Bearer {0}".format(self.api_key),
            "Accept": "application/json",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT
        }

        try:
            params = {}
            payload = None
            if method == "GET":
                params.update(data)
            elif method in ["POST", "PUT", "PATCH"]:
                payload = json.dumps(data)
            resp = requests.request(method, url, headers=headers, params=params, data=payload, timeout=self.timeout)
        except requests.exceptions.Timeout as e:
            raise APITimeoutError("Request timed out: " + repr(e))
        except requests.exceptions.RequestException as e:
            raise APIConnectionError("Unable to connect to server: " + repr(e))

        if resp.status_code not in [200, 201]:
            try:
                content = resp.json()
                message = content["message"]
            except (KeyError, ValueError):
                # Not JSON response, or message set
                if resp.status_code == 501:
                    message = "Not implemented"
                elif resp.status_code == 502:
                    message = "Bad gateway"
                elif resp.status_code == 503:
                    message = "Service unavailable"
                elif resp.status_code == 504:
                    message = "Gateway timeout"
                else:
                    message = "Internal server error"
            raise ResponseError(resp.status_code, message)
        return resp
