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


class RequiredAccountStatementEntry(TypedDict):
    pass

class OptionalAccountStatementEntry(TypedDict, total=False):
    # Number of the borrower instalment
    annuityNumber: int

    # Instalment due date
    dueDate: typing.Optional[str]

    # A date when the instalment is paid by borrower
    messageDate: typing.Optional[str]

    # A date when payment is booked in C4C system
    matchingDate: typing.Optional[str]

    # An amount paid by the borrower
    amount: typing.Union[int, float]

class AccountStatementEntry(RequiredAccountStatementEntry, OptionalAccountStatementEntry):
    pass
