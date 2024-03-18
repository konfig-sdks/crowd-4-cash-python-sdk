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


class RequiredIntermediaryLoanHandoverDate(TypedDict):
    pass

class OptionalIntermediaryLoanHandoverDate(TypedDict, total=False):
    # Loan ID
    loanId: int

    # The date when the car is handed over to the subscriber
    handoverDate: typing.Optional[str]

class IntermediaryLoanHandoverDate(RequiredIntermediaryLoanHandoverDate, OptionalIntermediaryLoanHandoverDate):
    pass
