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


class RequiredManualBuilderOption(TypedDict):
    pass

class OptionalManualBuilderOption(TypedDict, total=False):
    # Id of the manual portfolio builder
    id: int

    # Current investment using manual autoinvest
    investmentCurrently: typing.Union[int, float]

    # Who's create the manual portfolio builder?
    originators: typing.Optional[str]

    # Is manual portfolio builder active? - yes, no
    isActive: bool

class ManualBuilderOption(RequiredManualBuilderOption, OptionalManualBuilderOption):
    pass
