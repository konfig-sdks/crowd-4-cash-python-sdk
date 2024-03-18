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


class RequiredRentee(TypedDict):
    pass

class OptionalRentee(TypedDict, total=False):
    # Id of the rentee
    renteeId: int

    # Rentee gender acronym. M stands for male and F for female.
    gender: typing.Optional[str]

    # First name of the rentee
    firstName: typing.Optional[str]

    # Last name of the rentee
    lastName: typing.Optional[str]

    # Birthdate of the rentee
    birthdate: typing.Optional[str]

    # E-mail address of the rentee
    email: typing.Optional[str]

    # Mobile phone number of the rentee
    mobilePhone: typing.Optional[str]

    # Street address of the garage/shop/store
    streetAddress: typing.Optional[str]

    # House number of the garage/shop/store
    houseNumber: typing.Optional[str]

    # Zip code of the rentee
    zipCode: typing.Optional[str]

    # City where the rentee resides
    city: typing.Optional[str]

    # IBAN of the rentee
    iban: typing.Optional[str]

class Rentee(RequiredRentee, OptionalRentee):
    pass
