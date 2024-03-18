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

from crowd_4_cash_python_sdk.type.manual_builder_option import ManualBuilderOption
from crowd_4_cash_python_sdk.type.manual_option_rule import ManualOptionRule

class RequiredManualBuilder(TypedDict):
    pass

class OptionalManualBuilder(TypedDict, total=False):
    builderOption: ManualBuilderOption

    rules: typing.Optional[typing.List[ManualOptionRule]]

class ManualBuilder(RequiredManualBuilder, OptionalManualBuilder):
    pass
