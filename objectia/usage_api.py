class UsageAPI(object):
    """
    Usage API
    """
    def __init__(self, objectia):
        self.client = objectia.client

    def get(self):
        return self.client.get("/usage")
