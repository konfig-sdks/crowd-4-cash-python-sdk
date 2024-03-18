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


class Expenses(BaseModel):
    # Tax to be paid
    tax_at_source: typing.Optional[typing.Union[int, float]] = Field(None, alias='taxAtSource')

    housing_condition: typing.Optional[typing.Optional[str]] = Field(None, alias='housingCondition')

    # Residential situation
    residental_situation: typing.Optional[typing.Optional[str]] = Field(None, alias='residentalSituation')

    # Monthly rental cost
    monthly_rent: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyRent')

    # Are the rental costs shared?
    pay_cost_solely: typing.Optional[typing.Optional[str]] = Field(None, alias='payCostSolely')

    # Part of the rental costs (if shared)
    monthly_cost_portion: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyCostPortion')

    # Monthly cost for homeowners
    monthly_mortgage: typing.Optional[typing.Union[int, float]] = Field(None, alias='monthlyMortgage')

    # Amount of mortgage outstanding
    mortgage_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='mortgageAmount')

    # Are there any other open loans?
    another_loan: typing.Optional[typing.Optional[str]] = Field(None, alias='anotherLoan')

    # Name of lender of the outstanding loan
    another_loan_lender: typing.Optional[typing.Optional[str]] = Field(None, alias='anotherLoanLender')

    # Amount of the outstanding loan
    another_loan_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='anotherLoanAmount')

    # Interest rate of the outstanding loan
    another_loan_interest_rate: typing.Optional[typing.Union[int, float]] = Field(None, alias='anotherLoanInterestRate')

    # Monthly payment of the outstanding loan
    another_loan_monthly_payment: typing.Optional[typing.Union[int, float]] = Field(None, alias='anotherLoanMonthlyPayment')

    # Cost of insurances on a monthly basis
    insurance_monthly_cost: typing.Optional[typing.Union[int, float]] = Field(None, alias='insuranceMonthlyCost')

    # Cost of private transportation on a monthly basis (cost of leasing etc.)
    private_transport_monthly_cost: typing.Optional[typing.Union[int, float]] = Field(None, alias='privateTransportMonthlyCost')

    # Cost of public transportation on a monthly basis
    public_transport_monthly_cost: typing.Optional[typing.Union[int, float]] = Field(None, alias='publicTransportMonthlyCost')

    # Are there any dependent children?
    dependent_children: typing.Optional[typing.Optional[str]] = Field(None, alias='dependentChildren')

    # Number of children younger than ten years?
    children_younger_than_ten: typing.Optional[int] = Field(None, alias='childrenYoungerThanTen')

    # Number of children older than ten years?
    children_older_than_ten: typing.Optional[int] = Field(None, alias='childrenOlderThanTen')

    # Are there any alimony or external child support
    alimony_or_child_support: typing.Optional[typing.Optional[str]] = Field(None, alias='alimonyOrChildSupport')

    # Amount of alimony or external child support (if yes)
    alimony_or_child_support_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='alimonyOrChildSupportAmount')

    # Are there any other recurring monthly cost?
    further_recurring_monthly_cost: typing.Optional[typing.Optional[str]] = Field(None, alias='furtherRecurringMonthlyCost')

    # Amount of any other recurruing monthly cost (if yes)
    further_recurring_monthly_cost1_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='furtherRecurringMonthlyCost1Amount')

    # Description of any other recurruing monthly cost (if yes)
    further_recurring_monthly_cost1_description: typing.Optional[typing.Optional[str]] = Field(None, alias='furtherRecurringMonthlyCost1Description')

    # Amount of any other recurruing monthly cost (if yes)
    further_recurring_monthly_cost2_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='furtherRecurringMonthlyCost2Amount')

    # Description of any other recurruing monthly cost (if yes)
    further_recurring_monthly_cost2_description: typing.Optional[typing.Optional[str]] = Field(None, alias='furtherRecurringMonthlyCost2Description')
    class Config:
        arbitrary_types_allowed = True
