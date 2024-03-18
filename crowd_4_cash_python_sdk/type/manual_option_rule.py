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


class RequiredManualOptionRule(TypedDict):
    pass

class OptionalManualOptionRule(TypedDict, total=False):
    loanRating: typing.Optional[str]

    # Total amount that can be invested using manual autoinvest
    totalAmountForInvestment: typing.Union[int, float]

    # Minimum interest rate of the loan in which investor wants to invest
    minimumInterestRate: typing.Union[int, float]

    # Minimum bid amount per loan
    minimumPerBid: typing.Union[int, float]

    # Maximum bid amount per loan
    maximumPerBid: typing.Union[int, float]

    # Can investments be reinvested? - yes, no
    reinvest: bool

    # Can investment be sold on the secondary market? - yes, no
    secondaryMarket: bool

    # Date when manual autoinvest starts to be used
    durationFrom: int

    # Date when manual autoinvest ends to be used
    durationTo: int

    # Is manual autoinvest enabled? yes. no
    isEnabled: bool

    # Currency
    currency: typing.Optional[str]

class ManualOptionRule(RequiredManualOptionRule, OptionalManualOptionRule):
    pass
