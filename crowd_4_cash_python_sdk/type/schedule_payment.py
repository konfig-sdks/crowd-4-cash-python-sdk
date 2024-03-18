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


class RequiredSchedulePayment(TypedDict):
    pass

class OptionalSchedulePayment(TypedDict, total=False):
    # Number of the investor instalment
    annuityNumber: int

    # Instalment due date
    annuityDate: typing.Optional[str]

    # An amount the investor receives each month
    annuityAmount: typing.Union[int, float]

    # The principal part of the instalment
    principalPortion: typing.Union[int, float]

    # The interest part of the instalment
    interestPortion: typing.Union[int, float]

    # The insurance fee amount
    insuranceFee: typing.Union[int, float]

    # The administrative fee amount
    administrativeFee: typing.Union[int, float]

    # Monthly commission that investor pays
    commissionPortion: typing.Union[int, float]

    # Monthly net income of the investor (monthly interest - monthly commission)
    netIncome: typing.Union[int, float]

    # The amount of principal on the loan
    principalBalance: typing.Union[int, float]

    # The status of the instalment
    annuityStatus: typing.Optional[str]

    # Is instalment is paid?
    isPaid: typing.Optional[str]

    # A date when the instalment is paid.
    datePaid: typing.Optional[str]

    # Some explanation of the instalment
    note: typing.Optional[str]

class SchedulePayment(RequiredSchedulePayment, OptionalSchedulePayment):
    pass
