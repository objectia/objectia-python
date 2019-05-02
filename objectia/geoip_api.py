from objectia.models import GeoLocation


class GeolocationAPI(object):
    """
    Geolocation API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self, ip):
        resp = self.client.get("/usage/".format(ip))
        return GeoLocation(self, resp)
