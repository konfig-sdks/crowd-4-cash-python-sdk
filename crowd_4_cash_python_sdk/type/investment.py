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

from crowd_4_cash_python_sdk.type.account_statement import AccountStatement
from crowd_4_cash_python_sdk.type.amortization_schedule import AmortizationSchedule
from crowd_4_cash_python_sdk.type.bid import Bid
from crowd_4_cash_python_sdk.type.company import Company
from crowd_4_cash_python_sdk.type.crif import Crif
from crowd_4_cash_python_sdk.type.early_repayment import EarlyRepayment
from crowd_4_cash_python_sdk.type.expenses import Expenses
from crowd_4_cash_python_sdk.type.financial import Financial
from crowd_4_cash_python_sdk.type.income import Income
from crowd_4_cash_python_sdk.type.private import Private
from crowd_4_cash_python_sdk.type.questionnaire import Questionnaire
from crowd_4_cash_python_sdk.type.technical_data import TechnicalData

class RequiredInvestment(TypedDict):
    pass

class OptionalInvestment(TypedDict, total=False):
    # Investment ID - auto-generated
    id: int

    # Date when the loan application is submitted
    dateCreated: typing.Optional[str]

    # Date when the loan is approved
    dateApproved: typing.Optional[str]

    # Loan amount
    loanAmount: typing.Union[int, float]

    # Date of last payment received by the investor
    lastPaymentDate: typing.Optional[str]

    # Interest rate of the loan
    interestRate: typing.Union[int, float]

    # Payment frequency defines how often payments will be made
    paymentFrequency: typing.Optional[str]

    # Duration in months
    duration: int

    # Type of the borrower - Private or SME
    borrowerType: typing.Optional[str]

    # Type of the loan - Private or SME
    biddingType: typing.Optional[str]

    # Loan type - POS loan, Private and SME
    loanType: typing.Optional[str]

    # Purpose of the loan
    loanPurpose: typing.Optional[str]

    # Rating of the loan - AA, A, B, C, D
    loanRating: typing.Optional[str]

    # Status of the loan
    loanStatus: typing.Optional[str]

    # Payment status - performing, late 1 to 15 days, Defaulted
    performanceStatus: typing.Optional[str]

    # Number od days late
    daysLate: int

    # Is loan collaterialized? - Yes, No
    collateral: typing.Optional[str]

    # Collater Type - Real estate, Vehicle, Guarantor, Stock
    collateralType: typing.Optional[str]

    # Is loan insured? - Yes, No
    insurance: typing.Optional[str]

    # Unpaid Principal
    totalPrincipalRemaining: typing.Union[int, float]

    # Currently paid principal
    totalRepaidPrincipal: typing.Union[int, float]

    # Currently paid interest
    totalRepaidInterest: typing.Union[int, float]

    # End date of the project
    biddingEnd: typing.Optional[str]

    # Date when the bid is placed
    investmentDate: datetime

    # Date when the bid is paid by the investor
    purchaseDate: typing.Optional[str]

    # Date when the loan is paid to borrower
    disbursementDate: datetime

    # Date of the last instalment
    maturityDate: datetime

    # Share of outstanding Principal held by Fund
    share: typing.Union[int, float]

    # Value Factor
    vFac: typing.Union[int, float]

    # Current Principal Balance according to Vfac
    loanPosition: typing.Union[int, float]

    # Auto Invest Id. It can be null if auto invest is turned off
    autoInvestId: typing.Optional[int]

    # Description of the loan purpose
    notes: typing.Optional[str]

    # Web page where loan is desplayed in UI
    link: typing.Optional[str]

    bid: Bid

    borrowerPrivate: Private

    borrowerCompany: Company

    income: Income

    expense: Expenses

    crif: Crif

    questionnaire: Questionnaire

    financial: Financial

    amortizationSchedule: AmortizationSchedule

    earlyRepayment: EarlyRepayment

    accountStatement: AccountStatement

    technicalData: TechnicalData

class Investment(RequiredInvestment, OptionalInvestment):
    pass
