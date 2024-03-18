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


class RequiredAutomaticBuilderOption(TypedDict):
    pass

class OptionalAutomaticBuilderOption(TypedDict, total=False):
    # Id of the automatic portfolio builder
    id: int

    # Current investment using automatic autoinvest
    investmentCurrently: typing.Union[int, float]

    # Total amount that can be invested using automatic autoinvest
    totalAmountForInvestment: typing.Union[int, float]

    # Who's create/update the automatic portfolio builder?
    originators: typing.Optional[str]

    # Minimum interest rate of the loan in which investor wants to invest
    interestRateFrom: typing.Union[int, float]

    # Mаџимум interest rate of the loan in which investor wants to invest
    interestRateTo: typing.Union[int, float]

    # Maximum bid amount per loan
    maximumPerBid: typing.Union[int, float]

    # Minimum bid amount per loan
    minimumPerBid: typing.Union[int, float]

    # Can investments be reinvested? - yes, no
    reinvest: bool

    # Investment level - conservative, balanced, growth
    investmentLevel: typing.Optional[str]

    # Can investment be sold on the secondary market? - yes, no
    secondaryMarket: bool

    # Is automatic portfolio builder active? - yes, no
    isActive: bool

    # Date when automatic autoinvest starts to be used
    durationFrom: int

    # Date when automatic autoinvest ends to be used
    durationTo: int

    # Currency
    currency: typing.Optional[str]

class AutomaticBuilderOption(RequiredAutomaticBuilderOption, OptionalAutomaticBuilderOption):
    pass
