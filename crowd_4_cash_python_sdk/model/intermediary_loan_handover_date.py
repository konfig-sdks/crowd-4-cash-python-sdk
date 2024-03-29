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


class IntermediaryLoanHandoverDate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Handover Date Update
    """


    class MetaOapg:
        
        class properties:
            loanId = schemas.Int32Schema
            
            
            class handoverDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'handoverDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "loanId": loanId,
                "handoverDate": handoverDate,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loanId"]) -> MetaOapg.properties.loanId: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["handoverDate"]) -> MetaOapg.properties.handoverDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["loanId", "handoverDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loanId"]) -> typing.Union[MetaOapg.properties.loanId, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["handoverDate"]) -> typing.Union[MetaOapg.properties.handoverDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["loanId", "handoverDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        loanId: typing.Union[MetaOapg.properties.loanId, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        handoverDate: typing.Union[MetaOapg.properties.handoverDate, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntermediaryLoanHandoverDate':
        return super().__new__(
            cls,
            *args,
            loanId=loanId,
            handoverDate=handoverDate,
            _configuration=_configuration,
            **kwargs,
        )
