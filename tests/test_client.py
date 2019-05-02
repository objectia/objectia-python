import unittest
import tests.config as config
from objectia import Client


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(api_key=config.API_KEY)

    def test_client_without_api_key(self):
        with self.assertRaises(ValueError):
            Client(api_key="")

    def test_get_api_usage(self):
        usage = self.client.usage.get()
        self.assertIsNotNone(usage)
        print("Geoip requests: {0}".format(usage["geoip_requests"]))

    def test_get_geoip(self):
        location = self.client.geoip.get("8.8.8.8")
        self.assertIsNotNone(location)
        print("Country code: {0}".format(location["country_code"]))

    def test_get_geoip_myip(self):
        location = self.client.geoip.get_current()
        self.assertIsNotNone(location)

    def test_get_geoip_bulk(self):
        location = self.client.geoip.get_bulk("8.8.8.8,google.com")
        self.assertIsNotNone(location)


if __name__ == "__main__":
    unittest.main()
