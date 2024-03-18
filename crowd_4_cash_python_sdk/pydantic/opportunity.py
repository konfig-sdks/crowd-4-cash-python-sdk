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

from crowd_4_cash_python_sdk.pydantic.active_bid import ActiveBid
from crowd_4_cash_python_sdk.pydantic.company import Company
from crowd_4_cash_python_sdk.pydantic.expenses import Expenses
from crowd_4_cash_python_sdk.pydantic.financial import Financial
from crowd_4_cash_python_sdk.pydantic.income import Income
from crowd_4_cash_python_sdk.pydantic.private import Private
from crowd_4_cash_python_sdk.pydantic.questionnaire import Questionnaire
from crowd_4_cash_python_sdk.pydantic.technical_data import TechnicalData

class Opportunity(BaseModel):
    # Loan ID
    id: typing.Optional[int] = Field(None, alias='id')

    # Date when the loan application has been submitted.
    date_created: typing.Optional[typing.Optional[str]] = Field(None, alias='dateCreated')

    # Date when the loan application has been reviewed and approved.
    date_approved: typing.Optional[typing.Optional[str]] = Field(None, alias='dateApproved')

    # An amount the borrower promises to repay
    loan_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanAmount')

    # Interest rate in %
    interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestRate')

    # Payment frequency defines how often payments will be made
    payment_frequency: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentFrequency')

    # Duration in months
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Borrower Type (Private or SME)
    borrower_type: typing.Optional[typing.Optional[str]] = Field(None, alias='borrowerType')

    # Loan type
    bidding_type: typing.Optional[typing.Optional[str]] = Field(None, alias='biddingType')

    # Loan type e.g. POS loan, Private or SME
    loan_type: typing.Optional[typing.Optional[str]] = Field(None, alias='loanType')

    # Loan purpose category e.g. Education, Furnishing, Vehicle purchase, Wedding, Taxes, Refinancing etc.
    loan_purpose: typing.Optional[typing.Optional[str]] = Field(None, alias='loanPurpose')

    # Crowd4Cash Rating
    loan_rating: typing.Optional[typing.Optional[str]] = Field(None, alias='loanRating')

    # Loan status e.g. In funding, Funded, Active, Closed, Defaulted etc.
    loan_status: typing.Optional[typing.Optional[str]] = Field(None, alias='loanStatus')

    # Payment status e.g. Performing, Late 1 to 15 days, Late 16 to 30 days, Late more than 120 days, Defaulted, Cancelled, Finished prematurely, Paid off, etc.
    performance_status: typing.Optional[typing.Optional[str]] = Field(None, alias='performanceStatus')

    # Is oan collaterialized?
    collateral: typing.Optional[typing.Optional[str]] = Field(None, alias='collateral')

    # Collater Type - Real estate, Vehicle, Guarantor, Stock
    collateral_type: typing.Optional[typing.Optional[str]] = Field(None, alias='collateralType')

    # Is loan insured?
    insurance: typing.Optional[typing.Optional[str]] = Field(None, alias='insurance')

    # An amount that is not funded yet
    open_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='openAmount')

    # End date of the project
    bidding_end: typing.Optional[typing.Optional[str]] = Field(None, alias='biddingEnd')

    # Description of the loan purpose
    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    # Web page where loan is displayed in UI
    link: typing.Optional[typing.Optional[str]] = Field(None, alias='link')

    borrower_private: typing.Optional[Private] = Field(None, alias='borrowerPrivate')

    borrower_company: typing.Optional[Company] = Field(None, alias='borrowerCompany')

    income: typing.Optional[Income] = Field(None, alias='income')

    expenses: typing.Optional[Expenses] = Field(None, alias='expenses')

    questionnaire: typing.Optional[Questionnaire] = Field(None, alias='questionnaire')

    financial: typing.Optional[Financial] = Field(None, alias='financial')

    technical_data: typing.Optional[TechnicalData] = Field(None, alias='technicalData')

    bids: typing.Optional[typing.Optional[typing.List[ActiveBid]]] = Field(None, alias='bids')
    class Config:
        arbitrary_types_allowed = True
