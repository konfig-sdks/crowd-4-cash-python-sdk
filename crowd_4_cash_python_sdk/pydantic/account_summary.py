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


class AccountSummary(BaseModel):
    # Balance at the beggining of the month
    opening_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='openingBalance')

    # Interest that investor receives for all investments during the months
    interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='interest')

    # Interest that investor receives for the late payments
    default_interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='defaultInterest')

    # Principal paid to investor during the month
    principal: typing.Optional[typing.Union[int, float]] = Field(None, alias='principal')

    # Investor's investments during the month
    investments: typing.Optional[typing.Union[int, float]] = Field(None, alias='investments')

    # Commission paid by investor during the month
    commission: typing.Optional[typing.Union[int, float]] = Field(None, alias='commission')

    # Paid bids by investor during the months
    deposits: typing.Optional[typing.Union[int, float]] = Field(None, alias='deposits')

    # Deposits returned to investor during the month, due to cancelation of the agreement by the borrower
    withdrawals: typing.Optional[typing.Union[int, float]] = Field(None, alias='withdrawals')

    # Balance at the end of the month
    closing_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='closingBalance')
    class Config:
        arbitrary_types_allowed = True
