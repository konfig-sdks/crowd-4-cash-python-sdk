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


class Questionnaire(BaseModel):
    # Are there any current known issues with your services or product?
    known_issues: typing.Optional[typing.Optional[str]] = Field(None, alias='knownIssues')

    # Description of known issues (if yes)
    known_issues_description: typing.Optional[typing.Optional[str]] = Field(None, alias='knownIssuesDescription')

    # Were there any major issues in your company connected to your services/ products (like third party liability or any bigger lawsuits)?
    major_issues: typing.Optional[typing.Optional[str]] = Field(None, alias='majorIssues')

    # Description of major issues (if yes)
    major_issues_description: typing.Optional[typing.Optional[str]] = Field(None, alias='majorIssuesDescription')

    # Did you undergo any financial restructuring or financial recovery (or do you plan any in the foreseeable future)?
    financial_recovery: typing.Optional[typing.Optional[str]] = Field(None, alias='financialRecovery')

    # Description of financial recovery (if yes)
    financial_recovery_description: typing.Optional[typing.Optional[str]] = Field(None, alias='financialRecoveryDescription')

    # How long is your current management team active in this role in the company?
    option_team: typing.Optional[typing.Optional[str]] = Field(None, alias='optionTeam')

    # Is your company subject of an external audit?
    option_audit: typing.Optional[typing.Optional[str]] = Field(None, alias='optionAudit')

    # How much of your revenue is related to the top 3 clients?
    option_revenue: typing.Optional[typing.Optional[str]] = Field(None, alias='optionRevenue')

    # What was the price trend of your services/ products in the last few years?
    option_price: typing.Optional[typing.Optional[str]] = Field(None, alias='optionPrice')

    # What is your market estimation in the next few years?
    market_estimation: typing.Optional[typing.Optional[str]] = Field(None, alias='marketEstimation')

    # What is your position in the market?
    market_position: typing.Optional[typing.Optional[str]] = Field(None, alias='marketPosition')

    # What are the highest risks for your company in the next three years?
    market_risk: typing.Optional[typing.Optional[str]] = Field(None, alias='marketRisk')

    # What are your expectations related to revenue and net profit in the current fiscal year?
    current_revenue: typing.Optional[typing.Optional[str]] = Field(None, alias='currentRevenue')

    # What are your expectations related to revenue growth in the current fiscal year?
    revenue_growth: typing.Optional[typing.Optional[str]] = Field(None, alias='revenueGrowth')

    # What are your expectations related to the EBITDA margin in the next three years?
    ebitda_margin: typing.Optional[typing.Optional[str]] = Field(None, alias='ebitdaMargin')
    class Config:
        arbitrary_types_allowed = True
