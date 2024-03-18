import typing_extensions

from crowd_4_cash_python_sdk.apis.tags import TagValues
from crowd_4_cash_python_sdk.apis.tags.application_api import ApplicationApi
from crowd_4_cash_python_sdk.apis.tags.contracts_api import ContractsApi
from crowd_4_cash_python_sdk.apis.tags.reports_api import ReportsApi
from crowd_4_cash_python_sdk.apis.tags.bidding_api import BiddingApi
from crowd_4_cash_python_sdk.apis.tags.portfolio_api import PortfolioApi
from crowd_4_cash_python_sdk.apis.tags.authentication_api import AuthenticationApi
from crowd_4_cash_python_sdk.apis.tags.opportunities_api import OpportunitiesApi
from crowd_4_cash_python_sdk.apis.tags.loans_api import LoansApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.APPLICATION: ApplicationApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.BIDDING: BiddingApi,
        TagValues.PORTFOLIO: PortfolioApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.OPPORTUNITIES: OpportunitiesApi,
        TagValues.LOANS: LoansApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.APPLICATION: ApplicationApi,
        TagValues.CONTRACTS: ContractsApi,
        TagValues.REPORTS: ReportsApi,
        TagValues.BIDDING: BiddingApi,
        TagValues.PORTFOLIO: PortfolioApi,
        TagValues.AUTHENTICATION: AuthenticationApi,
        TagValues.OPPORTUNITIES: OpportunitiesApi,
        TagValues.LOANS: LoansApi,
    }
)
