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


class Contract(BaseModel):
    # ID of the loan you have invested in
    loan_id: typing.Optional[int] = Field(None, alias='loanId')

    # Name of the file (.PDF)
    contract_name: typing.Optional[typing.Optional[str]] = Field(None, alias='contractName')

    # String representation of the contract that is encoded with base-64 digits
    contract_file: typing.Optional[typing.Optional[str]] = Field(None, alias='contractFile')
    class Config:
        arbitrary_types_allowed = True
