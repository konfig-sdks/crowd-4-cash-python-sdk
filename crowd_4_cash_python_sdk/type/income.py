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


class RequiredIncome(TypedDict):
    pass

class OptionalIncome(TypedDict, total=False):
    # Profession description
    profession: typing.Optional[str]

    # Type of employment
    employmentType: typing.Optional[str]

    # Is the employment under notice
    employmentRelationshipUnderNotice: typing.Optional[str]

    # Date since started with the current employer
    workSince: typing.Optional[str]

    # Number of salaries paid out to borrower
    numberOfSalaries: int

    # Monthly net income of the borrower
    monthlyNetIncome: typing.Union[int, float]

    # Average bonus of the last 3 years
    bonusAverage: typing.Union[int, float]

    # Additional income included?
    additionalIncome: typing.Optional[str]

    # Source of additional income
    additionalIncomeType: typing.Optional[str]

    # Amount of the additional income
    additionalIncomeAmount: typing.Union[int, float]

    # Include partner income?
    partnerIncome: typing.Optional[str]

    # Profession description (Partner)
    partnerProfession: typing.Optional[str]

    # Date since started with the current employer (Partner)
    partnerWorkSince: typing.Optional[str]

    # Number of salaries paid out to partner
    partnerNumberOfSalaries: int

    # Monthly net income of the partner
    partnerMonthlyNetIncome: typing.Union[int, float]

    # Average bonus of partner of the last three years
    partnerBonusAverage: typing.Union[int, float]

class Income(RequiredIncome, OptionalIncome):
    pass
