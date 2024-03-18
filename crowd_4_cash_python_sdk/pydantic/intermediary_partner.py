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


class IntermediaryPartner(BaseModel):
    # Id of the partner
    partner_id: typing.Optional[int] = Field(None, alias='partnerId')

    # Name of the partner
    partner_name: typing.Optional[typing.Optional[str]] = Field(None, alias='partnerName')

    # legal form of the partner
    legal_form: typing.Optional[typing.Optional[str]] = Field(None, alias='legalForm')

    # when the company was established
    year_established: typing.Optional[typing.Optional[str]] = Field(None, alias='yearEstablished')

    # Street address of the garage/shop/store
    address: typing.Optional[typing.Optional[str]] = Field(None, alias='address')

    # House number of the garage/shop/store
    house_number: typing.Optional[typing.Optional[str]] = Field(None, alias='houseNumber')

    # Zip code of the garage/shop/store
    zip: typing.Optional[typing.Optional[str]] = Field(None, alias='zip')

    # City where the garage/shop/store resides
    city: typing.Optional[typing.Optional[str]] = Field(None, alias='city')

    # Phone number of the garage/shop/store
    phone: typing.Optional[typing.Optional[str]] = Field(None, alias='phone')

    # IBAN of the company
    iban: typing.Optional[typing.Optional[str]] = Field(None, alias='iban')

    # total number of loans
    number_of_loans: typing.Optional[int] = Field(None, alias='numberOfLoans')

    # limit allowed by C4C e.g. 200'000.00 CHF
    allowed_limit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='allowedLimitAmount')

    # An amount that is already used out e.g. 150'000.00 CHF
    used_limit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='usedLimitAmount')

    # available amount e.g. 50'000.00 CHF
    remaining_limit_amount: typing.Optional[typing.Union[int, float]] = Field(None, alias='remainingLimitAmount')
    class Config:
        arbitrary_types_allowed = True
