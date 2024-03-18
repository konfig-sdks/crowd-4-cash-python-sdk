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


class SchedulePayment(BaseModel):
    # Number of the investor instalment
    annuity_number: typing.Optional[int] = Field(None, alias='annuityNumber')

    # Instalment due date
    annuity_date: typing.Optional[typing.Optional[str]] = Field(None, alias='annuityDate')

    # An amount the investor receives each month
    annuity_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='annuityAmount')

    # The principal part of the instalment
    principal_portion: typing.Optional[typing.Union[int, float]] = Field(None, alias='principalPortion')

    # The interest part of the instalment
    interest_portion: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestPortion')

    # The insurance fee amount
    insurance_fee: typing.Optional[typing.Union[int, float]] = Field(None, alias='insuranceFee')

    # The administrative fee amount
    administrative_fee: typing.Optional[typing.Union[int, float]] = Field(None, alias='administrativeFee')

    # Monthly commission that investor pays
    commission_portion: typing.Optional[typing.Union[int, float]] = Field(None, alias='commissionPortion')

    # Monthly net income of the investor (monthly interest - monthly commission)
    net_income: typing.Optional[typing.Union[int, float]] = Field(None, alias='netIncome')

    # The amount of principal on the loan
    principal_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='principalBalance')

    # The status of the instalment
    annuity_status: typing.Optional[typing.Optional[str]] = Field(None, alias='annuityStatus')

    # Is instalment is paid?
    is_paid: typing.Optional[typing.Optional[str]] = Field(None, alias='isPaid')

    # A date when the instalment is paid.
    date_paid: typing.Optional[typing.Optional[str]] = Field(None, alias='datePaid')

    # Some explanation of the instalment
    note: typing.Optional[typing.Optional[str]] = Field(None, alias='note')
    class Config:
        arbitrary_types_allowed = True
