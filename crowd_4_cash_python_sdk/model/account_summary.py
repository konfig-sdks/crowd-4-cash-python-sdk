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


class AccountSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            openingBalance = schemas.Float64Schema
            interest = schemas.Float64Schema
            defaultInterest = schemas.Float64Schema
            principal = schemas.Float64Schema
            investments = schemas.Float64Schema
            commission = schemas.Float64Schema
            deposits = schemas.Float64Schema
            withdrawals = schemas.Float64Schema
            closingBalance = schemas.Float64Schema
            __annotations__ = {
                "openingBalance": openingBalance,
                "interest": interest,
                "defaultInterest": defaultInterest,
                "principal": principal,
                "investments": investments,
                "commission": commission,
                "deposits": deposits,
                "withdrawals": withdrawals,
                "closingBalance": closingBalance,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["openingBalance"]) -> MetaOapg.properties.openingBalance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interest"]) -> MetaOapg.properties.interest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["defaultInterest"]) -> MetaOapg.properties.defaultInterest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["principal"]) -> MetaOapg.properties.principal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investments"]) -> MetaOapg.properties.investments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["commission"]) -> MetaOapg.properties.commission: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["deposits"]) -> MetaOapg.properties.deposits: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["withdrawals"]) -> MetaOapg.properties.withdrawals: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["closingBalance"]) -> MetaOapg.properties.closingBalance: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["openingBalance", "interest", "defaultInterest", "principal", "investments", "commission", "deposits", "withdrawals", "closingBalance", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["openingBalance"]) -> typing.Union[MetaOapg.properties.openingBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interest"]) -> typing.Union[MetaOapg.properties.interest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["defaultInterest"]) -> typing.Union[MetaOapg.properties.defaultInterest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["principal"]) -> typing.Union[MetaOapg.properties.principal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investments"]) -> typing.Union[MetaOapg.properties.investments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["commission"]) -> typing.Union[MetaOapg.properties.commission, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["deposits"]) -> typing.Union[MetaOapg.properties.deposits, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["withdrawals"]) -> typing.Union[MetaOapg.properties.withdrawals, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["closingBalance"]) -> typing.Union[MetaOapg.properties.closingBalance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["openingBalance", "interest", "defaultInterest", "principal", "investments", "commission", "deposits", "withdrawals", "closingBalance", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        openingBalance: typing.Union[MetaOapg.properties.openingBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        interest: typing.Union[MetaOapg.properties.interest, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        defaultInterest: typing.Union[MetaOapg.properties.defaultInterest, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        principal: typing.Union[MetaOapg.properties.principal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        investments: typing.Union[MetaOapg.properties.investments, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        commission: typing.Union[MetaOapg.properties.commission, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        deposits: typing.Union[MetaOapg.properties.deposits, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        withdrawals: typing.Union[MetaOapg.properties.withdrawals, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        closingBalance: typing.Union[MetaOapg.properties.closingBalance, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountSummary':
        return super().__new__(
            cls,
            *args,
            openingBalance=openingBalance,
            interest=interest,
            defaultInterest=defaultInterest,
            principal=principal,
            investments=investments,
            commission=commission,
            deposits=deposits,
            withdrawals=withdrawals,
            closingBalance=closingBalance,
            _configuration=_configuration,
            **kwargs,
        )
