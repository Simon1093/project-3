import unittest

import requests


class AppTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_secret(self):
        response = requests.get('http://localhost:8000/secret')
        self.assertEqual(response.text, 'test_secret')
