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


class RequiredTechnicalData(TypedDict):
    pass

class OptionalTechnicalData(TypedDict, total=False):
    # Client Ip address
    ipAddress: typing.Optional[str]

    # Gets the raw user agent string of the client browser that has been provided.
    userAgent: typing.Optional[str]

    # URL of the client's previous request that linked to our website
    urlReferrer: typing.Optional[str]

    # Client browser
    browserType: typing.Optional[str]

    # Name of the browser
    browserName: typing.Optional[str]

    # Version of the browser
    browserVersion: typing.Optional[str]

    # Operating System
    platform: typing.Optional[str]

    # Does borrower use a beta version of the browser?
    isBeta: typing.Optional[str]

    # Does client connect by mobile device?
    isMobileDevice: typing.Optional[str]

    # Manufacturer of the mobile device
    mobileDeviceManufacturer: typing.Optional[str]

    # Model of the mobile device
    mobileDeviceModel: typing.Optional[str]

    # Is the \"Do Not Track\" setting in their web browser enabled?
    isDoNotTrackEnabled: typing.Optional[str]

    # Host of the client email
    emailHost: typing.Optional[str]

    # Is name of the client a part of the email?
    isNameInEmail: typing.Optional[str]

    # Is the name or the address lowercased?
    isNameOrAddressLowercased: typing.Optional[str]

    # How they found us?
    channel: typing.Optional[str]

class TechnicalData(RequiredTechnicalData, OptionalTechnicalData):
    pass
