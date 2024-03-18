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


class RequiredIntermediaryLoanApplication(TypedDict):
    # Serial number (aka VIN or Chassis No.)
    serialNumber: str

    # Identification number (aka Stammnummer)
    identificationNumber: str

class OptionalIntermediaryLoanApplication(TypedDict, total=False):
    # ID of the partner that is buying an item. This ID can be taken from the Report endpoint and Intermediary route.
    partnerId: int

    # Description of the item you buy e.g. Car
    purchaseItem: typing.Optional[str]

    # Status of the item
    itemStatus: typing.Optional[str]

    # Name of the item
    itemName: typing.Optional[str]

    # Type of the item e.g. SUV, Van, Saloon, Cabriolet etc.
    itemType: typing.Optional[str]

    # Brand of the item
    itemBrand: typing.Optional[str]

    # Model of the item
    itemModel: typing.Optional[str]

    # Color of the item
    itemColor: typing.Optional[str]

    # Market value of the item you want to buy. Please notice that the Loan Amount will be 80% of this value.
    itemMarketValue: typing.Union[int, float]

    # Date when the car was manufactured
    manufactureDate: typing.Optional[str]

    # Date when the item was registered very first time
    firstRegistration: typing.Optional[str]

    # Mileage of the item
    mileage: typing.Optional[str]

    # Certificate of the item
    itemCertificate: typing.Optional[str]

    # Rental amount per month
    rentalAmount: typing.Union[int, float]

    # The expected/approximate handover date (date when the car is expected to be handed over to the subscriber). Expected format: dd.MM.yyyy
    handoverDate: typing.Optional[str]

class IntermediaryLoanApplication(RequiredIntermediaryLoanApplication, OptionalIntermediaryLoanApplication):
    pass
