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


class Crif(BaseModel):
    # Credit score of the borrower in Crif
    credit_score: typing.Optional[int] = Field(None, alias='creditScore')

    # Date when borrower score is checked
    checking_date: typing.Optional[typing.Optional[str]] = Field(None, alias='checkingDate')
    class Config:
        arbitrary_types_allowed = True
