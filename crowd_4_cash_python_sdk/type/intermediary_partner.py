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


class RequiredIntermediaryPartner(TypedDict):
    pass

class OptionalIntermediaryPartner(TypedDict, total=False):
    # Id of the partner
    partnerId: int

    # Name of the partner
    partnerName: typing.Optional[str]

    # legal form of the partner
    legalForm: typing.Optional[str]

    # when the company was established
    yearEstablished: typing.Optional[str]

    # Street address of the garage/shop/store
    address: typing.Optional[str]

    # House number of the garage/shop/store
    houseNumber: typing.Optional[str]

    # Zip code of the garage/shop/store
    zip: typing.Optional[str]

    # City where the garage/shop/store resides
    city: typing.Optional[str]

    # Phone number of the garage/shop/store
    phone: typing.Optional[str]

    # IBAN of the company
    iban: typing.Optional[str]

    # total number of loans
    numberOfLoans: int

    # limit allowed by C4C e.g. 200'000.00 CHF
    allowedLimitAmount: typing.Union[int, float]

    # An amount that is already used out e.g. 150'000.00 CHF
    usedLimitAmount: typing.Union[int, float]

    # available amount e.g. 50'000.00 CHF
    remainingLimitAmount: typing.Union[int, float]

class IntermediaryPartner(RequiredIntermediaryPartner, OptionalIntermediaryPartner):
    pass
