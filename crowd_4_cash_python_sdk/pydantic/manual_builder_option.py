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


class ManualBuilderOption(BaseModel):
    # Id of the manual portfolio builder
    id: typing.Optional[int] = Field(None, alias='id')

    # Current investment using manual autoinvest
    investment_currently: typing.Optional[typing.Union[int, float]] = Field(None, alias='investmentCurrently')

    # Who's create the manual portfolio builder?
    originators: typing.Optional[typing.Optional[str]] = Field(None, alias='originators')

    # Is manual portfolio builder active? - yes, no
    is_active: typing.Optional[bool] = Field(None, alias='isActive')
    class Config:
        arbitrary_types_allowed = True
