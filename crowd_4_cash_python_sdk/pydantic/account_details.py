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


class AccountDetails(BaseModel):
    # Receivables that are not paid to investor
    available_cash: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableCash')

    # Currency
    available_cash_currency: typing.Optional[typing.Optional[str]] = Field(None, alias='availableCashCurrency')

    # Current principal balance + available cash
    account_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountValue')

    # Current principal balance
    invested_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='investedAmount')

    # Current number of investments
    number_of_investments: typing.Optional[int] = Field(None, alias='numberOfInvestments')

    # The sum of \"bad debt\" and \"default\"
    losses: typing.Optional[typing.Union[int, float]] = Field(None, alias='losses')
    class Config:
        arbitrary_types_allowed = True
