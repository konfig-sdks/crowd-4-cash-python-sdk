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


class RequiredCrif(TypedDict):
    pass

class OptionalCrif(TypedDict, total=False):
    # Credit score of the borrower in Crif
    creditScore: int

    # Date when borrower score is checked
    checkingDate: typing.Optional[str]

class Crif(RequiredCrif, OptionalCrif):
    pass
