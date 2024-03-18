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


class RequiredEarlyRepayment(TypedDict):
    pass

class OptionalEarlyRepayment(TypedDict, total=False):
    # date when the loan has been paid off
    paymentDate: typing.Optional[str]

    # the amount due and owed to satisfy the payoff of the loan
    principalBalance: typing.Union[int, float]

    # Gross interest amount
    interest: typing.Union[int, float]

    # investor commission amount
    investorCommission: typing.Union[int, float]

    # a total amount that has been paid earlier to the investor
    totalAmount: typing.Union[int, float]

class EarlyRepayment(RequiredEarlyRepayment, OptionalEarlyRepayment):
    pass
