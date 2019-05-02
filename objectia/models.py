class Entity(object):
    """
    Base class for all models
    """
    def __init__(self, resource, response):
        self.resource = resource
        self.response = response
        try:
            self.content = self.response.json()
        except ValueError:
            self.content = self.response.text

    def __getitem__(self, key):
        return self.content[key]


class Usage(Entity):
    """
    API Usage model
    """
    def __init__(self, resource, response):
        super(Usage, self).__init__(resource, response)
        self.id = None
        if (isinstance(self.content, dict) and "data" in self.content):
            self.geoip_requests = self.content["data"].get("geoip_requests")


class GeoLocation(Entity):
    """
    GeoLocation model
    """
    def __init__(self, resource, response):
        super(Usage, self).__init__(resource, response)
        self.id = None
        if (isinstance(self.content, dict) and "data" in self.content):
            self.country_code = self.content["data"].get("country_code")
            self.country_name = self.content["data"].get("country_name")


class User(Entity):
    """
    User model
    """
    def __init__(self, resource, response):
        super(User, self).__init__(resource, response)
        self.id = None
        if (isinstance(self.content, dict) and "data" in self.content):
            self.id = self.content["data"].get("id")
            self.email = self.content["data"].get("email")
            self.phone = self.content["data"].get("phone")
            self.country_code = self.content["data"].get("country_code", 0)
            self.confirmed = self.content["data"].get("confirmed", False)
            self.registered = self.content["data"].get("registered", False)


class Sms(Entity):
    """
    Sms model
    """
    def __init__(self, resource, response):
        super(Sms, self).__init__(resource, response)

        self.ignored = None
        self.phone = None

        if (isinstance(self.content, dict) and "data" in self.content):
            self.ignored = self.content["data"].get("ignored")
            self.phone = self.content["data"].get("phone")
