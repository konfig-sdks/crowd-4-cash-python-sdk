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

from crowd_4_cash_python_sdk.pydantic.intermediary_loan import IntermediaryLoan
from crowd_4_cash_python_sdk.pydantic.intermediary_partner import IntermediaryPartner

class IntermediarySummary(BaseModel):
    # Name of the intermediary company
    intermediary_name: typing.Optional[typing.Optional[str]] = Field(None, alias='intermediaryName')

    # Number of partners aka garages
    number_of_partners: typing.Optional[int] = Field(None, alias='numberOfPartners')

    # Number of loan applications
    number_of_loans: typing.Optional[int] = Field(None, alias='numberOfLoans')

    # A sum of all partner loans
    loans_total_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loansTotalAmount')

    # List of your partners (garages/shops/stores)
    partners: typing.Optional[typing.Optional[typing.List[IntermediaryPartner]]] = Field(None, alias='partners')

    # List of your partner loan(s)
    loans: typing.Optional[typing.Optional[typing.List[IntermediaryLoan]]] = Field(None, alias='loans')
    class Config:
        arbitrary_types_allowed = True
