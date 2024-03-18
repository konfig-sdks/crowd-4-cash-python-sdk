# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from crowd_4_cash_python_sdk.paths.contracts.get import GetAll
from crowd_4_cash_python_sdk.paths.contracts_rental_loan_loan_id.get import GetLoanContract
from crowd_4_cash_python_sdk.paths.contracts_loan_id.get import GetSpecific
from crowd_4_cash_python_sdk.paths.contracts_partner_id_loan_id.get import GetSpecificIntermediaryLoanContract
from crowd_4_cash_python_sdk.apis.tags.contracts_api_raw import ContractsApiRaw


class ContractsApi(
    GetAll,
    GetLoanContract,
    GetSpecific,
    GetSpecificIntermediaryLoanContract,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: ContractsApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = ContractsApiRaw(api_client)