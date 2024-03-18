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


class Rentee(BaseModel):
    # Id of the rentee
    rentee_id: typing.Optional[int] = Field(None, alias='renteeId')

    # Rentee gender acronym. M stands for male and F for female.
    gender: typing.Optional[typing.Optional[str]] = Field(None, alias='gender')

    # First name of the rentee
    first_name: typing.Optional[typing.Optional[str]] = Field(None, alias='firstName')

    # Last name of the rentee
    last_name: typing.Optional[typing.Optional[str]] = Field(None, alias='lastName')

    # Birthdate of the rentee
    birthdate: typing.Optional[typing.Optional[str]] = Field(None, alias='birthdate')

    # E-mail address of the rentee
    email: typing.Optional[typing.Optional[str]] = Field(None, alias='email')

    # Mobile phone number of the rentee
    mobile_phone: typing.Optional[typing.Optional[str]] = Field(None, alias='mobilePhone')

    # Street address of the garage/shop/store
    street_address: typing.Optional[typing.Optional[str]] = Field(None, alias='streetAddress')

    # House number of the garage/shop/store
    house_number: typing.Optional[typing.Optional[str]] = Field(None, alias='houseNumber')

    # Zip code of the rentee
    zip_code: typing.Optional[typing.Optional[str]] = Field(None, alias='zipCode')

    # City where the rentee resides
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # IBAN of the rentee
    iban: typing.Optional[typing.Optional[str]] = Field(None, alias='iban')
    class Config:
        arbitrary_types_allowed = True
