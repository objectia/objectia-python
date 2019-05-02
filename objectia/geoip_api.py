class GeoLocationAPI(object):
    """
    Geolocation API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self, ip):
        return self.client.get("/geoip/{0}".format(ip))

    def get_current(self):
        return self.client.get("/geoip/myip")

    def get_bulk(self, ip_list):
        return self.client.get("/geoip/{0}".format(ip_list))
