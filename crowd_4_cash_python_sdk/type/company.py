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


class RequiredCompany(TypedDict):
    pass

class OptionalCompany(TypedDict, total=False):
    # Legal form of the company
    legalForm: typing.Optional[str]

    # Year established in the commercial resgister
    yearEstablished: typing.Optional[int]

    # Company headquarter
    city: typing.Optional[str]

    # Business sector
    sector: typing.Optional[str]

    # Number of employees
    numberOfEmployees: typing.Optional[int]

class Company(RequiredCompany, OptionalCompany):
    pass
