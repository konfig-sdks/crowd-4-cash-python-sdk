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


class AccountStatementEntry(BaseModel):
    # Number of the borrower instalment
    annuity_number: typing.Optional[int] = Field(None, alias='annuityNumber')

    # Instalment due date
    due_date: typing.Optional[typing.Optional[str]] = Field(None, alias='dueDate')

    # A date when the instalment is paid by borrower
    message_date: typing.Optional[typing.Optional[str]] = Field(None, alias='messageDate')

    # A date when payment is booked in C4C system
    matching_date: typing.Optional[typing.Optional[str]] = Field(None, alias='matchingDate')

    # An amount paid by the borrower
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')
    class Config:
        arbitrary_types_allowed = True
