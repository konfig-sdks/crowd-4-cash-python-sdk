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

from crowd_4_cash_python_sdk.model.intermediary_loan_handover_date import IntermediaryLoanHandoverDate as IntermediaryLoanHandoverDateSchema
from crowd_4_cash_python_sdk.model.application_result import ApplicationResult as ApplicationResultSchema
from crowd_4_cash_python_sdk.model.error import Error as ErrorSchema

from crowd_4_cash_python_sdk.type.error import Error
from crowd_4_cash_python_sdk.type.intermediary_loan_handover_date import IntermediaryLoanHandoverDate
from crowd_4_cash_python_sdk.type.application_result import ApplicationResult

from ...api_client import Dictionary
from crowd_4_cash_python_sdk.pydantic.intermediary_loan_handover_date import IntermediaryLoanHandoverDate as IntermediaryLoanHandoverDatePydantic
from crowd_4_cash_python_sdk.pydantic.error import Error as ErrorPydantic
from crowd_4_cash_python_sdk.pydantic.application_result import ApplicationResult as ApplicationResultPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = IntermediaryLoanHandoverDateSchema


request_body_intermediary_loan_handover_date = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = ApplicationResultSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: ApplicationResult


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: ApplicationResult


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
    '401': _response_for_401,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _set_definitive_handover_date_mapped_args(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if loan_id is not None:
            _body["loanId"] = loan_id
        if handover_date is not None:
            _body["handoverDate"] = handover_date
        args.body = _body
        return args

    async def _aset_definitive_handover_date_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Set the definitive Handover Date (a date when the item is handed over to the customer)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/IntermediaryLoan',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_intermediary_loan_handover_date.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


    def _set_definitive_handover_date_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Set the definitive Handover Date (a date when the item is handed over to the customer)
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'put'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/IntermediaryLoan',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_intermediary_loan_handover_date.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
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


class SetDefinitiveHandoverDateRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aset_definitive_handover_date(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_definitive_handover_date_mapped_args(
            loan_id=loan_id,
            handover_date=handover_date,
        )
        return await self._aset_definitive_handover_date_oapg(
            body=args.body,
            **kwargs,
        )
    
    def set_definitive_handover_date(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_definitive_handover_date_mapped_args(
            loan_id=loan_id,
            handover_date=handover_date,
        )
        return self._set_definitive_handover_date_oapg(
            body=args.body,
        )

class SetDefinitiveHandoverDate(BaseApi):

    async def aset_definitive_handover_date(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> ApplicationResultPydantic:
        raw_response = await self.raw.aset_definitive_handover_date(
            loan_id=loan_id,
            handover_date=handover_date,
            **kwargs,
        )
        if validate:
            return ApplicationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationResultPydantic, raw_response.body)
    
    
    def set_definitive_handover_date(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> ApplicationResultPydantic:
        raw_response = self.raw.set_definitive_handover_date(
            loan_id=loan_id,
            handover_date=handover_date,
        )
        if validate:
            return ApplicationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(ApplicationResultPydantic, raw_response.body)


class ApiForput(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aput(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._set_definitive_handover_date_mapped_args(
            loan_id=loan_id,
            handover_date=handover_date,
        )
        return await self._aset_definitive_handover_date_oapg(
            body=args.body,
            **kwargs,
        )
    
    def put(
        self,
        loan_id: typing.Optional[int] = None,
        handover_date: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._set_definitive_handover_date_mapped_args(
            loan_id=loan_id,
            handover_date=handover_date,
        )
        return self._set_definitive_handover_date_oapg(
            body=args.body,
        )

