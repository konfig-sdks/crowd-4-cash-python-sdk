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


class ActiveBid(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Offers made by the other investors
    """


    class MetaOapg:
        
        class properties:
            
            
            class pseudonym(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pseudonym':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class dateCreated(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dateCreated':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            amount = schemas.Float64Schema
            __annotations__ = {
                "pseudonym": pseudonym,
                "dateCreated": dateCreated,
                "amount": amount,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pseudonym"]) -> MetaOapg.properties.pseudonym: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateCreated"]) -> MetaOapg.properties.dateCreated: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["pseudonym", "dateCreated", "amount", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pseudonym"]) -> typing.Union[MetaOapg.properties.pseudonym, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateCreated"]) -> typing.Union[MetaOapg.properties.dateCreated, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["pseudonym", "dateCreated", "amount", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        pseudonym: typing.Union[MetaOapg.properties.pseudonym, None, str, schemas.Unset] = schemas.unset,
        dateCreated: typing.Union[MetaOapg.properties.dateCreated, None, str, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ActiveBid':
        return super().__new__(
            cls,
            *args,
            pseudonym=pseudonym,
            dateCreated=dateCreated,
            amount=amount,
            _configuration=_configuration,
            **kwargs,
        )
