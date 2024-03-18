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


class RequiredAccountSummary(TypedDict):
    pass

class OptionalAccountSummary(TypedDict, total=False):
    # Balance at the beggining of the month
    openingBalance: typing.Union[int, float]

    # Interest that investor receives for all investments during the months
    interest: typing.Union[int, float]

    # Interest that investor receives for the late payments
    defaultInterest: typing.Union[int, float]

    # Principal paid to investor during the month
    principal: typing.Union[int, float]

    # Investor's investments during the month
    investments: typing.Union[int, float]

    # Commission paid by investor during the month
    commission: typing.Union[int, float]

    # Paid bids by investor during the months
    deposits: typing.Union[int, float]

    # Deposits returned to investor during the month, due to cancelation of the agreement by the borrower
    withdrawals: typing.Union[int, float]

    # Balance at the end of the month
    closingBalance: typing.Union[int, float]

class AccountSummary(RequiredAccountSummary, OptionalAccountSummary):
    pass
