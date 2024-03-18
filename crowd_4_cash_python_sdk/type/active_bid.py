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


class RequiredActiveBid(TypedDict):
    pass

class OptionalActiveBid(TypedDict, total=False):
    # Investor pseudonym
    pseudonym: typing.Optional[str]

    # Bidding date
    dateCreated: typing.Optional[str]

    # Bid amount
    amount: typing.Union[int, float]

class ActiveBid(RequiredActiveBid, OptionalActiveBid):
    pass
