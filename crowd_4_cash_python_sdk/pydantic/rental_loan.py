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


class RentalLoan(BaseModel):
    # Loan Id
    loan_id: typing.Optional[int] = Field(None, alias='loanId')

    # Rentee Id
    rentee_id: typing.Optional[int] = Field(None, alias='renteeId')

    # First name of the rentee
    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='firstName')

    # Last name of the rentee
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='lastName')

    # Date of applicaton
    date_created: typing.Optional[typing.Optional[str]] = Field(None, alias='dateCreated')

    # Date of approval
    date_approved: typing.Optional[typing.Optional[str]] = Field(None, alias='dateApproved')

    # Loan amount total
    loan_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='loanAmount')

    # Interest rate of the loan
    interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='interestRate')

    # Duration in months
    duration: typing.Optional[int] = Field(None, alias='duration')

    # Rating of the loan - AA, A, B, C, D
    loan_rating: typing.Optional[typing.Optional[str]] = Field(None, alias='loanRating')

    # Status of the loan
    loan_status: typing.Optional[typing.Optional[str]] = Field(None, alias='loanStatus')

    # Date of last payment received by the investor
    last_payment_date: typing.Optional[typing.Optional[str]] = Field(None, alias='lastPaymentDate')

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

    # Number of annuities that have been not paid yet.
    number_of_unpaid_annuities: typing.Optional[int] = Field(None, alias='numberOfUnpaidAnnuities')

    # Currently paid principal
    total_repaid_principal: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalRepaidPrincipal')

    # Currently paid interest
    total_repaid_interest: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalRepaidInterest')

    # Date when the loan is paid to borrower
    disbursement_date: typing.Optional[typing.Optional[str]] = Field(None, alias='disbursementDate')

    # Date of the last instalment
    maturity_date: typing.Optional[typing.Optional[str]] = Field(None, alias='maturityDate')

    # Description of the loan purpose
    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    # Web page where loan is desplayed in UI
    link: typing.Optional[typing.Optional[str]] = Field(None, alias='link')
    class Config:
        arbitrary_types_allowed = True
