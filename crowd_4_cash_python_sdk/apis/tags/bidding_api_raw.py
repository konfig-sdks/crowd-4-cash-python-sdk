# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from crowd_4_cash_python_sdk.paths.bid.post import PlaceBidRaw
from crowd_4_cash_python_sdk.paths.bids.post import SubmitBidsRaw


class BiddingApiRaw(
    PlaceBidRaw,
    SubmitBidsRaw,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    pass
