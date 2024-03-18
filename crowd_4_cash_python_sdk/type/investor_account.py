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

from crowd_4_cash_python_sdk.type.account_details import AccountDetails
from crowd_4_cash_python_sdk.type.account_summary import AccountSummary
from crowd_4_cash_python_sdk.type.auto_invest_settings import AutoInvestSettings
from crowd_4_cash_python_sdk.type.transacions import Transacions

class RequiredInvestorAccount(TypedDict):
    pass

class OptionalInvestorAccount(TypedDict, total=False):
    accountSummary: AccountSummary

    transactions: typing.Optional[typing.List[Transacions]]

    accountDetails: AccountDetails

    autoInvestSettings: AutoInvestSettings

class InvestorAccount(RequiredInvestorAccount, OptionalInvestorAccount):
    pass
