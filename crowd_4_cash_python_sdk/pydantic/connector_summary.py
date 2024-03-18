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

from crowd_4_cash_python_sdk.pydantic.connected_investor import ConnectedInvestor

class ConnectorSummary(BaseModel):
    # Name of the connector
    connector_name: typing.Optional[typing.Optional[str]] = Field(None, alias='connectorName')

    # Number of pending investments
    pending_investments_count: typing.Optional[int] = Field(None, alias='pendingInvestmentsCount')

    # Total amount of pending investments
    pending_investments_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='pendingInvestmentsTotal')

    # Number of active investments
    active_investments_count: typing.Optional[int] = Field(None, alias='activeInvestmentsCount')

    # Total amount of active investments
    active_investments_total: typing.Optional[typing.Union[int, float]] = Field(None, alias='activeInvestmentsTotal')

    # List of connected investors
    connected_investors: typing.Optional[typing.Optional[typing.List[ConnectedInvestor]]] = Field(None, alias='connectedInvestors')
    class Config:
        arbitrary_types_allowed = True
