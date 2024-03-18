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


class RequiredExpenses(TypedDict):
    pass

class OptionalExpenses(TypedDict, total=False):
    # Tax to be paid
    taxAtSource: typing.Union[int, float]

    housingCondition: typing.Optional[str]

    # Residential situation
    residentalSituation: typing.Optional[str]

    # Monthly rental cost
    monthlyRent: typing.Union[int, float]

    # Are the rental costs shared?
    payCostSolely: typing.Optional[str]

    # Part of the rental costs (if shared)
    monthlyCostPortion: typing.Union[int, float]

    # Monthly cost for homeowners
    monthlyMortgage: typing.Union[int, float]

    # Amount of mortgage outstanding
    mortgageAmount: typing.Union[int, float]

    # Are there any other open loans?
    anotherLoan: typing.Optional[str]

    # Name of lender of the outstanding loan
    anotherLoanLender: typing.Optional[str]

    # Amount of the outstanding loan
    anotherLoanAmount: typing.Union[int, float]

    # Interest rate of the outstanding loan
    anotherLoanInterestRate: typing.Union[int, float]

    # Monthly payment of the outstanding loan
    anotherLoanMonthlyPayment: typing.Union[int, float]

    # Cost of insurances on a monthly basis
    insuranceMonthlyCost: typing.Union[int, float]

    # Cost of private transportation on a monthly basis (cost of leasing etc.)
    privateTransportMonthlyCost: typing.Union[int, float]

    # Cost of public transportation on a monthly basis
    publicTransportMonthlyCost: typing.Union[int, float]

    # Are there any dependent children?
    dependentChildren: typing.Optional[str]

    # Number of children younger than ten years?
    childrenYoungerThanTen: int

    # Number of children older than ten years?
    childrenOlderThanTen: int

    # Are there any alimony or external child support
    alimonyOrChildSupport: typing.Optional[str]

    # Amount of alimony or external child support (if yes)
    alimonyOrChildSupportAmount: typing.Union[int, float]

    # Are there any other recurring monthly cost?
    furtherRecurringMonthlyCost: typing.Optional[str]

    # Amount of any other recurruing monthly cost (if yes)
    furtherRecurringMonthlyCost1Amount: typing.Union[int, float]

    # Description of any other recurruing monthly cost (if yes)
    furtherRecurringMonthlyCost1Description: typing.Optional[str]

    # Amount of any other recurruing monthly cost (if yes)
    furtherRecurringMonthlyCost2Amount: typing.Union[int, float]

    # Description of any other recurruing monthly cost (if yes)
    furtherRecurringMonthlyCost2Description: typing.Optional[str]

class Expenses(RequiredExpenses, OptionalExpenses):
    pass
