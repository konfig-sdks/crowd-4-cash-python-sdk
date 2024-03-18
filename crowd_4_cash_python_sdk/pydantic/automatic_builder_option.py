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


class AutomaticBuilderOption(BaseModel):
    # Id of the automatic portfolio builder
    id: typing.Optional[int] = Field(None, alias='id')

    # Current investment using automatic autoinvest
    investment_currently: typing.Optional[typing.Union[int, float]] = Field(None, alias='investmentCurrently')

    # Total amount that can be invested using automatic autoinvest
    total_amount_for_investment: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAmountForInvestment')

    # Who's create/update the automatic portfolio builder?
    originators: typing.Optional[typing.Optional[str]] = Field(None, alias='originators')

    # Minimum interest rate of the loan in which investor wants to invest
    interest_rate_from: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestRateFrom')

    # Mаџимум interest rate of the loan in which investor wants to invest
    interest_rate_to: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestRateTo')

    # Maximum bid amount per loan
    maximum_per_bid: typing.Optional[typing.Union[int, float]] = Field(None, alias='maximumPerBid')

    # Minimum bid amount per loan
    minimum_per_bid: typing.Optional[typing.Union[int, float]] = Field(None, alias='minimumPerBid')

    # Can investments be reinvested? - yes, no
    reinvest: typing.Optional[bool] = Field(None, alias='reinvest')

    # Investment level - conservative, balanced, growth
    investment_level: typing.Optional[typing.Optional[str]] = Field(None, alias='investmentLevel')

    # Can investment be sold on the secondary market? - yes, no
    secondary_market: typing.Optional[bool] = Field(None, alias='secondaryMarket')

    # Is automatic portfolio builder active? - yes, no
    is_active: typing.Optional[bool] = Field(None, alias='isActive')

    # Date when automatic autoinvest starts to be used
    duration_from: typing.Optional[int] = Field(None, alias='durationFrom')

    # Date when automatic autoinvest ends to be used
    duration_to: typing.Optional[int] = Field(None, alias='durationTo')

    # Currency
    currency: typing.Optional[typing.Optional[str]] = Field(None, alias='currency')
    class Config:
        arbitrary_types_allowed = True
