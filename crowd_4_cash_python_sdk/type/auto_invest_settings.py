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

from crowd_4_cash_python_sdk.type.automatic_builder import AutomaticBuilder
from crowd_4_cash_python_sdk.type.manual_builder import ManualBuilder

class RequiredAutoInvestSettings(TypedDict):
    pass

class OptionalAutoInvestSettings(TypedDict, total=False):
    automaticBuilder: AutomaticBuilder

    manualBuilder: ManualBuilder

class AutoInvestSettings(RequiredAutoInvestSettings, OptionalAutoInvestSettings):
    pass
