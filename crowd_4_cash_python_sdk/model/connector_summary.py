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


class ConnectorSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    Connector account details
    """


    class MetaOapg:
        
        class properties:
            
            
            class connectorName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'connectorName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            pendingInvestmentsCount = schemas.Int32Schema
            pendingInvestmentsTotal = schemas.Float64Schema
            activeInvestmentsCount = schemas.Int32Schema
            activeInvestmentsTotal = schemas.Float64Schema
            
            
            class connectedInvestors(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ConnectedInvestor']:
                        return ConnectedInvestor
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'connectedInvestors':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "connectorName": connectorName,
                "pendingInvestmentsCount": pendingInvestmentsCount,
                "pendingInvestmentsTotal": pendingInvestmentsTotal,
                "activeInvestmentsCount": activeInvestmentsCount,
                "activeInvestmentsTotal": activeInvestmentsTotal,
                "connectedInvestors": connectedInvestors,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectorName"]) -> MetaOapg.properties.connectorName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pendingInvestmentsCount"]) -> MetaOapg.properties.pendingInvestmentsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pendingInvestmentsTotal"]) -> MetaOapg.properties.pendingInvestmentsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeInvestmentsCount"]) -> MetaOapg.properties.activeInvestmentsCount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["activeInvestmentsTotal"]) -> MetaOapg.properties.activeInvestmentsTotal: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["connectedInvestors"]) -> MetaOapg.properties.connectedInvestors: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["connectorName", "pendingInvestmentsCount", "pendingInvestmentsTotal", "activeInvestmentsCount", "activeInvestmentsTotal", "connectedInvestors", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectorName"]) -> typing.Union[MetaOapg.properties.connectorName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pendingInvestmentsCount"]) -> typing.Union[MetaOapg.properties.pendingInvestmentsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pendingInvestmentsTotal"]) -> typing.Union[MetaOapg.properties.pendingInvestmentsTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeInvestmentsCount"]) -> typing.Union[MetaOapg.properties.activeInvestmentsCount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["activeInvestmentsTotal"]) -> typing.Union[MetaOapg.properties.activeInvestmentsTotal, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["connectedInvestors"]) -> typing.Union[MetaOapg.properties.connectedInvestors, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["connectorName", "pendingInvestmentsCount", "pendingInvestmentsTotal", "activeInvestmentsCount", "activeInvestmentsTotal", "connectedInvestors", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        connectorName: typing.Union[MetaOapg.properties.connectorName, None, str, schemas.Unset] = schemas.unset,
        pendingInvestmentsCount: typing.Union[MetaOapg.properties.pendingInvestmentsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        pendingInvestmentsTotal: typing.Union[MetaOapg.properties.pendingInvestmentsTotal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        activeInvestmentsCount: typing.Union[MetaOapg.properties.activeInvestmentsCount, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        activeInvestmentsTotal: typing.Union[MetaOapg.properties.activeInvestmentsTotal, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        connectedInvestors: typing.Union[MetaOapg.properties.connectedInvestors, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ConnectorSummary':
        return super().__new__(
            cls,
            *args,
            connectorName=connectorName,
            pendingInvestmentsCount=pendingInvestmentsCount,
            pendingInvestmentsTotal=pendingInvestmentsTotal,
            activeInvestmentsCount=activeInvestmentsCount,
            activeInvestmentsTotal=activeInvestmentsTotal,
            connectedInvestors=connectedInvestors,
            _configuration=_configuration,
            **kwargs,
        )

from crowd_4_cash_python_sdk.model.connected_investor import ConnectedInvestor