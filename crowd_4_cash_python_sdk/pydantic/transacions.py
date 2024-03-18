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


class Transacions(BaseModel):
    # Id of the transaction
    transaction_id: typing.Optional[typing.Optional[str]] = Field(None, alias='transactionId')

    # Date when the transaction is made
    transaction_date: typing.Optional[typing.Optional[str]] = Field(None, alias='transactionDate')

    # Type of the transaction - deposit, interest, withdrawal, etc.
    transaction_type: typing.Optional[typing.Optional[str]] = Field(None, alias='transactionType')

    # Loan Id
    loan_id: typing.Optional[int] = Field(None, alias='loanId')

    # Amount of the transaction
    amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='amount')

    # Currency
    currency: typing.Optional[typing.Optional[str]] = Field(None, alias='currency')

    # Description of the transaction
    remarks: typing.Optional[typing.Optional[str]] = Field(None, alias='remarks')
    class Config:
        arbitrary_types_allowed = True
