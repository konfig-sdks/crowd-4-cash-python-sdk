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


class RequiredRentalApplicationResult(TypedDict):
    pass

class OptionalRentalApplicationResult(TypedDict, total=False):
    # Success or Error
    result: typing.Optional[str]

    # Message of the action
    message: typing.Optional[str]

    # ID of the newly created loan
    loanId: int

    # ESR of the newly created loan
    esr: typing.Optional[str]

    # Monthly payment on a loan with insurance premium amount added
    rentalAmountWithInsurance: typing.Union[int, float]

    # If no error, it's empty
    error: typing.Optional[str]

class RentalApplicationResult(RequiredRentalApplicationResult, OptionalRentalApplicationResult):
    pass
