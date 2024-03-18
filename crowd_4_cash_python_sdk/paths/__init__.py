# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from crowd_4_cash_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    AUTHENTICATE = "/Authenticate"
    LOAN = "/Loan"
    INTERMEDIARY_LOAN = "/IntermediaryLoan"
    RENTAL_LOAN = "/RentalLoan"
    OPPORTUNITIES = "/Opportunities"
    BID = "/Bid"
    BIDS = "/Bids"
    CONTRACTS = "/Contracts"
    CONTRACTS_LOAN_ID = "/Contracts/{loanId}"
    CONTRACTS_PARTNER_ID_LOAN_ID = "/Contracts/{partnerId}/{loanId}"
    CONTRACTS_RENTAL_LOAN_LOAN_ID = "/Contracts/RentalLoan/{loanId}"
    PORTFOLIO = "/Portfolio"
    CUSTOM_PORTFOLIO = "/CustomPortfolio"
    CONNECTOR = "/Connector"
    INTERMEDIARY = "/Intermediary"
    RENTAL = "/Rental"
    LOANS = "/Loans"
