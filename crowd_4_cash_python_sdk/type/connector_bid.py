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


class RequiredConnectorBid(TypedDict):
    # Investor ID
    investorId: int

    # Loan ID on which you want to place a bid on behalf of your investors
    loanId: int

    # Amount of the bid
    amount: typing.Union[int, float]

class OptionalConnectorBid(TypedDict, total=False):
    pass

class ConnectorBid(RequiredConnectorBid, OptionalConnectorBid):
    pass
