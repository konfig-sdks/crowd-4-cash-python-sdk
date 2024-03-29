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


class IntermediarySummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A rental company like Carify which rents user and new cars
    """


    class MetaOapg:
        
        class properties:
            
            
            class intermediaryName(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'intermediaryName':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            numberOfPartners = schemas.Int32Schema
            numberOfLoans = schemas.Int32Schema
            loansTotalAmount = schemas.Float64Schema
            
            
            class partners(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IntermediaryPartner']:
                        return IntermediaryPartner
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'partners':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class loans(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['IntermediaryLoan']:
                        return IntermediaryLoan
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'loans':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "intermediaryName": intermediaryName,
                "numberOfPartners": numberOfPartners,
                "numberOfLoans": numberOfLoans,
                "loansTotalAmount": loansTotalAmount,
                "partners": partners,
                "loans": loans,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["intermediaryName"]) -> MetaOapg.properties.intermediaryName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfPartners"]) -> MetaOapg.properties.numberOfPartners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["numberOfLoans"]) -> MetaOapg.properties.numberOfLoans: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loansTotalAmount"]) -> MetaOapg.properties.loansTotalAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["partners"]) -> MetaOapg.properties.partners: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["loans"]) -> MetaOapg.properties.loans: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["intermediaryName", "numberOfPartners", "numberOfLoans", "loansTotalAmount", "partners", "loans", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["intermediaryName"]) -> typing.Union[MetaOapg.properties.intermediaryName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfPartners"]) -> typing.Union[MetaOapg.properties.numberOfPartners, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["numberOfLoans"]) -> typing.Union[MetaOapg.properties.numberOfLoans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loansTotalAmount"]) -> typing.Union[MetaOapg.properties.loansTotalAmount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["partners"]) -> typing.Union[MetaOapg.properties.partners, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["loans"]) -> typing.Union[MetaOapg.properties.loans, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["intermediaryName", "numberOfPartners", "numberOfLoans", "loansTotalAmount", "partners", "loans", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        intermediaryName: typing.Union[MetaOapg.properties.intermediaryName, None, str, schemas.Unset] = schemas.unset,
        numberOfPartners: typing.Union[MetaOapg.properties.numberOfPartners, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        numberOfLoans: typing.Union[MetaOapg.properties.numberOfLoans, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        loansTotalAmount: typing.Union[MetaOapg.properties.loansTotalAmount, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        partners: typing.Union[MetaOapg.properties.partners, list, tuple, None, schemas.Unset] = schemas.unset,
        loans: typing.Union[MetaOapg.properties.loans, list, tuple, None, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'IntermediarySummary':
        return super().__new__(
            cls,
            *args,
            intermediaryName=intermediaryName,
            numberOfPartners=numberOfPartners,
            numberOfLoans=numberOfLoans,
            loansTotalAmount=loansTotalAmount,
            partners=partners,
            loans=loans,
            _configuration=_configuration,
            **kwargs,
        )

from crowd_4_cash_python_sdk.model.intermediary_loan import IntermediaryLoan
from crowd_4_cash_python_sdk.model.intermediary_partner import IntermediaryPartner
