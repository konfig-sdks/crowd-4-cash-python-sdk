# coding: utf-8

# flake8: noqa

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

__version__ = "2.0.0"

# import ApiClient
from crowd_4_cash_python_sdk.api_client import ApiClient

# import Configuration
from crowd_4_cash_python_sdk.configuration import Configuration

# import exceptions
from crowd_4_cash_python_sdk.exceptions import OpenApiException
from crowd_4_cash_python_sdk.exceptions import ApiAttributeError
from crowd_4_cash_python_sdk.exceptions import ApiTypeError
from crowd_4_cash_python_sdk.exceptions import ApiValueError
from crowd_4_cash_python_sdk.exceptions import ApiKeyError
from crowd_4_cash_python_sdk.exceptions import ApiException

from crowd_4_cash_python_sdk.client import Crowd4Cash
