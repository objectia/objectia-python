import unittest
import tests.config as config
from objectia import Client
# import objectia
from objectia.models import Usage


class ClientTest(unittest.TestCase):

    def setUp(self):
        self.client = Client(api_key=config.API_KEY)

    def test_client_without_api_key(self):
        with self.assertRaises(ValueError):
            Client(api_key="")

    def test_get_api_usage(self):
        usage = self.client.usage.get()
        self.assertIsInstance(usage, Usage)


if __name__ == "__main__":
    unittest.main()
