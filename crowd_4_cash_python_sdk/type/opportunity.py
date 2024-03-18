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

from crowd_4_cash_python_sdk.type.active_bid import ActiveBid
from crowd_4_cash_python_sdk.type.company import Company
from crowd_4_cash_python_sdk.type.expenses import Expenses
from crowd_4_cash_python_sdk.type.financial import Financial
from crowd_4_cash_python_sdk.type.income import Income
from crowd_4_cash_python_sdk.type.private import Private
from crowd_4_cash_python_sdk.type.questionnaire import Questionnaire
from crowd_4_cash_python_sdk.type.technical_data import TechnicalData

class RequiredOpportunity(TypedDict):
    pass

class OptionalOpportunity(TypedDict, total=False):
    # Loan ID
    id: int

    # Date when the loan application has been submitted.
    dateCreated: typing.Optional[str]

    # Date when the loan application has been reviewed and approved.
    dateApproved: typing.Optional[str]

    # An amount the borrower promises to repay
    loanAmount: typing.Union[int, float]

    # Interest rate in %
    interestRate: typing.Union[int, float]

    # Payment frequency defines how often payments will be made
    paymentFrequency: typing.Optional[str]

    # Duration in months
    duration: int

    # Borrower Type (Private or SME)
    borrowerType: typing.Optional[str]

    # Loan type
    biddingType: typing.Optional[str]

    # Loan type e.g. POS loan, Private or SME
    loanType: typing.Optional[str]

    # Loan purpose category e.g. Education, Furnishing, Vehicle purchase, Wedding, Taxes, Refinancing etc.
    loanPurpose: typing.Optional[str]

    # Crowd4Cash Rating
    loanRating: typing.Optional[str]

    # Loan status e.g. In funding, Funded, Active, Closed, Defaulted etc.
    loanStatus: typing.Optional[str]

    # Payment status e.g. Performing, Late 1 to 15 days, Late 16 to 30 days, Late more than 120 days, Defaulted, Cancelled, Finished prematurely, Paid off, etc.
    performanceStatus: typing.Optional[str]

    # Is oan collaterialized?
    collateral: typing.Optional[str]

    # Collater Type - Real estate, Vehicle, Guarantor, Stock
    collateralType: typing.Optional[str]

    # Is loan insured?
    insurance: typing.Optional[str]

    # An amount that is not funded yet
    openAmount: typing.Union[int, float]

    # End date of the project
    biddingEnd: typing.Optional[str]

    # Description of the loan purpose
    notes: typing.Optional[str]

    # Web page where loan is displayed in UI
    link: typing.Optional[str]

    borrowerPrivate: Private

    borrowerCompany: Company

    income: Income

    expenses: Expenses

    questionnaire: Questionnaire

    financial: Financial

    technicalData: TechnicalData

    bids: typing.Optional[typing.List[ActiveBid]]

class Opportunity(RequiredOpportunity, OptionalOpportunity):
    pass
