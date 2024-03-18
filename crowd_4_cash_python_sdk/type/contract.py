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


class RequiredContract(TypedDict):
    pass

class OptionalContract(TypedDict, total=False):
    # ID of the loan you have invested in
    loanId: int

    # Name of the file (.PDF)
    contractName: typing.Optional[str]

    # String representation of the contract that is encoded with base-64 digits
    contractFile: typing.Optional[str]

class Contract(RequiredContract, OptionalContract):
    pass
