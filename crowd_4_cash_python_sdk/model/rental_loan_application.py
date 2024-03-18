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


class RentalLoanApplication(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)

    A loan application that is submitted by the rental on behalf of their rentee(s)
    """


    class MetaOapg:
        required = {
            "selfieExtension",
            "renteeGender",
            "rentalAmount",
            "renteeLastName",
            "selfiePhoto",
            "contractFileExtension",
            "renteeEmail",
            "contractFile",
            "renteeFirstName",
            "itemName",
            "idBackExtension",
            "idFrontExtension",
            "itemMarketValue",
            "renteeMobilePhoneNumber",
            "idBackPhoto",
            "purchaseItem",
            "idFrontPhoto",
        }
        
        class properties:
            
            
            class renteeGender(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class renteeFirstName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class renteeLastName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class renteeEmail(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class renteeMobilePhoneNumber(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class purchaseItem(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class itemName(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            itemMarketValue = schemas.Float64Schema
            rentalAmount = schemas.Float64Schema
            
            
            class idFrontPhoto(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class idFrontExtension(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class idBackPhoto(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class idBackExtension(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class selfiePhoto(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class selfieExtension(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class contractFile(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class contractFileExtension(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class apiRequester(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'apiRequester':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class renteeBirthdate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'renteeBirthdate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class renteeStreetAddress(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'renteeStreetAddress':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class renteeHouseNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'renteeHouseNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class renteeZipCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'renteeZipCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class renteeCity(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'renteeCity':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class itemStatus(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'itemStatus':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class itemType(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'itemType':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class itemBrand(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'itemBrand':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class itemModel(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'itemModel':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class itemColor(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'itemColor':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class serialNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'serialNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class identificationNumber(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'identificationNumber':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class rentDate(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'rentDate':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "renteeGender": renteeGender,
                "renteeFirstName": renteeFirstName,
                "renteeLastName": renteeLastName,
                "renteeEmail": renteeEmail,
                "renteeMobilePhoneNumber": renteeMobilePhoneNumber,
                "purchaseItem": purchaseItem,
                "itemName": itemName,
                "itemMarketValue": itemMarketValue,
                "rentalAmount": rentalAmount,
                "idFrontPhoto": idFrontPhoto,
                "idFrontExtension": idFrontExtension,
                "idBackPhoto": idBackPhoto,
                "idBackExtension": idBackExtension,
                "selfiePhoto": selfiePhoto,
                "selfieExtension": selfieExtension,
                "contractFile": contractFile,
                "contractFileExtension": contractFileExtension,
                "apiRequester": apiRequester,
                "renteeBirthdate": renteeBirthdate,
                "renteeStreetAddress": renteeStreetAddress,
                "renteeHouseNumber": renteeHouseNumber,
                "renteeZipCode": renteeZipCode,
                "renteeCity": renteeCity,
                "itemStatus": itemStatus,
                "itemType": itemType,
                "itemBrand": itemBrand,
                "itemModel": itemModel,
                "itemColor": itemColor,
                "serialNumber": serialNumber,
                "identificationNumber": identificationNumber,
                "rentDate": rentDate,
            }
    
    selfieExtension: MetaOapg.properties.selfieExtension
    renteeGender: MetaOapg.properties.renteeGender
    rentalAmount: MetaOapg.properties.rentalAmount
    renteeLastName: MetaOapg.properties.renteeLastName
    selfiePhoto: MetaOapg.properties.selfiePhoto
    contractFileExtension: MetaOapg.properties.contractFileExtension
    renteeEmail: MetaOapg.properties.renteeEmail
    contractFile: MetaOapg.properties.contractFile
    renteeFirstName: MetaOapg.properties.renteeFirstName
    itemName: MetaOapg.properties.itemName
    idBackExtension: MetaOapg.properties.idBackExtension
    idFrontExtension: MetaOapg.properties.idFrontExtension
    itemMarketValue: MetaOapg.properties.itemMarketValue
    renteeMobilePhoneNumber: MetaOapg.properties.renteeMobilePhoneNumber
    idBackPhoto: MetaOapg.properties.idBackPhoto
    purchaseItem: MetaOapg.properties.purchaseItem
    idFrontPhoto: MetaOapg.properties.idFrontPhoto
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeGender"]) -> MetaOapg.properties.renteeGender: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeFirstName"]) -> MetaOapg.properties.renteeFirstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeLastName"]) -> MetaOapg.properties.renteeLastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeEmail"]) -> MetaOapg.properties.renteeEmail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeMobilePhoneNumber"]) -> MetaOapg.properties.renteeMobilePhoneNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["purchaseItem"]) -> MetaOapg.properties.purchaseItem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemName"]) -> MetaOapg.properties.itemName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemMarketValue"]) -> MetaOapg.properties.itemMarketValue: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rentalAmount"]) -> MetaOapg.properties.rentalAmount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idFrontPhoto"]) -> MetaOapg.properties.idFrontPhoto: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idFrontExtension"]) -> MetaOapg.properties.idFrontExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idBackPhoto"]) -> MetaOapg.properties.idBackPhoto: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["idBackExtension"]) -> MetaOapg.properties.idBackExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfiePhoto"]) -> MetaOapg.properties.selfiePhoto: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selfieExtension"]) -> MetaOapg.properties.selfieExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractFile"]) -> MetaOapg.properties.contractFile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contractFileExtension"]) -> MetaOapg.properties.contractFileExtension: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["apiRequester"]) -> MetaOapg.properties.apiRequester: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeBirthdate"]) -> MetaOapg.properties.renteeBirthdate: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeStreetAddress"]) -> MetaOapg.properties.renteeStreetAddress: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeHouseNumber"]) -> MetaOapg.properties.renteeHouseNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeZipCode"]) -> MetaOapg.properties.renteeZipCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["renteeCity"]) -> MetaOapg.properties.renteeCity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemStatus"]) -> MetaOapg.properties.itemStatus: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemType"]) -> MetaOapg.properties.itemType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemBrand"]) -> MetaOapg.properties.itemBrand: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemModel"]) -> MetaOapg.properties.itemModel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["itemColor"]) -> MetaOapg.properties.itemColor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["serialNumber"]) -> MetaOapg.properties.serialNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["identificationNumber"]) -> MetaOapg.properties.identificationNumber: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rentDate"]) -> MetaOapg.properties.rentDate: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["renteeGender", "renteeFirstName", "renteeLastName", "renteeEmail", "renteeMobilePhoneNumber", "purchaseItem", "itemName", "itemMarketValue", "rentalAmount", "idFrontPhoto", "idFrontExtension", "idBackPhoto", "idBackExtension", "selfiePhoto", "selfieExtension", "contractFile", "contractFileExtension", "apiRequester", "renteeBirthdate", "renteeStreetAddress", "renteeHouseNumber", "renteeZipCode", "renteeCity", "itemStatus", "itemType", "itemBrand", "itemModel", "itemColor", "serialNumber", "identificationNumber", "rentDate", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeGender"]) -> MetaOapg.properties.renteeGender: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeFirstName"]) -> MetaOapg.properties.renteeFirstName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeLastName"]) -> MetaOapg.properties.renteeLastName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeEmail"]) -> MetaOapg.properties.renteeEmail: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeMobilePhoneNumber"]) -> MetaOapg.properties.renteeMobilePhoneNumber: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["purchaseItem"]) -> MetaOapg.properties.purchaseItem: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemName"]) -> MetaOapg.properties.itemName: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemMarketValue"]) -> MetaOapg.properties.itemMarketValue: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rentalAmount"]) -> MetaOapg.properties.rentalAmount: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idFrontPhoto"]) -> MetaOapg.properties.idFrontPhoto: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idFrontExtension"]) -> MetaOapg.properties.idFrontExtension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idBackPhoto"]) -> MetaOapg.properties.idBackPhoto: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["idBackExtension"]) -> MetaOapg.properties.idBackExtension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfiePhoto"]) -> MetaOapg.properties.selfiePhoto: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selfieExtension"]) -> MetaOapg.properties.selfieExtension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractFile"]) -> MetaOapg.properties.contractFile: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contractFileExtension"]) -> MetaOapg.properties.contractFileExtension: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["apiRequester"]) -> typing.Union[MetaOapg.properties.apiRequester, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeBirthdate"]) -> typing.Union[MetaOapg.properties.renteeBirthdate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeStreetAddress"]) -> typing.Union[MetaOapg.properties.renteeStreetAddress, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeHouseNumber"]) -> typing.Union[MetaOapg.properties.renteeHouseNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeZipCode"]) -> typing.Union[MetaOapg.properties.renteeZipCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["renteeCity"]) -> typing.Union[MetaOapg.properties.renteeCity, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemStatus"]) -> typing.Union[MetaOapg.properties.itemStatus, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemType"]) -> typing.Union[MetaOapg.properties.itemType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemBrand"]) -> typing.Union[MetaOapg.properties.itemBrand, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemModel"]) -> typing.Union[MetaOapg.properties.itemModel, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["itemColor"]) -> typing.Union[MetaOapg.properties.itemColor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["serialNumber"]) -> typing.Union[MetaOapg.properties.serialNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["identificationNumber"]) -> typing.Union[MetaOapg.properties.identificationNumber, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rentDate"]) -> typing.Union[MetaOapg.properties.rentDate, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["renteeGender", "renteeFirstName", "renteeLastName", "renteeEmail", "renteeMobilePhoneNumber", "purchaseItem", "itemName", "itemMarketValue", "rentalAmount", "idFrontPhoto", "idFrontExtension", "idBackPhoto", "idBackExtension", "selfiePhoto", "selfieExtension", "contractFile", "contractFileExtension", "apiRequester", "renteeBirthdate", "renteeStreetAddress", "renteeHouseNumber", "renteeZipCode", "renteeCity", "itemStatus", "itemType", "itemBrand", "itemModel", "itemColor", "serialNumber", "identificationNumber", "rentDate", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        selfieExtension: typing.Union[MetaOapg.properties.selfieExtension, str, ],
        renteeGender: typing.Union[MetaOapg.properties.renteeGender, str, ],
        rentalAmount: typing.Union[MetaOapg.properties.rentalAmount, decimal.Decimal, int, float, ],
        renteeLastName: typing.Union[MetaOapg.properties.renteeLastName, str, ],
        selfiePhoto: typing.Union[MetaOapg.properties.selfiePhoto, str, ],
        contractFileExtension: typing.Union[MetaOapg.properties.contractFileExtension, str, ],
        renteeEmail: typing.Union[MetaOapg.properties.renteeEmail, str, ],
        contractFile: typing.Union[MetaOapg.properties.contractFile, str, ],
        renteeFirstName: typing.Union[MetaOapg.properties.renteeFirstName, str, ],
        itemName: typing.Union[MetaOapg.properties.itemName, str, ],
        idBackExtension: typing.Union[MetaOapg.properties.idBackExtension, str, ],
        idFrontExtension: typing.Union[MetaOapg.properties.idFrontExtension, str, ],
        itemMarketValue: typing.Union[MetaOapg.properties.itemMarketValue, decimal.Decimal, int, float, ],
        renteeMobilePhoneNumber: typing.Union[MetaOapg.properties.renteeMobilePhoneNumber, str, ],
        idBackPhoto: typing.Union[MetaOapg.properties.idBackPhoto, str, ],
        purchaseItem: typing.Union[MetaOapg.properties.purchaseItem, str, ],
        idFrontPhoto: typing.Union[MetaOapg.properties.idFrontPhoto, str, ],
        apiRequester: typing.Union[MetaOapg.properties.apiRequester, None, str, schemas.Unset] = schemas.unset,
        renteeBirthdate: typing.Union[MetaOapg.properties.renteeBirthdate, None, str, schemas.Unset] = schemas.unset,
        renteeStreetAddress: typing.Union[MetaOapg.properties.renteeStreetAddress, None, str, schemas.Unset] = schemas.unset,
        renteeHouseNumber: typing.Union[MetaOapg.properties.renteeHouseNumber, None, str, schemas.Unset] = schemas.unset,
        renteeZipCode: typing.Union[MetaOapg.properties.renteeZipCode, None, str, schemas.Unset] = schemas.unset,
        renteeCity: typing.Union[MetaOapg.properties.renteeCity, None, str, schemas.Unset] = schemas.unset,
        itemStatus: typing.Union[MetaOapg.properties.itemStatus, None, str, schemas.Unset] = schemas.unset,
        itemType: typing.Union[MetaOapg.properties.itemType, None, str, schemas.Unset] = schemas.unset,
        itemBrand: typing.Union[MetaOapg.properties.itemBrand, None, str, schemas.Unset] = schemas.unset,
        itemModel: typing.Union[MetaOapg.properties.itemModel, None, str, schemas.Unset] = schemas.unset,
        itemColor: typing.Union[MetaOapg.properties.itemColor, None, str, schemas.Unset] = schemas.unset,
        serialNumber: typing.Union[MetaOapg.properties.serialNumber, None, str, schemas.Unset] = schemas.unset,
        identificationNumber: typing.Union[MetaOapg.properties.identificationNumber, None, str, schemas.Unset] = schemas.unset,
        rentDate: typing.Union[MetaOapg.properties.rentDate, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RentalLoanApplication':
        return super().__new__(
            cls,
            *args,
            selfieExtension=selfieExtension,
            renteeGender=renteeGender,
            rentalAmount=rentalAmount,
            renteeLastName=renteeLastName,
            selfiePhoto=selfiePhoto,
            contractFileExtension=contractFileExtension,
            renteeEmail=renteeEmail,
            contractFile=contractFile,
            renteeFirstName=renteeFirstName,
            itemName=itemName,
            idBackExtension=idBackExtension,
            idFrontExtension=idFrontExtension,
            itemMarketValue=itemMarketValue,
            renteeMobilePhoneNumber=renteeMobilePhoneNumber,
            idBackPhoto=idBackPhoto,
            purchaseItem=purchaseItem,
            idFrontPhoto=idFrontPhoto,
            apiRequester=apiRequester,
            renteeBirthdate=renteeBirthdate,
            renteeStreetAddress=renteeStreetAddress,
            renteeHouseNumber=renteeHouseNumber,
            renteeZipCode=renteeZipCode,
            renteeCity=renteeCity,
            itemStatus=itemStatus,
            itemType=itemType,
            itemBrand=itemBrand,
            itemModel=itemModel,
            itemColor=itemColor,
            serialNumber=serialNumber,
            identificationNumber=identificationNumber,
            rentDate=rentDate,
            _configuration=_configuration,
            **kwargs,
        )