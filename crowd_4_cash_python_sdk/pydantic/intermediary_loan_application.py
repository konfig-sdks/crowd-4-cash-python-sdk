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


class IntermediaryLoanApplication(BaseModel):
    # Serial number (aka VIN or Chassis No.)
    serial_number: str = Field(alias='serialNumber')

    # Identification number (aka Stammnummer)
    identification_number: str = Field(alias='identificationNumber')

    # ID of the partner that is buying an item. This ID can be taken from the Report endpoint and Intermediary route.
    partner_id: typing.Optional[int] = Field(None, alias='partnerId')

    # Description of the item you buy e.g. Car
    purchase_item: typing.Optional[typing.Optional[str]] = Field(None, alias='purchaseItem')

    # Status of the item
    item_status: typing.Optional[typing.Optional[str]] = Field(None, alias='itemStatus')

    # Name of the item
    item_name: typing.Optional[typing.Optional[str]] = Field(None, alias='itemName')

    # Type of the item e.g. SUV, Van, Saloon, Cabriolet etc.
    item_type: typing.Optional[typing.Optional[str]] = Field(None, alias='itemType')

    # Brand of the item
    item_brand: typing.Optional[typing.Optional[str]] = Field(None, alias='itemBrand')

    # Model of the item
    item_model: typing.Optional[typing.Optional[str]] = Field(None, alias='itemModel')

    # Color of the item
    item_color: typing.Optional[typing.Optional[str]] = Field(None, alias='itemColor')

    # Market value of the item you want to buy. Please notice that the Loan Amount will be 80% of this value.
    item_market_value: typing.Optional[typing.Union[int, float]] = Field(None, alias='itemMarketValue')

    # Date when the car was manufactured
    manufacture_date: typing.Optional[typing.Optional[str]] = Field(None, alias='manufactureDate')

    # Date when the item was registered very first time
    first_registration: typing.Optional[typing.Optional[str]] = Field(None, alias='firstRegistration')

    # Mileage of the item
    mileage: typing.Optional[typing.Optional[str]] = Field(None, alias='mileage')

    # Certificate of the item
    item_certificate: typing.Optional[typing.Optional[str]] = Field(None, alias='itemCertificate')

    # Rental amount per month
    rental_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='rentalAmount')

    # The expected/approximate handover date (date when the car is expected to be handed over to the subscriber). Expected format: dd.MM.yyyy
    handover_date: typing.Optional[typing.Optional[str]] = Field(None, alias='handoverDate')
    class Config:
        arbitrary_types_allowed = True
