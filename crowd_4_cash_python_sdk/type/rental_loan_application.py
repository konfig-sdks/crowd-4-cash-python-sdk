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


class RequiredRentalLoanApplication(TypedDict):
    # Rentee gender acronym. M stands for male and F for female.
    renteeGender: str

    # First name of the rentee
    renteeFirstName: str

    # Last name of the rentee
    renteeLastName: str

    # E-mail address of the rentee
    renteeEmail: str

    # Rentee mobile phone number - the last 8 digits only
    renteeMobilePhoneNumber: str

    # Description of the item you buy
    purchaseItem: str

    # Name of the item
    itemName: str

    # Market value of the item that is rented.
    itemMarketValue: typing.Union[int, float]

    # Rental amount per month
    rentalAmount: typing.Union[int, float]

    # Front Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.
    idFrontPhoto: str

    # Front Side file extension.
    idFrontExtension: str

    # Back Side of the Identity Document (National ID, Passport or Permit). Please notice that you must first convert it to Base64 and then send to our API.
    idBackPhoto: str

    # Back Side file extension.
    idBackExtension: str

    # Selfie of the Rentee. Please notice that you must first convert it to Base64 and then send to our API.
    selfiePhoto: str

    # Selfie file extension.
    selfieExtension: str

    # Copy of the Contract. Please notice that you must first convert it to Base64 and then send to our API.
    contractFile: str

    # Contract file extension.
    contractFileExtension: str

class OptionalRentalLoanApplication(TypedDict, total=False):
    # Name or E-mail of the user who makes the API call
    apiRequester: typing.Optional[str]

    # Birthdate of the rentee. Expected format: dd.MM.yyyy
    renteeBirthdate: typing.Optional[str]

    # Street address of the rentee
    renteeStreetAddress: typing.Optional[str]

    # House number of the rentee
    renteeHouseNumber: typing.Optional[str]

    # Zip code of the rentee
    renteeZipCode: typing.Optional[str]

    # City of the rentee
    renteeCity: typing.Optional[str]

    # Status of the item
    itemStatus: typing.Optional[str]

    # Type of the item e.g. Electric Scooter, E-Motorcycle etc.
    itemType: typing.Optional[str]

    # Brand of the item
    itemBrand: typing.Optional[str]

    # Model of the item
    itemModel: typing.Optional[str]

    # Color of the item
    itemColor: typing.Optional[str]

    # Serial number (aka VIN or Chassis No.)
    serialNumber: typing.Optional[str]

    # Identification number (aka Stammnummer)
    identificationNumber: typing.Optional[str]

    # The first date of the rental period. Expected format: dd.MM.yyyy
    rentDate: typing.Optional[str]

class RentalLoanApplication(RequiredRentalLoanApplication, OptionalRentalLoanApplication):
    pass
