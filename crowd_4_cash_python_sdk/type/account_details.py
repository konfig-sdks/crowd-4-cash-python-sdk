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


class RequiredAccountDetails(TypedDict):
    pass

class OptionalAccountDetails(TypedDict, total=False):
    # Receivables that are not paid to investor
    availableCash: typing.Union[int, float]

    # Currency
    availableCashCurrency: typing.Optional[str]

    # Current principal balance + available cash
    accountValue: typing.Union[int, float]

    # Current principal balance
    investedAmount: typing.Union[int, float]

    # Current number of investments
    numberOfInvestments: int

    # The sum of \"bad debt\" and \"default\"
    losses: typing.Union[int, float]

class AccountDetails(RequiredAccountDetails, OptionalAccountDetails):
    pass
