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

from crowd_4_cash_python_sdk.type.intermediary_loan import IntermediaryLoan
from crowd_4_cash_python_sdk.type.intermediary_partner import IntermediaryPartner

class RequiredIntermediarySummary(TypedDict):
    pass

class OptionalIntermediarySummary(TypedDict, total=False):
    # Name of the intermediary company
    intermediaryName: typing.Optional[str]

    # Number of partners aka garages
    numberOfPartners: int

    # Number of loan applications
    numberOfLoans: int

    # A sum of all partner loans
    loansTotalAmount: typing.Union[int, float]

    # List of your partners (garages/shops/stores)
    partners: typing.Optional[typing.List[IntermediaryPartner]]

    # List of your partner loan(s)
    loans: typing.Optional[typing.List[IntermediaryLoan]]

class IntermediarySummary(RequiredIntermediarySummary, OptionalIntermediarySummary):
    pass
