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

from crowd_4_cash_python_sdk.type.connected_investor import ConnectedInvestor

class RequiredConnectorSummary(TypedDict):
    pass

class OptionalConnectorSummary(TypedDict, total=False):
    # Name of the connector
    connectorName: typing.Optional[str]

    # Number of pending investments
    pendingInvestmentsCount: int

    # Total amount of pending investments
    pendingInvestmentsTotal: typing.Union[int, float]

    # Number of active investments
    activeInvestmentsCount: int

    # Total amount of active investments
    activeInvestmentsTotal: typing.Union[int, float]

    # List of connected investors
    connectedInvestors: typing.Optional[typing.List[ConnectedInvestor]]

class ConnectorSummary(RequiredConnectorSummary, OptionalConnectorSummary):
    pass
