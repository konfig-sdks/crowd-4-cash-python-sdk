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


class RequiredIntermediaryLoan(TypedDict):
    pass

class OptionalIntermediaryLoan(TypedDict, total=False):
    # Loan Id
    loanId: int

    # Partner Id
    partnerId: int

    # Name of the partner
    partnerName: typing.Optional[str]

    # Date of applicaton
    dateCreated: typing.Optional[str]

    # Date of approval
    dateApproved: typing.Optional[str]

    # Loan amount total
    loanAmount: typing.Union[int, float]

    # Interest rate of the loan
    interestRate: typing.Union[int, float]

    # Duration in months
    duration: int

    # Rating of the loan - AA, A, B, C, D
    loanRating: typing.Optional[str]

    # Status of the loan
    loanStatus: typing.Optional[str]

    # Date of last payment received by the investor
    lastPaymentDate: typing.Optional[str]

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

    # Number of annuities that have been not paid yet.
    numberOfUnpaidAnnuities: int

    # Currently paid principal
    totalRepaidPrincipal: typing.Union[int, float]

    # Currently paid interest
    totalRepaidInterest: typing.Union[int, float]

    # Date when the loan is paid to borrower
    disbursementDate: typing.Optional[str]

    # Date of the last instalment
    maturityDate: typing.Optional[str]

    # Description of the loan purpose
    notes: typing.Optional[str]

    # Web page where loan is desplayed in UI
    link: typing.Optional[str]

class IntermediaryLoan(RequiredIntermediaryLoan, OptionalIntermediaryLoan):
    pass
