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


class EarlyRepayment(BaseModel):
    # date when the loan has been paid off
    payment_date: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentDate')

    # the amount due and owed to satisfy the payoff of the loan
    principal_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='principalBalance')

    # Gross interest amount
    interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='interest')

    # investor commission amount
    investor_commission: typing.Optional[typing.Union[int, float]] = Field(None, alias='investorCommission')

    # a total amount that has been paid earlier to the investor
    total_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAmount')
    class Config:
        arbitrary_types_allowed = True
