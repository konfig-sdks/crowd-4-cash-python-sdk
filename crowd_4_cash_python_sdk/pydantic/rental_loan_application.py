# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel


class RentalLoanApplication(BaseModel):
    # Rentee gender acronym. M stands for male and F for female.
    rentee_gender: str = Field(alias='renteeGender')

    # First name of the rentee
    rentee_first_name: str = Field(alias='renteeFirstName')

    # Last name of the rentee
    rentee_last_name: str = Field(alias='renteeLastName')

    # E-mail address of the rentee
    rentee_email: str = Field(alias='renteeEmail')

    # Rentee mobile phone number - the last 8 digits only
    rentee_mobile_phone_number: str = Field(alias='renteeMobilePhoneNumber')

    # Description of the item you buy
    purchase_item: str = Field(alias='purchaseItem')

    # Name of the item
    item_name: str = Field(alias='itemName')

    # Market value of the item that is rented.
    item_market_value: typing.Union[int, float] = Field(alias='itemMarketValue')

    # Rental amount per month
    rental_amount: typing.Union[int, float] = Field(alias='rentalAmount')

    # Front Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.
    id_front_photo: str = Field(alias='idFrontPhoto')

    # Front Side file extension.
    id_front_extension: str = Field(alias='idFrontExtension')

    # Back Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.
    id_back_photo: str = Field(alias='idBackPhoto')

    # Back Side file extension.
    id_back_extension: str = Field(alias='idBackExtension')

    # Selfie of the Rentee. Please notice that you must first convert it to Base64 and then send to our API.
    selfie_photo: str = Field(alias='selfiePhoto')

    # Selfie file extension.
    selfie_extension: str = Field(alias='selfieExtension')

    # Copy of the Contract. Please notice that you must first convert it to Base64 and then send to our API.
    contract_file: str = Field(alias='contractFile')

    # Contract file extension.
    contract_file_extension: str = Field(alias='contractFileExtension')

    # Name or E-mail of the user who makes the API call
    api_requester: typing.Optional[typing.Optional[str]] = Field(None, alias='apiRequester')

    # Birthdate of the rentee. Expected format: dd.MM.yyyy
    rentee_birthdate: typing.Optional[typing.Optional[str]] = Field(None, alias='renteeBirthdate')

    # Street address of the rentee
    rentee_street_address: typing.Optional[typing.Optional[str]] = Field(None, alias='renteeStreetAddress')

    # House number of the rentee
    rentee_house_number: typing.Optional[typing.Optional[str]] = Field(None, alias='renteeHouseNumber')

    # Zip code of the rentee
    rentee_zip_code: typing.Optional[typing.Optional[str]] = Field(None, alias='renteeZipCode')

    # City of the rentee
    rentee_city: typing.Optional[typing.Optional[str]] = Field(None, alias='renteeCity')

    # Status of the item
    item_status: typing.Optional[typing.Optional[str]] = Field(None, alias='itemStatus')

    # Type of the item e.g. Electric Scooter, E-Motorcycle etc.
    item_type: typing.Optional[typing.Optional[str]] = Field(None, alias='itemType')

    # Brand of the item
    item_brand: typing.Optional[typing.Optional[str]] = Field(None, alias='itemBrand')

    # Model of the item
    item_model: typing.Optional[typing.Optional[str]] = Field(None, alias='itemModel')

    # Color of the item
    item_color: typing.Optional[typing.Optional[str]] = Field(None, alias='itemColor')

    # Serial number (aka VIN or Chassis No.)
    serial_number: typing.Optional[typing.Optional[str]] = Field(None, alias='serialNumber')

    # Identification number (aka Stammnummer)
    identification_number: typing.Optional[typing.Optional[str]] = Field(None, alias='identificationNumber')

    # The first date of the rental period. Expected format: dd.MM.yyyy
    rent_date: typing.Optional[typing.Optional[str]] = Field(None, alias='rentDate')
    class Config:
        arbitrary_types_allowed = True
