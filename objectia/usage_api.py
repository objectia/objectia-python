from objectia.models import Usage


class UsageAPI(object):
    """
    Usage API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self):
        resp = self.client.get("/usage")
        return Usage(self, resp)
