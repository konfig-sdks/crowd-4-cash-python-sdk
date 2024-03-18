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


class RequiredTransacions(TypedDict):
    pass

class OptionalTransacions(TypedDict, total=False):
    # Id of the transaction
    transactionId: typing.Optional[str]

    # Date when the transaction is made
    transactionDate: typing.Optional[str]

    # Type of the transaction - deposit, interest, withdrawal, etc.
    transactionType: typing.Optional[str]

    # Loan Id
    loanId: int

    # Amount of the transaction
    amount: typing.Union[int, float]

    # Currency
    currency: typing.Optional[str]

    # Description of the transaction
    remarks: typing.Optional[str]

class Transacions(RequiredTransacions, OptionalTransacions):
    pass
