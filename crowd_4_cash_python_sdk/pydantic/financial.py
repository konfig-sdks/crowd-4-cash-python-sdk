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


class Financial(BaseModel):
    # Liquid funds at the end of Year 1
    liquid_funds__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='liquidFunds_Year1')

    # Liquid funds at the end of Year 2
    liquid_funds__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='liquidFunds_Year2')

    # Accounts receivable at the end of Year 1
    accounts_receivable__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountsReceivable_Year1')

    # Accounts receivable at the end of Year 2
    accounts_receivable__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountsReceivable_Year2')

    # Stocks at the end of Year 1
    stocks__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='stocks_Year1')

    # Stocks at the end of Year 2
    stocks__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='stocks_Year2')

    # Other current assets at the end of Year 1
    current_assets__other__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentAssets_Other_Year1')

    # Other current assets at the end of Year 2
    current_assets__other__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentAssets_Other_Year2')

    # Total current assets at the end of Year 1
    current_assets__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentAssets_Year1_SUM')

    # Total current assets at the end of Year 2
    current_assets__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='currentAssets_Year2_SUM')

    # Machines and systems at the end of Year 1
    machines_and_systems__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='machinesAndSystems_Year1')

    # Machines and systems at the end of Year 2
    machines_and_systems__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='machinesAndSystems_Year2')

    # Facilities and vehicle at the end of Year 1
    facilities_and_vehicle_park__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='facilitiesAndVehiclePark_Year1')

    # Facilities and vehicle at the end of Year 2
    facilities_and_vehicle_park__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='facilitiesAndVehiclePark_Year2')

    # Other fixed assets at the end of Year 1
    fixed_assets__other__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='fixedAssets_Other_Year1')

    # Other fixed assets at the end of Year 2
    fixed_assets__other__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='fixedAssets_Other_Year2')

    # Total fixed assets at the end of Year 1
    fixed_assets__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='fixedAssets_Year1_SUM')

    # Total fixed assets at the end of Year 2
    fixed_assets__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='fixedAssets_Year2_SUM')

    # Accounts payable at the end of Year 1
    accounts_payable__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountsPayable_Year1')

    # Accounts payable at the end of Year 2
    accounts_payable__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='accountsPayable_Year2')

    # Total assets at the end of Year 1
    total_assets__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAssets_Year1')

    # Total assets at the end of Year 2
    total_assets__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalAssets_Year2')

    # Short term loans at the end of Year 1
    short_term_loans__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='shortTermLoans_Year1')

    # Short term loans at the end of Year 2
    short_term_loans__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='shortTermLoans_Year2')

    # Other current liabilities at the end of Year 1
    curent_liabilities__other__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='curentLiabilities_Other_Year1')

    # Other current liabilities at the end of Year 2
    curent_liabilities__other__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='curentLiabilities_Other_Year2')

    # Total current liabilities at the end of Year 1
    curent_liabilities__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='curentLiabilities_Year1_SUM')

    # Total current liabilities at the end of Year 2
    curent_liabilities__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='curentLiabilities_Year2_SUM')

    # Long term loans at the end of Year 1
    long_term_loans__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLoans_Year1')

    # Long term loans at the end of Year 2
    long_term_loans__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLoans_Year2')

    # Accruals at the end of Year 1
    accruals__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='accruals_Year1')

    # Accruals at the end of Year 2
    accruals__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='accruals_Year2')

    # Other long term laiabilities at the end of Year 1
    long_term_liabilities__other__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLiabilities_Other_Year1')

    # Other long term laiabilities at the end of Year 2
    long_term_liabilities__other__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLiabilities_Other_Year2')

    # Total long term laiabilities at the end of Year 1
    long_term_liabilities__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLiabilities_Year1_SUM')

    # Total long term laiabilities at the end of Year 2
    long_term_liabilities__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='longTermLiabilities_Year2_SUM')

    # Equity at the end of Year 1
    equity__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='equity_Year1')

    # Equity at the end of Year 2
    equity__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='equity_Year2')

    # Total laiabilitie at the end of Year 1
    total_liabilities__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalLiabilities_Year1_SUM')

    # Total laiabilitie at the end of Year 2
    total_liabilities__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='totalLiabilities_Year2_SUM')

    # Sales Year 1
    sales_proceeds__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='salesProceeds_Year1')

    # Sales Year 2
    sales_proceeds__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='salesProceeds_Year2')

    # Cost of goods Year 1
    cost_of_goods__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='costOfGoods_Year1')

    # Cost of goods Year 2
    cost_of_goods__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='costOfGoods_Year2')

    # Gross profit Year 1
    gross_profit__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossProfit_Year1_SUM')

    # Gross profit Year 2
    gross_profit__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='grossProfit_Year2_SUM')

    # Operating expenses Year 1
    operating_expenses__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='operatingExpenses_Year1')

    # Operating expenses Year 2
    operating_expenses__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='operatingExpenses_Year2')

    # Ebidta Year 1
    ebidta__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='ebidta_Year1_SUM')

    # Ebidta Year 2
    ebidta__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='ebidta_Year2_SUM')

    # Depreciation Year 1
    depreciation__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='depreciation_Year1')

    # Depreciation Year 2
    depreciation__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='depreciation_Year2')

    # Ebit Year 1
    ebit__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='ebit_Year1_SUM')

    # Ebit Year 2
    ebit__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='ebit_Year2_SUM')

    # Financial expenses Year 1
    financial_expenses__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='financialExpenses_Year1')

    # Financial expenses Year 2
    financial_expenses__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='financialExpenses_Year2')

    # Net income before tax Year 1
    net_income_before_taxes__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='netIncomeBeforeTaxes_Year1_SUM')

    # Net income before tax Year 2
    net_income_before_taxes__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='netIncomeBeforeTaxes_Year2_SUM')

    # Income taxes Year 1
    income_taxes__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='incomeTaxes_Year1')

    # Income taxes Year 2
    income_taxes__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='incomeTaxes_Year2')

    # Net profit Year 1
    net_profit__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='netProfit_Year1_SUM')

    # Net profit Year 2
    net_profit__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='netProfit_Year2_SUM')

    # Financials at the beginning of Year 1
    beginning_of_year_financials__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='beginningOfYearFinancials_Year1')

    # Financials at the beginning of Year 2
    beginning_of_year_financials__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='beginningOfYearFinancials_Year2')

    # Cash flow of operating activities Year 1
    cash_flow_operating__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowOperating_Year1')

    # Cash flow of operating activities Year 2
    cash_flow_operating__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowOperating_Year2')

    # Cash flow of investing activities Year 1
    cash_flow_investing__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowInvesting_Year1')

    # Cash flow of investing activities Year 2
    cash_flow_investing__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowInvesting_Year2')

    # Cash flow of finansing activities Year 1
    cash_flow_financing__year1: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowFinancing_Year1')

    # Cash flow of finansing activities Year 2
    cash_flow_financing__year2: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlowFinancing_Year2')

    # Total cash flow Year 1
    cash_flow__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlow_Year1_SUM')

    # Total cash flow Year 2
    cash_flow__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='cashFlow_Year2_SUM')

    # Financials at the end of Year 1
    end_of_year_financials__year1__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='endOfYearFinancials_Year1_SUM')

    # Financials at the end of Year 2
    end_of_year_financials__year2__s_u_m: typing.Optional[typing.Union[int, float]] = Field(None, alias='endOfYearFinancials_Year2_SUM')
    class Config:
        arbitrary_types_allowed = True
