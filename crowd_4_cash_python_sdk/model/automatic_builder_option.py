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


class AutomaticBuilderOption(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            id = schemas.Int32Schema
            investmentCurrently = schemas.Float64Schema
            totalAmountForInvestment = schemas.Float64Schema
            
            
            class originators(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'originators':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            interestRateFrom = schemas.Float64Schema
            interestRateTo = schemas.Float64Schema
            maximumPerBid = schemas.Float64Schema
            minimumPerBid = schemas.Float64Schema
            reinvest = schemas.BoolSchema
            
            
            class investmentLevel(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'investmentLevel':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            secondaryMarket = schemas.BoolSchema
            isActive = schemas.BoolSchema
            durationFrom = schemas.Int32Schema
            durationTo = schemas.Int32Schema
            
            
            class currency(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "id": id,
                "investmentCurrently": investmentCurrently,
                "totalAmountForInvestment": totalAmountForInvestment,
                "originators": originators,
                "interestRateFrom": interestRateFrom,
                "interestRateTo": interestRateTo,
                "maximumPerBid": maximumPerBid,
                "minimumPerBid": minimumPerBid,
                "reinvest": reinvest,
                "investmentLevel": investmentLevel,
                "secondaryMarket": secondaryMarket,
                "isActive": isActive,
                "durationFrom": durationFrom,
                "durationTo": durationTo,
                "currency": currency,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investmentCurrently"]) -> MetaOapg.properties.investmentCurrently: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["totalAmountForInvestment"]) -> MetaOapg.properties.totalAmountForInvestment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["originators"]) -> MetaOapg.properties.originators: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interestRateFrom"]) -> MetaOapg.properties.interestRateFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["interestRateTo"]) -> MetaOapg.properties.interestRateTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["maximumPerBid"]) -> MetaOapg.properties.maximumPerBid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["minimumPerBid"]) -> MetaOapg.properties.minimumPerBid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["reinvest"]) -> MetaOapg.properties.reinvest: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["investmentLevel"]) -> MetaOapg.properties.investmentLevel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["secondaryMarket"]) -> MetaOapg.properties.secondaryMarket: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["isActive"]) -> MetaOapg.properties.isActive: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationFrom"]) -> MetaOapg.properties.durationFrom: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["durationTo"]) -> MetaOapg.properties.durationTo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "investmentCurrently", "totalAmountForInvestment", "originators", "interestRateFrom", "interestRateTo", "maximumPerBid", "minimumPerBid", "reinvest", "investmentLevel", "secondaryMarket", "isActive", "durationFrom", "durationTo", "currency", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investmentCurrently"]) -> typing.Union[MetaOapg.properties.investmentCurrently, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["totalAmountForInvestment"]) -> typing.Union[MetaOapg.properties.totalAmountForInvestment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["originators"]) -> typing.Union[MetaOapg.properties.originators, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interestRateFrom"]) -> typing.Union[MetaOapg.properties.interestRateFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["interestRateTo"]) -> typing.Union[MetaOapg.properties.interestRateTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["maximumPerBid"]) -> typing.Union[MetaOapg.properties.maximumPerBid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["minimumPerBid"]) -> typing.Union[MetaOapg.properties.minimumPerBid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["reinvest"]) -> typing.Union[MetaOapg.properties.reinvest, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["investmentLevel"]) -> typing.Union[MetaOapg.properties.investmentLevel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["secondaryMarket"]) -> typing.Union[MetaOapg.properties.secondaryMarket, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["isActive"]) -> typing.Union[MetaOapg.properties.isActive, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationFrom"]) -> typing.Union[MetaOapg.properties.durationFrom, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["durationTo"]) -> typing.Union[MetaOapg.properties.durationTo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "investmentCurrently", "totalAmountForInvestment", "originators", "interestRateFrom", "interestRateTo", "maximumPerBid", "minimumPerBid", "reinvest", "investmentLevel", "secondaryMarket", "isActive", "durationFrom", "durationTo", "currency", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        investmentCurrently: typing.Union[MetaOapg.properties.investmentCurrently, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        totalAmountForInvestment: typing.Union[MetaOapg.properties.totalAmountForInvestment, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        originators: typing.Union[MetaOapg.properties.originators, None, str, schemas.Unset] = schemas.unset,
        interestRateFrom: typing.Union[MetaOapg.properties.interestRateFrom, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        interestRateTo: typing.Union[MetaOapg.properties.interestRateTo, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        maximumPerBid: typing.Union[MetaOapg.properties.maximumPerBid, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        minimumPerBid: typing.Union[MetaOapg.properties.minimumPerBid, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        reinvest: typing.Union[MetaOapg.properties.reinvest, bool, schemas.Unset] = schemas.unset,
        investmentLevel: typing.Union[MetaOapg.properties.investmentLevel, None, str, schemas.Unset] = schemas.unset,
        secondaryMarket: typing.Union[MetaOapg.properties.secondaryMarket, bool, schemas.Unset] = schemas.unset,
        isActive: typing.Union[MetaOapg.properties.isActive, bool, schemas.Unset] = schemas.unset,
        durationFrom: typing.Union[MetaOapg.properties.durationFrom, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        durationTo: typing.Union[MetaOapg.properties.durationTo, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AutomaticBuilderOption':
        return super().__new__(
            cls,
            *args,
            id=id,
            investmentCurrently=investmentCurrently,
            totalAmountForInvestment=totalAmountForInvestment,
            originators=originators,
            interestRateFrom=interestRateFrom,
            interestRateTo=interestRateTo,
            maximumPerBid=maximumPerBid,
            minimumPerBid=minimumPerBid,
            reinvest=reinvest,
            investmentLevel=investmentLevel,
            secondaryMarket=secondaryMarket,
            isActive=isActive,
            durationFrom=durationFrom,
            durationTo=durationTo,
            currency=currency,
            _configuration=_configuration,
            **kwargs,
        )
