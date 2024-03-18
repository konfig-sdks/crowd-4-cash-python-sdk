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


class TechnicalData(BaseModel):
    # Client Ip address
    ip_address: typing.Optional[typing.Optional[str]] = Field(None, alias='ipAddress')

    # Gets the raw user agent string of the client browser that has been provided.
    user_agent: typing.Optional[typing.Optional[str]] = Field(None, alias='userAgent')

    # URL of the client's previous request that linked to our website
    url_referrer: typing.Optional[typing.Optional[str]] = Field(None, alias='urlReferrer')

    # Client browser
    browser_type: typing.Optional[typing.Optional[str]] = Field(None, alias='browserType')

    # Name of the browser
    browser_name: typing.Optional[typing.Optional[str]] = Field(None, alias='browserName')

    # Version of the browser
    browser_version: typing.Optional[typing.Optional[str]] = Field(None, alias='browserVersion')

    # Operating System
    platform: typing.Optional[typing.Optional[str]] = Field(None, alias='platform')

    # Does borrower use a beta version of the browser?
    is_beta: typing.Optional[typing.Optional[str]] = Field(None, alias='isBeta')

    # Does client connect by mobile device?
    is_mobile_device: typing.Optional[typing.Optional[str]] = Field(None, alias='isMobileDevice')

    # Manufacturer of the mobile device
    mobile_device_manufacturer: typing.Optional[typing.Optional[str]] = Field(None, alias='mobileDeviceManufacturer')

    # Model of the mobile device
    mobile_device_model: typing.Optional[typing.Optional[str]] = Field(None, alias='mobileDeviceModel')

    # Is the \"Do Not Track\" setting in their web browser enabled?
    is_do_not_track_enabled: typing.Optional[typing.Optional[str]] = Field(None, alias='isDoNotTrackEnabled')

    # Host of the client email
    email_host: typing.Optional[typing.Optional[str]] = Field(None, alias='emailHost')

    # Is name of the client a part of the email?
    is_name_in_email: typing.Optional[typing.Optional[str]] = Field(None, alias='isNameInEmail')

    # Is the name or the address lowercased?
    is_name_or_address_lowercased: typing.Optional[typing.Optional[str]] = Field(None, alias='isNameOrAddressLowercased')

    # How they found us?
    channel: typing.Optional[typing.Optional[str]] = Field(None, alias='channel')
    class Config:
        arbitrary_types_allowed = True
