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

from crowd_4_cash_python_sdk.pydantic.account_details import AccountDetails
from crowd_4_cash_python_sdk.pydantic.account_summary import AccountSummary
from crowd_4_cash_python_sdk.pydantic.auto_invest_settings import AutoInvestSettings
from crowd_4_cash_python_sdk.pydantic.transacions import Transacions

class InvestorAccount(BaseModel):
    account_summary: typing.Optional[AccountSummary] = Field(None, alias='accountSummary')

    transactions: typing.Optional[typing.Optional[typing.List[Transacions]]] = Field(None, alias='transactions')

    account_details: typing.Optional[AccountDetails] = Field(None, alias='accountDetails')

    auto_invest_settings: typing.Optional[AutoInvestSettings] = Field(None, alias='autoInvestSettings')
    class Config:
        arbitrary_types_allowed = True
