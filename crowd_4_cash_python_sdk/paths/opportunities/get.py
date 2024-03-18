# coding: utf-8

"""
    C4C REST API

    Access to the Crowd4Cash Crowdlending Platform through an API

    The version of the OpenAPI document: 2.0.0
    Contact: info@crowd4cash.ch
    Created by: https://crowd4cash.ch
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from crowd_4_cash_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from crowd_4_cash_python_sdk.api_response import AsyncGeneratorResponse
from crowd_4_cash_python_sdk import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from crowd_4_cash_python_sdk import schemas  # noqa: F401

from crowd_4_cash_python_sdk.model.yn import YN as YNSchema
from crowd_4_cash_python_sdk.model.loan_rating import LoanRating as LoanRatingSchema
from crowd_4_cash_python_sdk.model.opportunity import Opportunity as OpportunitySchema
from crowd_4_cash_python_sdk.model.error import Error as ErrorSchema

from crowd_4_cash_python_sdk.type.opportunity import Opportunity
from crowd_4_cash_python_sdk.type.error import Error
from crowd_4_cash_python_sdk.type.yn import YN
from crowd_4_cash_python_sdk.type.loan_rating import LoanRating

from ...api_client import Dictionary
from crowd_4_cash_python_sdk.pydantic.loan_rating import LoanRating as LoanRatingPydantic
from crowd_4_cash_python_sdk.pydantic.yn import YN as YNPydantic
from crowd_4_cash_python_sdk.pydantic.opportunity import Opportunity as OpportunityPydantic
from crowd_4_cash_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# Query params
RatingSchema = LoanRatingSchema
LoanAmountSchema = schemas.Float64Schema
LoanTypeSchema = schemas.StrSchema
AvailableAmountSchema = schemas.Float64Schema
InterestRateSchema = schemas.Float64Schema
DurationSchema = schemas.Int32Schema
InsuranceSchema = YNSchema
CollateralSchema = YNSchema
BorrowerAgeSchema = schemas.Int32Schema
BorrowerNationalitySchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'Rating': typing.Union[RatingSchema, ],
        'LoanAmount': typing.Union[LoanAmountSchema, decimal.Decimal, int, float, ],
        'LoanType': typing.Union[LoanTypeSchema, str, ],
        'AvailableAmount': typing.Union[AvailableAmountSchema, decimal.Decimal, int, float, ],
        'InterestRate': typing.Union[InterestRateSchema, decimal.Decimal, int, float, ],
        'Duration': typing.Union[DurationSchema, decimal.Decimal, int, ],
        'Insurance': typing.Union[InsuranceSchema, ],
        'Collateral': typing.Union[CollateralSchema, ],
        'BorrowerAge': typing.Union[BorrowerAgeSchema, decimal.Decimal, int, ],
        'BorrowerNationality': typing.Union[BorrowerNationalitySchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_rating = api_client.QueryParameter(
    name="Rating",
    style=api_client.ParameterStyle.FORM,
    schema=LoanRatingSchema,
    explode=True,
)
request_query_loan_amount = api_client.QueryParameter(
    name="LoanAmount",
    style=api_client.ParameterStyle.FORM,
    schema=LoanAmountSchema,
    explode=True,
)
request_query_loan_type = api_client.QueryParameter(
    name="LoanType",
    style=api_client.ParameterStyle.FORM,
    schema=LoanTypeSchema,
    explode=True,
)
request_query_available_amount = api_client.QueryParameter(
    name="AvailableAmount",
    style=api_client.ParameterStyle.FORM,
    schema=AvailableAmountSchema,
    explode=True,
)
request_query_interest_rate = api_client.QueryParameter(
    name="InterestRate",
    style=api_client.ParameterStyle.FORM,
    schema=InterestRateSchema,
    explode=True,
)
request_query_duration = api_client.QueryParameter(
    name="Duration",
    style=api_client.ParameterStyle.FORM,
    schema=DurationSchema,
    explode=True,
)
request_query_insurance = api_client.QueryParameter(
    name="Insurance",
    style=api_client.ParameterStyle.FORM,
    schema=YNSchema,
    explode=True,
)
request_query_collateral = api_client.QueryParameter(
    name="Collateral",
    style=api_client.ParameterStyle.FORM,
    schema=YNSchema,
    explode=True,
)
request_query_borrower_age = api_client.QueryParameter(
    name="BorrowerAge",
    style=api_client.ParameterStyle.FORM,
    schema=BorrowerAgeSchema,
    explode=True,
)
request_query_borrower_nationality = api_client.QueryParameter(
    name="BorrowerNationality",
    style=api_client.ParameterStyle.FORM,
    schema=BorrowerNationalitySchema,
    explode=True,
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = OpportunitySchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Opportunity


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Opportunity


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor400Async(api_client.AsyncApiResponse):
    body: Error


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    response_cls_async=ApiResponseFor400Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor401Async(api_client.AsyncApiResponse):
    body: Error


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    response_cls_async=ApiResponseFor401Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorSchema


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    body: Error


@dataclass
class ApiResponseFor404Async(api_client.AsyncApiResponse):
    body: Error


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    response_cls_async=ApiResponseFor404Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
    '404': _response_for_404,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_available_investments_mapped_args(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if rating is not None:
            _query_params["Rating"] = rating
        if loan_amount is not None:
            _query_params["LoanAmount"] = loan_amount
        if loan_type is not None:
            _query_params["LoanType"] = loan_type
        if available_amount is not None:
            _query_params["AvailableAmount"] = available_amount
        if interest_rate is not None:
            _query_params["InterestRate"] = interest_rate
        if duration is not None:
            _query_params["Duration"] = duration
        if insurance is not None:
            _query_params["Insurance"] = insurance
        if collateral is not None:
            _query_params["Collateral"] = collateral
        if borrower_age is not None:
            _query_params["BorrowerAge"] = borrower_age
        if borrower_nationality is not None:
            _query_params["BorrowerNationality"] = borrower_nationality
        args.query = _query_params
        return args

    async def _aget_available_investments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get available investment opportunities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_rating,
            request_query_loan_amount,
            request_query_loan_type,
            request_query_available_amount,
            request_query_interest_rate,
            request_query_duration,
            request_query_insurance,
            request_query_collateral,
            request_query_borrower_age,
            request_query_borrower_nationality,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Opportunities',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _get_available_investments_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get available investment opportunities
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_rating,
            request_query_loan_amount,
            request_query_loan_type,
            request_query_available_amount,
            request_query_interest_rate,
            request_query_duration,
            request_query_insurance,
            request_query_collateral,
            request_query_borrower_age,
            request_query_borrower_nationality,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Opportunities',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class GetAvailableInvestmentsRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_available_investments(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_available_investments_mapped_args(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
        )
        return await self._aget_available_investments_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get_available_investments(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_available_investments_mapped_args(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
        )
        return self._get_available_investments_oapg(
            query_params=args.query,
        )

class GetAvailableInvestments(BaseApi):

    async def aget_available_investments(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OpportunityPydantic:
        raw_response = await self.raw.aget_available_investments(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
            **kwargs,
        )
        if validate:
            return OpportunityPydantic(**raw_response.body)
        return api_client.construct_model_instance(OpportunityPydantic, raw_response.body)
    
    
    def get_available_investments(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OpportunityPydantic:
        raw_response = self.raw.get_available_investments(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
        )
        if validate:
            return OpportunityPydantic(**raw_response.body)
        return api_client.construct_model_instance(OpportunityPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_available_investments_mapped_args(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
        )
        return await self._aget_available_investments_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        rating: typing.Optional[LoanRating] = None,
        loan_amount: typing.Optional[typing.Union[int, float]] = None,
        loan_type: typing.Optional[str] = None,
        available_amount: typing.Optional[typing.Union[int, float]] = None,
        interest_rate: typing.Optional[typing.Union[int, float]] = None,
        duration: typing.Optional[int] = None,
        insurance: typing.Optional[YN] = None,
        collateral: typing.Optional[YN] = None,
        borrower_age: typing.Optional[int] = None,
        borrower_nationality: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_available_investments_mapped_args(
            rating=rating,
            loan_amount=loan_amount,
            loan_type=loan_type,
            available_amount=available_amount,
            interest_rate=interest_rate,
            duration=duration,
            insurance=insurance,
            collateral=collateral,
            borrower_age=borrower_age,
            borrower_nationality=borrower_nationality,
        )
        return self._get_available_investments_oapg(
            query_params=args.query,
        )

