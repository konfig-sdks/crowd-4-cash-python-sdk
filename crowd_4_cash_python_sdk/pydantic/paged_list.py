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

from crowd_4_cash_python_sdk.pydantic.loan import Loan

class PagedList(BaseModel):
    loans: typing.Optional[typing.Optional[typing.List[Loan]]] = Field(None, alias='loans')

    current_page: typing.Optional[int] = Field(None, alias='currentPage')

    total_pages: typing.Optional[int] = Field(None, alias='totalPages')

    page_size: typing.Optional[int] = Field(None, alias='pageSize')

    total_loans_count: typing.Optional[int] = Field(None, alias='totalLoansCount')

    has_previous_page: typing.Optional[bool] = Field(None, alias='hasPreviousPage')

    has_next_page: typing.Optional[bool] = Field(None, alias='hasNextPage')
    class Config:
        arbitrary_types_allowed = True
