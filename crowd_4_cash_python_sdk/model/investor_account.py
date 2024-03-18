# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from crowd_4_cash_python_sdk import schemas  # noqa: F401


class InvestorAccount(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Investor account details and settings
    """


    class MetaOapg:
        
        class properties:
        
            @staticmethod
            def accountSummary() -> typing.Type['AccountSummary']:
                return AccountSummary
            
            
            class transactions(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Transacions']:
                        return Transacions
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'transactions':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def accountDetails() -> typing.Type['AccountDetails']:
                return AccountDetails
        
            @staticmethod
            def autoInvestSettings() -> typing.Type['AutoInvestSettings']:
                return AutoInvestSettings
            __annotations__ = {
                "accountSummary": accountSummary,
                "transactions": transactions,
                "accountDetails": accountDetails,
                "autoInvestSettings": autoInvestSettings,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountSummary"]) -> 'AccountSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["transactions"]) -> MetaOapg.properties.transactions: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountDetails"]) -> 'AccountDetails': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["autoInvestSettings"]) -> 'AutoInvestSettings': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["accountSummary", "transactions", "accountDetails", "autoInvestSettings", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountSummary"]) -> typing.Union['AccountSummary', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["transactions"]) -> typing.Union[MetaOapg.properties.transactions, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountDetails"]) -> typing.Union['AccountDetails', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["autoInvestSettings"]) -> typing.Union['AutoInvestSettings', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["accountSummary", "transactions", "accountDetails", "autoInvestSettings", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        accountSummary: typing.Union['AccountSummary', schemas.Unset] = schemas.unset,
        transactions: typing.Union[MetaOapg.properties.transactions, list, tuple, None, schemas.Unset] = schemas.unset,
        accountDetails: typing.Union['AccountDetails', schemas.Unset] = schemas.unset,
        autoInvestSettings: typing.Union['AutoInvestSettings', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'InvestorAccount':
        return super().__new__(
            cls,
            *args,
            accountSummary=accountSummary,
            transactions=transactions,
            accountDetails=accountDetails,
            autoInvestSettings=autoInvestSettings,
            _configuration=_configuration,
            **kwargs,
        )

from crowd_4_cash_python_sdk.model.account_details import AccountDetails
from crowd_4_cash_python_sdk.model.account_summary import AccountSummary
from crowd_4_cash_python_sdk.model.auto_invest_settings import AutoInvestSettings
from crowd_4_cash_python_sdk.model.transacions import Transacions