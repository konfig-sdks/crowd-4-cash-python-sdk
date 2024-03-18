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


class RequiredPrivate(TypedDict):
    pass

class OptionalPrivate(TypedDict, total=False):
    # Id of the borrower
    borrowerId: int

    # Zip of the borrower
    zip: typing.Optional[str]

    # City of the borrower
    city: typing.Optional[str]

    # Age of the borrower
    age: int

    # Gender of borrower
    gender: typing.Optional[str]

    # Borrower type
    category: typing.Optional[str]

    # Description of the housing conditon (used to calculate the living costs)
    housingCondition: typing.Optional[str]

    # Residential situation
    residentialSituation: typing.Optional[str]

    # Nationality
    nationality: typing.Optional[str]

    # Number of children
    children: int

    # Profession description
    profession: typing.Optional[str]

    # Date since started with the current employer
    workSince: typing.Optional[str]

    # Check in economical database successful
    solvency: typing.Optional[str]

    # Monthly net income of the borrower
    monthlyNetIncome: typing.Union[int, float]

    # Income of the partner (if parter as a second borrower included)
    partnerIncome: typing.Union[int, float]

    # Income minus expenses
    availableAmount: typing.Union[int, float]

    # Relation of monthly payment with available amount (how much of the available amount is covered by the monthly payment)
    availableAmountPercentage: typing.Union[int, float]

    # Monthly payment of the requested loan
    monthlyPayment: typing.Union[int, float]

    # Are there any collection procedures in the last three years
    collectionProcedures: typing.Optional[str]

class Private(RequiredPrivate, OptionalPrivate):
    pass
