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


class RentalApplicationResult(BaseModel):
    # Success or Error
    result: typing.Optional[typing.Optional[str]] = Field(None, alias='result')

    # Message of the action
    message: typing.Optional[typing.Optional[str]] = Field(None, alias='message')

    # ID of the newly created loan
    loan_id: typing.Optional[int] = Field(None, alias='loanId')

    # ESR of the newly created loan
    esr: typing.Optional[typing.Optional[str]] = Field(None, alias='esr')

    # Monthly payment on a loan with insurance premium amount added
    rental_amount_with_insurance: typing.Optional[typing.Union[int, float]] = Field(None, alias='rentalAmountWithInsurance')

    # If no error, it's empty
    error: typing.Optional[typing.Optional[str]] = Field(None, alias='error')
    class Config:
        arbitrary_types_allowed = True
