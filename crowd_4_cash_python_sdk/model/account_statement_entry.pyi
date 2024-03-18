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


class AccountStatementEntry(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Information about the each payment by the borrower
    """


    class MetaOapg:
        
        class properties:
            annuityNumber = schemas.Int32Schema
            
            
            class dueDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dueDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class messageDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'messageDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class matchingDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'matchingDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            amount = schemas.Float64Schema
            __annotations__ = {
                "annuityNumber": annuityNumber,
                "dueDate": dueDate,
                "messageDate": messageDate,
                "matchingDate": matchingDate,
                "amount": amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["annuityNumber"]) -> MetaOapg.properties.annuityNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dueDate"]) -> MetaOapg.properties.dueDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["messageDate"]) -> MetaOapg.properties.messageDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["matchingDate"]) -> MetaOapg.properties.matchingDate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["annuityNumber", "dueDate", "messageDate", "matchingDate", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["annuityNumber"]) -> typing.Union[MetaOapg.properties.annuityNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dueDate"]) -> typing.Union[MetaOapg.properties.dueDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["messageDate"]) -> typing.Union[MetaOapg.properties.messageDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["matchingDate"]) -> typing.Union[MetaOapg.properties.matchingDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["annuityNumber", "dueDate", "messageDate", "matchingDate", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        annuityNumber: typing.Union[MetaOapg.properties.annuityNumber, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dueDate: typing.Union[MetaOapg.properties.dueDate, None, str, schemas.Unset] = schemas.unset,
        messageDate: typing.Union[MetaOapg.properties.messageDate, None, str, schemas.Unset] = schemas.unset,
        matchingDate: typing.Union[MetaOapg.properties.matchingDate, None, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AccountStatementEntry':
        return super().__new__(
            cls,
            *args,
            annuityNumber=annuityNumber,
            dueDate=dueDate,
            messageDate=messageDate,
            matchingDate=matchingDate,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )