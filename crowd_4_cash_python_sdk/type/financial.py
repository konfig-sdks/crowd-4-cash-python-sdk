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


class RequiredFinancial(TypedDict):
    pass

class OptionalFinancial(TypedDict, total=False):
    # Liquid funds at the end of Year 1
    liquidFunds_Year1: typing.Union[int, float]

    # Liquid funds at the end of Year 2
    liquidFunds_Year2: typing.Union[int, float]

    # Accounts receivable at the end of Year 1
    accountsReceivable_Year1: typing.Union[int, float]

    # Accounts receivable at the end of Year 2
    accountsReceivable_Year2: typing.Union[int, float]

    # Stocks at the end of Year 1
    stocks_Year1: typing.Union[int, float]

    # Stocks at the end of Year 2
    stocks_Year2: typing.Union[int, float]

    # Other current assets at the end of Year 1
    currentAssets_Other_Year1: typing.Union[int, float]

    # Other current assets at the end of Year 2
    currentAssets_Other_Year2: typing.Union[int, float]

    # Total current assets at the end of Year 1
    currentAssets_Year1_SUM: typing.Union[int, float]

    # Total current assets at the end of Year 2
    currentAssets_Year2_SUM: typing.Union[int, float]

    # Machines and systems at the end of Year 1
    machinesAndSystems_Year1: typing.Union[int, float]

    # Machines and systems at the end of Year 2
    machinesAndSystems_Year2: typing.Union[int, float]

    # Facilities and vehicle at the end of Year 1
    facilitiesAndVehiclePark_Year1: typing.Union[int, float]

    # Facilities and vehicle at the end of Year 2
    facilitiesAndVehiclePark_Year2: typing.Union[int, float]

    # Other fixed assets at the end of Year 1
    fixedAssets_Other_Year1: typing.Union[int, float]

    # Other fixed assets at the end of Year 2
    fixedAssets_Other_Year2: typing.Union[int, float]

    # Total fixed assets at the end of Year 1
    fixedAssets_Year1_SUM: typing.Union[int, float]

    # Total fixed assets at the end of Year 2
    fixedAssets_Year2_SUM: typing.Union[int, float]

    # Accounts payable at the end of Year 1
    accountsPayable_Year1: typing.Union[int, float]

    # Accounts payable at the end of Year 2
    accountsPayable_Year2: typing.Union[int, float]

    # Total assets at the end of Year 1
    totalAssets_Year1: typing.Union[int, float]

    # Total assets at the end of Year 2
    totalAssets_Year2: typing.Union[int, float]

    # Short term loans at the end of Year 1
    shortTermLoans_Year1: typing.Union[int, float]

    # Short term loans at the end of Year 2
    shortTermLoans_Year2: typing.Union[int, float]

    # Other current liabilities at the end of Year 1
    curentLiabilities_Other_Year1: typing.Union[int, float]

    # Other current liabilities at the end of Year 2
    curentLiabilities_Other_Year2: typing.Union[int, float]

    # Total current liabilities at the end of Year 1
    curentLiabilities_Year1_SUM: typing.Union[int, float]

    # Total current liabilities at the end of Year 2
    curentLiabilities_Year2_SUM: typing.Union[int, float]

    # Long term loans at the end of Year 1
    longTermLoans_Year1: typing.Union[int, float]

    # Long term loans at the end of Year 2
    longTermLoans_Year2: typing.Union[int, float]

    # Accruals at the end of Year 1
    accruals_Year1: typing.Union[int, float]

    # Accruals at the end of Year 2
    accruals_Year2: typing.Union[int, float]

    # Other long term laiabilities at the end of Year 1
    longTermLiabilities_Other_Year1: typing.Union[int, float]

    # Other long term laiabilities at the end of Year 2
    longTermLiabilities_Other_Year2: typing.Union[int, float]

    # Total long term laiabilities at the end of Year 1
    longTermLiabilities_Year1_SUM: typing.Union[int, float]

    # Total long term laiabilities at the end of Year 2
    longTermLiabilities_Year2_SUM: typing.Union[int, float]

    # Equity at the end of Year 1
    equity_Year1: typing.Union[int, float]

    # Equity at the end of Year 2
    equity_Year2: typing.Union[int, float]

    # Total laiabilitie at the end of Year 1
    totalLiabilities_Year1_SUM: typing.Union[int, float]

    # Total laiabilitie at the end of Year 2
    totalLiabilities_Year2_SUM: typing.Union[int, float]

    # Sales Year 1
    salesProceeds_Year1: typing.Union[int, float]

    # Sales Year 2
    salesProceeds_Year2: typing.Union[int, float]

    # Cost of goods Year 1
    costOfGoods_Year1: typing.Union[int, float]

    # Cost of goods Year 2
    costOfGoods_Year2: typing.Union[int, float]

    # Gross profit Year 1
    grossProfit_Year1_SUM: typing.Union[int, float]

    # Gross profit Year 2
    grossProfit_Year2_SUM: typing.Union[int, float]

    # Operating expenses Year 1
    operatingExpenses_Year1: typing.Union[int, float]

    # Operating expenses Year 2
    operatingExpenses_Year2: typing.Union[int, float]

    # Ebidta Year 1
    ebidta_Year1_SUM: typing.Union[int, float]

    # Ebidta Year 2
    ebidta_Year2_SUM: typing.Union[int, float]

    # Depreciation Year 1
    depreciation_Year1: typing.Union[int, float]

    # Depreciation Year 2
    depreciation_Year2: typing.Union[int, float]

    # Ebit Year 1
    ebit_Year1_SUM: typing.Union[int, float]

    # Ebit Year 2
    ebit_Year2_SUM: typing.Union[int, float]

    # Financial expenses Year 1
    financialExpenses_Year1: typing.Union[int, float]

    # Financial expenses Year 2
    financialExpenses_Year2: typing.Union[int, float]

    # Net income before tax Year 1
    netIncomeBeforeTaxes_Year1_SUM: typing.Union[int, float]

    # Net income before tax Year 2
    netIncomeBeforeTaxes_Year2_SUM: typing.Union[int, float]

    # Income taxes Year 1
    incomeTaxes_Year1: typing.Union[int, float]

    # Income taxes Year 2
    incomeTaxes_Year2: typing.Union[int, float]

    # Net profit Year 1
    netProfit_Year1_SUM: typing.Union[int, float]

    # Net profit Year 2
    netProfit_Year2_SUM: typing.Union[int, float]

    # Financials at the beginning of Year 1
    beginningOfYearFinancials_Year1: typing.Union[int, float]

    # Financials at the beginning of Year 2
    beginningOfYearFinancials_Year2: typing.Union[int, float]

    # Cash flow of operating activities Year 1
    cashFlowOperating_Year1: typing.Union[int, float]

    # Cash flow of operating activities Year 2
    cashFlowOperating_Year2: typing.Union[int, float]

    # Cash flow of investing activities Year 1
    cashFlowInvesting_Year1: typing.Union[int, float]

    # Cash flow of investing activities Year 2
    cashFlowInvesting_Year2: typing.Union[int, float]

    # Cash flow of finansing activities Year 1
    cashFlowFinancing_Year1: typing.Union[int, float]

    # Cash flow of finansing activities Year 2
    cashFlowFinancing_Year2: typing.Union[int, float]

    # Total cash flow Year 1
    cashFlow_Year1_SUM: typing.Union[int, float]

    # Total cash flow Year 2
    cashFlow_Year2_SUM: typing.Union[int, float]

    # Financials at the end of Year 1
    endOfYearFinancials_Year1_SUM: typing.Union[int, float]

    # Financials at the end of Year 2
    endOfYearFinancials_Year2_SUM: typing.Union[int, float]

class Financial(RequiredFinancial, OptionalFinancial):
    pass
