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
from pydantic import BaseModel, Field, RootModel


class ManualOptionRule(BaseModel):
    loan_rating: typing.Optional[typing.Optional[str]] = Field(None, alias='loanRating')

    # Total amount that can be invested using manual autoinvest
    total_amount_for_investment: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAmountForInvestment')

    # Minimum interest rate of the loan in which investor wants to invest
    minimum_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='minimumInterestRate')

    # Minimum bid amount per loan
    minimum_per_bid: typing.Optional[typing.Union[int, float]] = Field(None, alias='minimumPerBid')

    # Maximum bid amount per loan
    maximum_per_bid: typing.Optional[typing.Union[int, float]] = Field(None, alias='maximumPerBid')

    # Can investments be reinvested? - yes, no
    reinvest: typing.Optional[bool] = Field(None, alias='reinvest')

    # Can investment be sold on the secondary market? - yes, no
    secondary_market: typing.Optional[bool] = Field(None, alias='secondaryMarket')

    # Date when manual autoinvest starts to be used
    duration_from: typing.Optional[int] = Field(None, alias='durationFrom')

    # Date when manual autoinvest ends to be used
    duration_to: typing.Optional[int] = Field(None, alias='durationTo')

    # Is manual autoinvest enabled? yes. no
    is_enabled: typing.Optional[bool] = Field(None, alias='isEnabled')

    # Currency
    currency: typing.Optional[typing.Optional[str]] = Field(None, alias='currency')
    class Config:
        arbitrary_types_allowed = True
