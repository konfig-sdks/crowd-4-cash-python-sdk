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


class AccountDetails(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            availableCash = schemas.Float64Schema
            
            
            class availableCashCurrency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'availableCashCurrency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            accountValue = schemas.Float64Schema
            investedAmount = schemas.Float64Schema
            numberOfInvestments = schemas.Int32Schema
            losses = schemas.Float64Schema
            __annotations__ = {
                "availableCash": availableCash,
                "availableCashCurrency": availableCashCurrency,
                "accountValue": accountValue,
                "investedAmount": investedAmount,
                "numberOfInvestments": numberOfInvestments,
                "losses": losses,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableCash"]) -> MetaOapg.properties.availableCash: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["availableCashCurrency"]) -> MetaOapg.properties.availableCashCurrency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["accountValue"]) -> MetaOapg.properties.accountValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investedAmount"]) -> MetaOapg.properties.investedAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfInvestments"]) -> MetaOapg.properties.numberOfInvestments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["losses"]) -> MetaOapg.properties.losses: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["availableCash", "availableCashCurrency", "accountValue", "investedAmount", "numberOfInvestments", "losses", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableCash"]) -> typing.Union[MetaOapg.properties.availableCash, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["availableCashCurrency"]) -> typing.Union[MetaOapg.properties.availableCashCurrency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["accountValue"]) -> typing.Union[MetaOapg.properties.accountValue, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investedAmount"]) -> typing.Union[MetaOapg.properties.investedAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfInvestments"]) -> typing.Union[MetaOapg.properties.numberOfInvestments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["losses"]) -> typing.Union[MetaOapg.properties.losses, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["availableCash", "availableCashCurrency", "accountValue", "investedAmount", "numberOfInvestments", "losses", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        availableCash: typing.Union[MetaOapg.properties.availableCash, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        availableCashCurrency: typing.Union[MetaOapg.properties.availableCashCurrency, None, str, schemas.Unset] = schemas.unset,
        accountValue: typing.Union[MetaOapg.properties.accountValue, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        investedAmount: typing.Union[MetaOapg.properties.investedAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        numberOfInvestments: typing.Union[MetaOapg.properties.numberOfInvestments, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        losses: typing.Union[MetaOapg.properties.losses, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountDetails':
        return super().__new__(
            cls,
            *args,
            availableCash=availableCash,
            availableCashCurrency=availableCashCurrency,
            accountValue=accountValue,
            investedAmount=investedAmount,
            numberOfInvestments=numberOfInvestments,
            losses=losses,
            _configuration=_configuration,
            **kwargs,
        )
