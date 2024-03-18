# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

import unittest

import os
from pprint import pprint
from crowd_4_cash_python_sdk import Crowd4Cash

class TestSimple(unittest.TestCase):
    def setUp(self):
        pass

    def test_client(self):
        crowd4cash = Crowd4Cash(
        
                        bearer = 'YOUR_API_KEY',
        )
        self.assertIsNotNone(crowd4cash)

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main()
