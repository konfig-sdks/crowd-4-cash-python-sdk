import typing_extensions

from crowd_4_cash_python_sdk.paths import PathValues
from crowd_4_cash_python_sdk.apis.paths.authenticate import Authenticate
from crowd_4_cash_python_sdk.apis.paths.loan import Loan
from crowd_4_cash_python_sdk.apis.paths.intermediary_loan import IntermediaryLoan
from crowd_4_cash_python_sdk.apis.paths.rental_loan import RentalLoan
from crowd_4_cash_python_sdk.apis.paths.opportunities import Opportunities
from crowd_4_cash_python_sdk.apis.paths.bid import Bid
from crowd_4_cash_python_sdk.apis.paths.bids import Bids
from crowd_4_cash_python_sdk.apis.paths.contracts import Contracts
from crowd_4_cash_python_sdk.apis.paths.contracts_loan_id import ContractsLoanId
from crowd_4_cash_python_sdk.apis.paths.contracts_partner_id_loan_id import ContractsPartnerIdLoanId
from crowd_4_cash_python_sdk.apis.paths.contracts_rental_loan_loan_id import ContractsRentalLoanLoanId
from crowd_4_cash_python_sdk.apis.paths.portfolio import Portfolio
from crowd_4_cash_python_sdk.apis.paths.custom_portfolio import CustomPortfolio
from crowd_4_cash_python_sdk.apis.paths.connector import Connector
from crowd_4_cash_python_sdk.apis.paths.intermediary import Intermediary
from crowd_4_cash_python_sdk.apis.paths.rental import Rental
from crowd_4_cash_python_sdk.apis.paths.loans import Loans

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.AUTHENTICATE: Authenticate,
        PathValues.LOAN: Loan,
        PathValues.INTERMEDIARY_LOAN: IntermediaryLoan,
        PathValues.RENTAL_LOAN: RentalLoan,
        PathValues.OPPORTUNITIES: Opportunities,
        PathValues.BID: Bid,
        PathValues.BIDS: Bids,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_LOAN_ID: ContractsLoanId,
        PathValues.CONTRACTS_PARTNER_ID_LOAN_ID: ContractsPartnerIdLoanId,
        PathValues.CONTRACTS_RENTAL_LOAN_LOAN_ID: ContractsRentalLoanLoanId,
        PathValues.PORTFOLIO: Portfolio,
        PathValues.CUSTOM_PORTFOLIO: CustomPortfolio,
        PathValues.CONNECTOR: Connector,
        PathValues.INTERMEDIARY: Intermediary,
        PathValues.RENTAL: Rental,
        PathValues.LOANS: Loans,
    }
)

path_to_api = PathToApi(
    {
        PathValues.AUTHENTICATE: Authenticate,
        PathValues.LOAN: Loan,
        PathValues.INTERMEDIARY_LOAN: IntermediaryLoan,
        PathValues.RENTAL_LOAN: RentalLoan,
        PathValues.OPPORTUNITIES: Opportunities,
        PathValues.BID: Bid,
        PathValues.BIDS: Bids,
        PathValues.CONTRACTS: Contracts,
        PathValues.CONTRACTS_LOAN_ID: ContractsLoanId,
        PathValues.CONTRACTS_PARTNER_ID_LOAN_ID: ContractsPartnerIdLoanId,
        PathValues.CONTRACTS_RENTAL_LOAN_LOAN_ID: ContractsRentalLoanLoanId,
        PathValues.PORTFOLIO: Portfolio,
        PathValues.CUSTOM_PORTFOLIO: CustomPortfolio,
        PathValues.CONNECTOR: Connector,
        PathValues.INTERMEDIARY: Intermediary,
        PathValues.RENTAL: Rental,
        PathValues.LOANS: Loans,
    }
)
