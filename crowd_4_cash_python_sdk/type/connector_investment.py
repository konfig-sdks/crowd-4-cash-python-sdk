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


class RequiredConnectorInvestment(TypedDict):
    pass

class OptionalConnectorInvestment(TypedDict, total=False):
    # Id of the investor
    investorId: int

    # Name of the investor
    investorName: typing.Optional[str]

    # Amount of the bid
    bidAmount: typing.Union[int, float]

    # Date when the bid is placed
    bidDate: typing.Optional[str]

    # Id of the loan
    loanId: int

    # Amount of the loan
    loanAmount: typing.Union[int, float]

    # Duration of the loan in months
    loanDuration: int

    # Interest rate of the loan
    loanInterest: typing.Union[int, float]

    # Rating of the loan - AA, A, B, C, D
    loanRating: typing.Optional[str]

class ConnectorInvestment(RequiredConnectorInvestment, OptionalConnectorInvestment):
    pass
