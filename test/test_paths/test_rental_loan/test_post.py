# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

import unittest
from unittest.mock import patch

import urllib3

import crowd_4_cash_python_sdk
from crowd_4_cash_python_sdk.paths.rental_loan import post
from crowd_4_cash_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestRentalLoan(ApiTestMixin, unittest.TestCase):
    """
    RentalLoan unit test stubs
        Apply for a rental loan
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
