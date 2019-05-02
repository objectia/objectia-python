from objectia.models import GeoLocation


class GeoLocationAPI(object):
    """
    Geolocation API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self, ip):
        resp = self.client.get("/geoip/{0}".format(ip))
        return GeoLocation(self, resp)

    def getCurrent(self, ip):
        resp = self.client.get("/geoip/myip")
        return GeoLocation(self, resp)

    def getBulk(self, ip_list):
        resp = self.client.get("/geoip/{0}".format(ip_list))
        return GeoLocation(self, resp)
