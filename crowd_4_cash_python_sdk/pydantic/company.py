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


class Company(BaseModel):
    # Legal form of the company
    legal_form: typing.Optional[typing.Optional[str]] = Field(None, alias='legalForm')

    # Year established in the commercial resgister
    year_established: typing.Optional[typing.Optional[int]] = Field(None, alias='yearEstablished')

    # Company headquarter
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # Business sector
    sector: typing.Optional[typing.Optional[str]] = Field(None, alias='sector')

    # Number of employees
    number_of_employees: typing.Optional[typing.Optional[int]] = Field(None, alias='numberOfEmployees')
    class Config:
        arbitrary_types_allowed = True
