# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING


class RequiredLogin(TypedDict):
    # Your C4C username
    username: str

    # Your C4C password
    password: str

class OptionalLogin(TypedDict, total=False):
    pass

class Login(RequiredLogin, OptionalLogin):
    pass
