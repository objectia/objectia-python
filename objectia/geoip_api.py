class GeoLocationAPI(object):
    """
    Geolocation API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self, ip, **kwargs):
        query = self._query(**kwargs)
        return self.client.get("/geoip/{0}{1}".format(ip, query))

    def get_current(self, **kwargs):
        return self.get("myip", **kwargs)

    def get_bulk(self, ip_list, **kwargs):
        ips = ""
        if isinstance(ip_list, list):
            ips = ",".join(ip_list)
        else:
            ips = ip_list
        return self.get(ips, **kwargs)

    def _query(self, **kwargs):
        fields = kwargs.get("fields", "")
        hostname = kwargs.get("hostname", False)
        security = kwargs.get("security", False)
        q = ""
        if fields:
            q = "?fields={0}".format(fields)
        if hostname:
            if q:
                q += "&"
            else:
                q += "?"
            q += "hostname=true"
        if security:
            if q:
                q += "&"
            else:
                q += "?"
            q = "security=true"
        return q
