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


class ConnectorBid(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A bid that connector places on behalf of connected investors
    """


    class MetaOapg:
        required = {
            "amount",
            "investorId",
            "loanId",
        }
        
        class properties:
            investorId = schemas.Int32Schema
            loanId = schemas.Int32Schema
            amount = schemas.Float64Schema
            __annotations__ = {
                "investorId": investorId,
                "loanId": loanId,
                "amount": amount,
            }
    
    amount: MetaOapg.properties.amount
    investorId: MetaOapg.properties.investorId
    loanId: MetaOapg.properties.loanId
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investorId"]) -> MetaOapg.properties.investorId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanId"]) -> MetaOapg.properties.loanId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["investorId", "loanId", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investorId"]) -> MetaOapg.properties.investorId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanId"]) -> MetaOapg.properties.loanId: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["investorId", "loanId", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, ],
        investorId: typing.Union[MetaOapg.properties.investorId, decimal.Decimal, int, ],
        loanId: typing.Union[MetaOapg.properties.loanId, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectorBid':
        return super().__new__(
            cls,
            *args,
            amount=amount,
            investorId=investorId,
            loanId=loanId,
            _configuration=_configuration,
            **kwargs,
        )
