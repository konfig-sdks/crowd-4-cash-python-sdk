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

from crowd_4_cash_python_sdk.model.rental_application_result import RentalApplicationResult as RentalApplicationResultSchema
from crowd_4_cash_python_sdk.model.rental_loan_application import RentalLoanApplication as RentalLoanApplicationSchema
from crowd_4_cash_python_sdk.model.error import Error as ErrorSchema

from crowd_4_cash_python_sdk.type.error import Error
from crowd_4_cash_python_sdk.type.rental_application_result import RentalApplicationResult
from crowd_4_cash_python_sdk.type.rental_loan_application import RentalLoanApplication

from ...api_client import Dictionary
from crowd_4_cash_python_sdk.pydantic.rental_application_result import RentalApplicationResult as RentalApplicationResultPydantic
from crowd_4_cash_python_sdk.pydantic.rental_loan_application import RentalLoanApplication as RentalLoanApplicationPydantic
from crowd_4_cash_python_sdk.pydantic.error import Error as ErrorPydantic

from . import path

# body param
SchemaForRequestBodyApplicationJson = RentalLoanApplicationSchema


request_body_rental_loan_application = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
_auth = [
    'Bearer',
]
SchemaFor200ResponseBodyApplicationJson = RentalApplicationResultSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: RentalApplicationResult


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: RentalApplicationResult


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

    def _submit_rental_loan_application_mapped_args(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if api_requester is not None:
            _body["apiRequester"] = api_requester
        if rentee_gender is not None:
            _body["renteeGender"] = rentee_gender
        if rentee_first_name is not None:
            _body["renteeFirstName"] = rentee_first_name
        if rentee_last_name is not None:
            _body["renteeLastName"] = rentee_last_name
        if rentee_birthdate is not None:
            _body["renteeBirthdate"] = rentee_birthdate
        if rentee_email is not None:
            _body["renteeEmail"] = rentee_email
        if rentee_mobile_phone_number is not None:
            _body["renteeMobilePhoneNumber"] = rentee_mobile_phone_number
        if rentee_street_address is not None:
            _body["renteeStreetAddress"] = rentee_street_address
        if rentee_house_number is not None:
            _body["renteeHouseNumber"] = rentee_house_number
        if rentee_zip_code is not None:
            _body["renteeZipCode"] = rentee_zip_code
        if rentee_city is not None:
            _body["renteeCity"] = rentee_city
        if purchase_item is not None:
            _body["purchaseItem"] = purchase_item
        if item_status is not None:
            _body["itemStatus"] = item_status
        if item_name is not None:
            _body["itemName"] = item_name
        if item_type is not None:
            _body["itemType"] = item_type
        if item_brand is not None:
            _body["itemBrand"] = item_brand
        if item_model is not None:
            _body["itemModel"] = item_model
        if item_color is not None:
            _body["itemColor"] = item_color
        if item_market_value is not None:
            _body["itemMarketValue"] = item_market_value
        if serial_number is not None:
            _body["serialNumber"] = serial_number
        if identification_number is not None:
            _body["identificationNumber"] = identification_number
        if rental_amount is not None:
            _body["rentalAmount"] = rental_amount
        if rent_date is not None:
            _body["rentDate"] = rent_date
        if id_front_photo is not None:
            _body["idFrontPhoto"] = id_front_photo
        if id_front_extension is not None:
            _body["idFrontExtension"] = id_front_extension
        if id_back_photo is not None:
            _body["idBackPhoto"] = id_back_photo
        if id_back_extension is not None:
            _body["idBackExtension"] = id_back_extension
        if selfie_photo is not None:
            _body["selfiePhoto"] = selfie_photo
        if selfie_extension is not None:
            _body["selfieExtension"] = selfie_extension
        if contract_file is not None:
            _body["contractFile"] = contract_file
        if contract_file_extension is not None:
            _body["contractFileExtension"] = contract_file_extension
        args.body = _body
        return args

    async def _asubmit_rental_loan_application_oapg(
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
        Apply for a rental loan
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
            path_template='/RentalLoan',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_rental_loan_application.serialize(body, content_type)
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


    def _submit_rental_loan_application_oapg(
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
        Apply for a rental loan
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
            path_template='/RentalLoan',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_rental_loan_application.serialize(body, content_type)
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


class SubmitRentalLoanApplicationRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def asubmit_rental_loan_application(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._submit_rental_loan_application_mapped_args(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
        )
        return await self._asubmit_rental_loan_application_oapg(
            body=args.body,
            **kwargs,
        )
    
    def submit_rental_loan_application(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._submit_rental_loan_application_mapped_args(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
        )
        return self._submit_rental_loan_application_oapg(
            body=args.body,
        )

class SubmitRentalLoanApplication(BaseApi):

    async def asubmit_rental_loan_application(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
        **kwargs,
    ) -> RentalApplicationResultPydantic:
        raw_response = await self.raw.asubmit_rental_loan_application(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
            **kwargs,
        )
        if validate:
            return RentalApplicationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(RentalApplicationResultPydantic, raw_response.body)
    
    
    def submit_rental_loan_application(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
        validate: bool = False,
    ) -> RentalApplicationResultPydantic:
        raw_response = self.raw.submit_rental_loan_application(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
        )
        if validate:
            return RentalApplicationResultPydantic(**raw_response.body)
        return api_client.construct_model_instance(RentalApplicationResultPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._submit_rental_loan_application_mapped_args(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
        )
        return await self._asubmit_rental_loan_application_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        rentee_gender: str,
        rentee_first_name: str,
        rentee_last_name: str,
        rentee_email: str,
        rentee_mobile_phone_number: str,
        purchase_item: str,
        item_name: str,
        item_market_value: typing.Union[int, float],
        rental_amount: typing.Union[int, float],
        id_front_photo: str,
        id_front_extension: str,
        id_back_photo: str,
        id_back_extension: str,
        selfie_photo: str,
        selfie_extension: str,
        contract_file: str,
        contract_file_extension: str,
        api_requester: typing.Optional[typing.Optional[str]] = None,
        rentee_birthdate: typing.Optional[typing.Optional[str]] = None,
        rentee_street_address: typing.Optional[typing.Optional[str]] = None,
        rentee_house_number: typing.Optional[typing.Optional[str]] = None,
        rentee_zip_code: typing.Optional[typing.Optional[str]] = None,
        rentee_city: typing.Optional[typing.Optional[str]] = None,
        item_status: typing.Optional[typing.Optional[str]] = None,
        item_type: typing.Optional[typing.Optional[str]] = None,
        item_brand: typing.Optional[typing.Optional[str]] = None,
        item_model: typing.Optional[typing.Optional[str]] = None,
        item_color: typing.Optional[typing.Optional[str]] = None,
        serial_number: typing.Optional[typing.Optional[str]] = None,
        identification_number: typing.Optional[typing.Optional[str]] = None,
        rent_date: typing.Optional[typing.Optional[str]] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._submit_rental_loan_application_mapped_args(
            rentee_gender=rentee_gender,
            rentee_first_name=rentee_first_name,
            rentee_last_name=rentee_last_name,
            rentee_email=rentee_email,
            rentee_mobile_phone_number=rentee_mobile_phone_number,
            purchase_item=purchase_item,
            item_name=item_name,
            item_market_value=item_market_value,
            rental_amount=rental_amount,
            id_front_photo=id_front_photo,
            id_front_extension=id_front_extension,
            id_back_photo=id_back_photo,
            id_back_extension=id_back_extension,
            selfie_photo=selfie_photo,
            selfie_extension=selfie_extension,
            contract_file=contract_file,
            contract_file_extension=contract_file_extension,
            api_requester=api_requester,
            rentee_birthdate=rentee_birthdate,
            rentee_street_address=rentee_street_address,
            rentee_house_number=rentee_house_number,
            rentee_zip_code=rentee_zip_code,
            rentee_city=rentee_city,
            item_status=item_status,
            item_type=item_type,
            item_brand=item_brand,
            item_model=item_model,
            item_color=item_color,
            serial_number=serial_number,
            identification_number=identification_number,
            rent_date=rent_date,
        )
        return self._submit_rental_loan_application_oapg(
            body=args.body,
        )

