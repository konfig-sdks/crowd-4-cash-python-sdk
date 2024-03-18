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


class ConnectorInvestment(BaseModel):
    # Id of the investor
    investor_id: typing.Optional[int] = Field(None, alias='investorId')

    # Name of the investor
    investor_name: typing.Optional[typing.Optional[str]] = Field(None, alias='investorName')

    # Amount of the bid
    bid_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='bidAmount')

    # Date when the bid is placed
    bid_date: typing.Optional[typing.Optional[str]] = Field(None, alias='bidDate')

    # Id of the loan
    loan_id: typing.Optional[int] = Field(None, alias='loanId')

    # Amount of the loan
    loan_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanAmount')

    # Duration of the loan in months
    loan_duration: typing.Optional[int] = Field(None, alias='loanDuration')

    # Interest rate of the loan
    loan_interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanInterest')

    # Rating of the loan - AA, A, B, C, D
    loan_rating: typing.Optional[typing.Optional[str]] = Field(None, alias='loanRating')
    class Config:
        arbitrary_types_allowed = True
