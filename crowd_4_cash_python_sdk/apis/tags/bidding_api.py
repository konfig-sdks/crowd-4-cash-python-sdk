# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from crowd_4_cash_python_sdk.paths.bid.post import PlaceBid
from crowd_4_cash_python_sdk.paths.bids.post import SubmitBids
from crowd_4_cash_python_sdk.apis.tags.bidding_api_raw import BiddingApiRaw


class BiddingApi(
    PlaceBid,
    SubmitBids,
):
    """NOTE:
    This class is auto generated by Konfig (https://konfigthis.com)
    """
    raw: BiddingApiRaw

    def __init__(self, api_client=None):
        super().__init__(api_client)
        self.raw = BiddingApiRaw(api_client)
