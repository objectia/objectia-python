from objectia.rest import RestClient
from objectia.usage_api import UsageAPI
from objectia.geoip_api import GeoLocationAPI

API_BASE_URL = "https://api.objectia.com/rest/v1"
DEFAULT_TIMEOUT = 30  # seconds


class Client(object):
    """
    Client for sending requests to Objectia API server
    """
    def __init__(self, **kwargs):
        # Process arguments
        self.api_key = kwargs.get("api_key", None)
        if not self.api_key:
            raise ValueError("No API key provided")
        self.api_base_url = kwargs.get("api_base_url", API_BASE_URL)
        self.timeout = kwargs.get("timeout", DEFAULT_TIMEOUT)

        # Create the REST client
        self.client = RestClient(self.api_key, self.api_base_url, self.timeout)

        # Attach the APIs
        self._usage_api = UsageAPI(self)
        self._geoip_api = GeoLocationAPI(self)

    @property
    def usage(self):
        """
        Usage API
        """
        return self._usage_api

    @property
    def geoip(self):
        """
        GeoLocation API
        """
        return self._geoip_api
