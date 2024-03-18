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


class Private(BaseModel):
    # Id of the borrower
    borrower_id: typing.Optional[int] = Field(None, alias='borrowerId')

    # Zip of the borrower
    zip: typing.Optional[typing.Optional[str]] = Field(None, alias='zip')

    # City of the borrower
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # Age of the borrower
    age: typing.Optional[int] = Field(None, alias='age')

    # Gender of borrower
    gender: typing.Optional[typing.Optional[str]] = Field(None, alias='gender')

    # Borrower type
    category: typing.Optional[typing.Optional[str]] = Field(None, alias='category')

    # Description of the housing conditon (used to calculate the living costs)
    housing_condition: typing.Optional[typing.Optional[str]] = Field(None, alias='housingCondition')

    # Residential situation
    residential_situation: typing.Optional[typing.Optional[str]] = Field(None, alias='residentialSituation')

    # Nationality
    nationality: typing.Optional[typing.Optional[str]] = Field(None, alias='nationality')

    # Number of children
    children: typing.Optional[int] = Field(None, alias='children')

    # Profession description
    profession: typing.Optional[typing.Optional[str]] = Field(None, alias='profession')

    # Date since started with the current employer
    work_since: typing.Optional[typing.Optional[str]] = Field(None, alias='workSince')

    # Check in economical database successful
    solvency: typing.Optional[typing.Optional[str]] = Field(None, alias='solvency')

    # Monthly net income of the borrower
    monthly_net_income: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyNetIncome')

    # Income of the partner (if parter as a second borrower included)
    partner_income: typing.Optional[typing.Union[int, float]] = Field(None, alias='partnerIncome')

    # Income minus expenses
    available_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableAmount')

    # Relation of monthly payment with available amount (how much of the available amount is covered by the monthly payment)
    available_amount_percentage: typing.Optional[typing.Union[int, float]] = Field(None, alias='availableAmountPercentage')

    # Monthly payment of the requested loan
    monthly_payment: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyPayment')

    # Are there any collection procedures in the last three years
    collection_procedures: typing.Optional[typing.Optional[str]] = Field(None, alias='collectionProcedures')
    class Config:
        arbitrary_types_allowed = True
