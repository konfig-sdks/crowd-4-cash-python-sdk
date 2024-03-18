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


class RequiredQuestionnaire(TypedDict):
    pass

class OptionalQuestionnaire(TypedDict, total=False):
    # Are there any current known issues with your services or product?
    knownIssues: typing.Optional[str]

    # Description of known issues (if yes)
    knownIssuesDescription: typing.Optional[str]

    # Were there any major issues in your company connected to your services/ products (like third party liability or any bigger lawsuits)?
    majorIssues: typing.Optional[str]

    # Description of major issues (if yes)
    majorIssuesDescription: typing.Optional[str]

    # Did you undergo any financial restructuring or financial recovery (or do you plan any in the foreseeable future)?
    financialRecovery: typing.Optional[str]

    # Description of financial recovery (if yes)
    financialRecoveryDescription: typing.Optional[str]

    # How long is your current management team active in this role in the company?
    optionTeam: typing.Optional[str]

    # Is your company subject of an external audit?
    optionAudit: typing.Optional[str]

    # How much of your revenue is related to the top 3 clients?
    optionRevenue: typing.Optional[str]

    # What was the price trend of your services/ products in the last few years?
    optionPrice: typing.Optional[str]

    # What is your market estimation in the next few years?
    marketEstimation: typing.Optional[str]

    # What is your position in the market?
    marketPosition: typing.Optional[str]

    # What are the highest risks for your company in the next three years?
    marketRisk: typing.Optional[str]

    # What are your expectations related to revenue and net profit in the current fiscal year?
    currentRevenue: typing.Optional[str]

    # What are your expectations related to revenue growth in the current fiscal year?
    revenueGrowth: typing.Optional[str]

    # What are your expectations related to the EBITDA margin in the next three years?
    ebitdaMargin: typing.Optional[str]

class Questionnaire(RequiredQuestionnaire, OptionalQuestionnaire):
    pass
