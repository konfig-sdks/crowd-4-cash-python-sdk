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


class ConnectedInvestor(BaseModel):
    # Id of the investor
    investor_id: typing.Optional[int] = Field(None, alias='investorId')

    # Type of the investor Private/Company
    investor_type: typing.Optional[typing.Optional[str]] = Field(None, alias='investorType')

    # Name of the investor
    investor_name: typing.Optional[typing.Optional[str]] = Field(None, alias='investorName')

    # Number of pending investments
    pending_investments_count: typing.Optional[int] = Field(None, alias='pendingInvestmentsCount')

    # Total amount of pending investments
    pending_investments_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='pendingInvestmentsTotal')

    # Number of active investments
    active_investments_count: typing.Optional[int] = Field(None, alias='activeInvestmentsCount')

    # Total amount of active investments
    active_investments_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='activeInvestmentsTotal')
    class Config:
        arbitrary_types_allowed = True
