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


class RequiredMultipleBiddingResult(TypedDict):
    pass

class OptionalMultipleBiddingResult(TypedDict, total=False):
    # Success or Error
    result: typing.Optional[str]

    # If no error, it's empty
    error: typing.Optional[str]

class MultipleBiddingResult(RequiredMultipleBiddingResult, OptionalMultipleBiddingResult):
    pass
