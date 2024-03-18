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


class Income(BaseModel):
    # Profession description
    profession: typing.Optional[typing.Optional[str]] = Field(None, alias='profession')

    # Type of employment
    employment_type: typing.Optional[typing.Optional[str]] = Field(None, alias='employmentType')

    # Is the employment under notice
    employment_relationship_under_notice: typing.Optional[typing.Optional[str]] = Field(None, alias='employmentRelationshipUnderNotice')

    # Date since started with the current employer
    work_since: typing.Optional[typing.Optional[str]] = Field(None, alias='workSince')

    # Number of salaries paid out to borrower
    number_of_salaries: typing.Optional[int] = Field(None, alias='numberOfSalaries')

    # Monthly net income of the borrower
    monthly_net_income: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyNetIncome')

    # Average bonus of the last 3 years
    bonus_average: typing.Optional[typing.Union[int, float]] = Field(None, alias='bonusAverage')

    # Additional income included?
    additional_income: typing.Optional[typing.Optional[str]] = Field(None, alias='additionalIncome')

    # Source of additional income
    additional_income_type: typing.Optional[typing.Optional[str]] = Field(None, alias='additionalIncomeType')

    # Amount of the additional income
    additional_income_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='additionalIncomeAmount')

    # Include partner income?
    partner_income: typing.Optional[typing.Optional[str]] = Field(None, alias='partnerIncome')

    # Profession description (Partner)
    partner_profession: typing.Optional[typing.Optional[str]] = Field(None, alias='partnerProfession')

    # Date since started with the current employer (Partner)
    partner_work_since: typing.Optional[typing.Optional[str]] = Field(None, alias='partnerWorkSince')

    # Number of salaries paid out to partner
    partner_number_of_salaries: typing.Optional[int] = Field(None, alias='partnerNumberOfSalaries')

    # Monthly net income of the partner
    partner_monthly_net_income: typing.Optional[typing.Union[int, float]] = Field(None, alias='partnerMonthlyNetIncome')

    # Average bonus of partner of the last three years
    partner_bonus_average: typing.Optional[typing.Union[int, float]] = Field(None, alias='partnerBonusAverage')
    class Config:
        arbitrary_types_allowed = True
