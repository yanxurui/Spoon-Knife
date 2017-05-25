import unittest
from pymemcache.client.base import Client

class TestMemcached(unittest.TestCase):
    def test_set_get(self):
        client = Client(('localhost', 11211))
        client.set('some_key', 'some_value')
        result = client.get('some_key')
        self.assertEqual(result, 'some_value')

    def test_delete(self):
        client = Client(('localhost', 11212))
        client.set('some_key', 'some_value')
        client.delete('some_key')
        result = client.get('some_key')
        self.assertEqual(result, None)