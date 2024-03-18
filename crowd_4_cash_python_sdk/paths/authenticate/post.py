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

from crowd_4_cash_python_sdk.model.login import Login as LoginSchema
from crowd_4_cash_python_sdk.model.token import Token as TokenSchema
from crowd_4_cash_python_sdk.model.error import Error as ErrorSchema

from crowd_4_cash_python_sdk.type.error import Error
from crowd_4_cash_python_sdk.type.login import Login
from crowd_4_cash_python_sdk.type.token import Token

from ...api_client import Dictionary
from crowd_4_cash_python_sdk.pydantic.login import Login as LoginPydantic
from crowd_4_cash_python_sdk.pydantic.error import Error as ErrorPydantic
from crowd_4_cash_python_sdk.pydantic.token import Token as TokenPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = LoginSchema


request_body_login = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = TokenSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: Token


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: Token


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
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _get_token_mapped_args(
        self,
        username: str,
        password: str,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if username is not None:
            _body["username"] = username
        if password is not None:
            _body["password"] = password
        args.body = _body
        return args

    async def _aget_token_oapg(
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
        Authenticate yourself and get an access token
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Authenticate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_login.serialize(body, content_type)
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


    def _get_token_oapg(
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
        Authenticate yourself and get an access token
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
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/Authenticate',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_login.serialize(body, content_type)
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


class GetTokenRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def aget_token(
        self,
        username: str,
        password: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_token_mapped_args(
            username=username,
            password=password,
        )
        return await self._aget_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def get_token(
        self,
        username: str,
        password: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_token_mapped_args(
            username=username,
            password=password,
        )
        return self._get_token_oapg(
            body=args.body,
        )

class GetToken(BaseApi):

    async def aget_token(
        self,
        username: str,
        password: str,
        validate: bool = False,
        **kwargs,
    ) -> TokenPydantic:
        raw_response = await self.raw.aget_token(
            username=username,
            password=password,
            **kwargs,
        )
        if validate:
            return TokenPydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenPydantic, raw_response.body)
    
    
    def get_token(
        self,
        username: str,
        password: str,
        validate: bool = False,
    ) -> TokenPydantic:
        raw_response = self.raw.get_token(
            username=username,
            password=password,
        )
        if validate:
            return TokenPydantic(**raw_response.body)
        return api_client.construct_model_instance(TokenPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        username: str,
        password: str,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._get_token_mapped_args(
            username=username,
            password=password,
        )
        return await self._aget_token_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        username: str,
        password: str,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._get_token_mapped_args(
            username=username,
            password=password,
        )
        return self._get_token_oapg(
            body=args.body,
        )

