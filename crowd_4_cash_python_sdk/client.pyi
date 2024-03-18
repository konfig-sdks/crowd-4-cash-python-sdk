# coding: utf-8
"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

import typing
import inspect
from datetime import date, datetime
from crowd_4_cash_python_sdk.client_custom import ClientCustom
from crowd_4_cash_python_sdk.configuration import Configuration
from crowd_4_cash_python_sdk.api_client import ApiClient
from crowd_4_cash_python_sdk.type_util import copy_signature
from crowd_4_cash_python_sdk.apis.tags.application_api import ApplicationApi
from crowd_4_cash_python_sdk.apis.tags.authentication_api import AuthenticationApi
from crowd_4_cash_python_sdk.apis.tags.bidding_api import BiddingApi
from crowd_4_cash_python_sdk.apis.tags.contracts_api import ContractsApi
from crowd_4_cash_python_sdk.apis.tags.loans_api import LoansApi
from crowd_4_cash_python_sdk.apis.tags.opportunities_api import OpportunitiesApi
from crowd_4_cash_python_sdk.apis.tags.portfolio_api import PortfolioApi
from crowd_4_cash_python_sdk.apis.tags.reports_api import ReportsApi



class Crowd4Cash(ClientCustom):

    def __init__(self, configuration: typing.Union[Configuration, None] = None, **kwargs):
        super().__init__(configuration, **kwargs)
        if (len(kwargs) > 0):
            configuration = Configuration(**kwargs)
        if (configuration is None):
            raise Exception("configuration is required")
        api_client = ApiClient(configuration)
        self.application: ApplicationApi = ApplicationApi(api_client)
        self.authentication: AuthenticationApi = AuthenticationApi(api_client)
        self.bidding: BiddingApi = BiddingApi(api_client)
        self.contracts: ContractsApi = ContractsApi(api_client)
        self.loans: LoansApi = LoansApi(api_client)
        self.opportunities: OpportunitiesApi = OpportunitiesApi(api_client)
        self.portfolio: PortfolioApi = PortfolioApi(api_client)
        self.reports: ReportsApi = ReportsApi(api_client)
