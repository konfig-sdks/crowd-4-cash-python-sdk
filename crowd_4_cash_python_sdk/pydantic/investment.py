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

from crowd_4_cash_python_sdk.pydantic.account_statement import AccountStatement
from crowd_4_cash_python_sdk.pydantic.amortization_schedule import AmortizationSchedule
from crowd_4_cash_python_sdk.pydantic.bid import Bid
from crowd_4_cash_python_sdk.pydantic.company import Company
from crowd_4_cash_python_sdk.pydantic.crif import Crif
from crowd_4_cash_python_sdk.pydantic.early_repayment import EarlyRepayment
from crowd_4_cash_python_sdk.pydantic.expenses import Expenses
from crowd_4_cash_python_sdk.pydantic.financial import Financial
from crowd_4_cash_python_sdk.pydantic.income import Income
from crowd_4_cash_python_sdk.pydantic.private import Private
from crowd_4_cash_python_sdk.pydantic.questionnaire import Questionnaire
from crowd_4_cash_python_sdk.pydantic.technical_data import TechnicalData

class Investment(BaseModel):
    # Investment ID - auto-generated
    id: typing.Optional[int] = Field(None, alias='id')

    # Date when the loan application is submitted
    date_created: typing.Optional[typing.Optional[str]] = Field(None, alias='dateCreated')

    # Date when the loan is approved
    date_approved: typing.Optional[typing.Optional[str]] = Field(None, alias='dateApproved')

    # Loan amount
    loan_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanAmount')

    # Date of last payment received by the investor
    last_payment_date: typing.Optional[typing.Optional[str]] = Field(None, alias='lastPaymentDate')

    # Interest rate of the loan
    interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestRate')

    # Payment frequency defines how often payments will be made
    payment_frequency: typing.Optional[typing.Optional[str]] = Field(None, alias='paymentFrequency')

    # Duration in months
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Type of the borrower - Private or SME
    borrower_type: typing.Optional[typing.Optional[str]] = Field(None, alias='borrowerType')

    # Type of the loan - Private or SME
    bidding_type: typing.Optional[typing.Optional[str]] = Field(None, alias='biddingType')

    # Loan type - POS loan, Private and SME
    loan_type: typing.Optional[typing.Optional[str]] = Field(None, alias='loanType')

    # Purpose of the loan
    loan_purpose: typing.Optional[typing.Optional[str]] = Field(None, alias='loanPurpose')

    # Rating of the loan - AA, A, B, C, D
    loan_rating: typing.Optional[typing.Optional[str]] = Field(None, alias='loanRating')

    # Status of the loan
    loan_status: typing.Optional[typing.Optional[str]] = Field(None, alias='loanStatus')

    # Payment status - performing, late 1 to 15 days, Defaulted
    performance_status: typing.Optional[typing.Optional[str]] = Field(None, alias='performanceStatus')

    # Number od days late
    days_late: typing.Optional[int] = Field(None, alias='daysLate')

    # Is loan collaterialized? - Yes, No
    collateral: typing.Optional[typing.Optional[str]] = Field(None, alias='collateral')

    # Collater Type - Real estate, Vehicle, Guarantor, Stock
    collateral_type: typing.Optional[typing.Optional[str]] = Field(None, alias='collateralType')

    # Is loan insured? - Yes, No
    insurance: typing.Optional[typing.Optional[str]] = Field(None, alias='insurance')

    # Unpaid Principal
    total_principal_remaining: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalPrincipalRemaining')

    # Currently paid principal
    total_repaid_principal: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalRepaidPrincipal')

    # Currently paid interest
    total_repaid_interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalRepaidInterest')

    # End date of the project
    bidding_end: typing.Optional[typing.Optional[str]] = Field(None, alias='biddingEnd')

    # Date when the bid is placed
    investment_date: typing.Optional[datetime] = Field(None, alias='investmentDate')

    # Date when the bid is paid by the investor
    purchase_date: typing.Optional[typing.Optional[str]] = Field(None, alias='purchaseDate')

    # Date when the loan is paid to borrower
    disbursement_date: typing.Optional[datetime] = Field(None, alias='disbursementDate')

    # Date of the last instalment
    maturity_date: typing.Optional[datetime] = Field(None, alias='maturityDate')

    # Share of outstanding Principal held by Fund
    share: typing.Optional[typing.Union[int, float]] = Field(None, alias='share')

    # Value Factor
    v_fac: typing.Optional[typing.Union[int, float]] = Field(None, alias='vFac')

    # Current Principal Balance according to Vfac
    loan_position: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanPosition')

    # Auto Invest Id. It can be null if auto invest is turned off
    auto_invest_id: typing.Optional[typing.Optional[int]] = Field(None, alias='autoInvestId')

    # Description of the loan purpose
    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    # Web page where loan is desplayed in UI
    link: typing.Optional[typing.Optional[str]] = Field(None, alias='link')

    bid: typing.Optional[Bid] = Field(None, alias='bid')

    borrower_private: typing.Optional[Private] = Field(None, alias='borrowerPrivate')

    borrower_company: typing.Optional[Company] = Field(None, alias='borrowerCompany')

    income: typing.Optional[Income] = Field(None, alias='income')

    expense: typing.Optional[Expenses] = Field(None, alias='expense')

    crif: typing.Optional[Crif] = Field(None, alias='crif')

    questionnaire: typing.Optional[Questionnaire] = Field(None, alias='questionnaire')

    financial: typing.Optional[Financial] = Field(None, alias='financial')

    amortization_schedule: typing.Optional[AmortizationSchedule] = Field(None, alias='amortizationSchedule')

    early_repayment: typing.Optional[EarlyRepayment] = Field(None, alias='earlyRepayment')

    account_statement: typing.Optional[AccountStatement] = Field(None, alias='accountStatement')

    technical_data: typing.Optional[TechnicalData] = Field(None, alias='technicalData')
    class Config:
        arbitrary_types_allowed = True
