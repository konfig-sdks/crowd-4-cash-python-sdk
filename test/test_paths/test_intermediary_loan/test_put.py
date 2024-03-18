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
from crowd_4_cash_python_sdk.paths.intermediary_loan import put
from crowd_4_cash_python_sdk import configuration, schemas, api_client

from .. import ApiTestMixin


class TestIntermediaryLoan(ApiTestMixin, unittest.TestCase):
    """
    IntermediaryLoan unit test stubs
        Set the definitive Handover Date (a date when the item is handed over to the customer)
    """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
