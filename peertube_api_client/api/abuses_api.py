# coding: utf-8

"""
    PeerTube

    The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api-rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/*`                    | | `/download/*`               | | `/lazy-static/*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins.   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr, conint, conlist, validator

from typing import Optional

from peertube_api_client.models.abuse_state_set import AbuseStateSet
from peertube_api_client.models.api_v1_abuses_abuse_id_messages_get200_response import ApiV1AbusesAbuseIdMessagesGet200Response
from peertube_api_client.models.api_v1_abuses_abuse_id_messages_post_request import ApiV1AbusesAbuseIdMessagesPostRequest
from peertube_api_client.models.api_v1_abuses_abuse_id_put_request import ApiV1AbusesAbuseIdPutRequest
from peertube_api_client.models.api_v1_abuses_post200_response import ApiV1AbusesPost200Response
from peertube_api_client.models.api_v1_abuses_post_request import ApiV1AbusesPostRequest
from peertube_api_client.models.get_my_abuses200_response import GetMyAbuses200Response

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class AbusesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def api_v1_abuses_abuse_id_delete(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], **kwargs) -> None:  # noqa: E501
        """Delete an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_delete(abuse_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_abuse_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_abuse_id_delete_with_http_info(abuse_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_abuse_id_delete_with_http_info(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_delete_with_http_info(abuse_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'abuse_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_abuse_id_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['abuse_id']:
            _path_params['abuseId'] = _params['abuse_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/abuses/{abuseId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_abuse_message_id_delete(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], abuse_message_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse message id")], **kwargs) -> None:  # noqa: E501
        """Delete an abuse message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_abuse_message_id_delete(abuse_id, abuse_message_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param abuse_message_id: Abuse message id (required)
        :type abuse_message_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_abuse_id_messages_abuse_message_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_abuse_id_messages_abuse_message_id_delete_with_http_info(abuse_id, abuse_message_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_abuse_message_id_delete_with_http_info(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], abuse_message_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse message id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete an abuse message  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_abuse_message_id_delete_with_http_info(abuse_id, abuse_message_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param abuse_message_id: Abuse message id (required)
        :type abuse_message_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'abuse_id',
            'abuse_message_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_abuse_id_messages_abuse_message_id_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['abuse_id']:
            _path_params['abuseId'] = _params['abuse_id']

        if _params['abuse_message_id']:
            _path_params['abuseMessageId'] = _params['abuse_message_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/abuses/{abuseId}/messages/{abuseMessageId}', 'DELETE',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_get(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], **kwargs) -> ApiV1AbusesAbuseIdMessagesGet200Response:  # noqa: E501
        """List messages of an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_get(abuse_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1AbusesAbuseIdMessagesGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_abuse_id_messages_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_abuse_id_messages_get_with_http_info(abuse_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_get_with_http_info(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], **kwargs) -> ApiResponse:  # noqa: E501
        """List messages of an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_get_with_http_info(abuse_id, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiV1AbusesAbuseIdMessagesGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'abuse_id'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_abuse_id_messages_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['abuse_id']:
            _path_params['abuseId'] = _params['abuse_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "ApiV1AbusesAbuseIdMessagesGet200Response",
        }

        return self.api_client.call_api(
            '/api/v1/abuses/{abuseId}/messages', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_post(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], api_v1_abuses_abuse_id_messages_post_request : ApiV1AbusesAbuseIdMessagesPostRequest, **kwargs) -> None:  # noqa: E501
        """Add message to an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_post(abuse_id, api_v1_abuses_abuse_id_messages_post_request, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param api_v1_abuses_abuse_id_messages_post_request: (required)
        :type api_v1_abuses_abuse_id_messages_post_request: ApiV1AbusesAbuseIdMessagesPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_abuse_id_messages_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_abuse_id_messages_post_with_http_info(abuse_id, api_v1_abuses_abuse_id_messages_post_request, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_abuse_id_messages_post_with_http_info(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], api_v1_abuses_abuse_id_messages_post_request : ApiV1AbusesAbuseIdMessagesPostRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Add message to an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_messages_post_with_http_info(abuse_id, api_v1_abuses_abuse_id_messages_post_request, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param api_v1_abuses_abuse_id_messages_post_request: (required)
        :type api_v1_abuses_abuse_id_messages_post_request: ApiV1AbusesAbuseIdMessagesPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'abuse_id',
            'api_v1_abuses_abuse_id_messages_post_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_abuse_id_messages_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['abuse_id']:
            _path_params['abuseId'] = _params['abuse_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['api_v1_abuses_abuse_id_messages_post_request'] is not None:
            _body_params = _params['api_v1_abuses_abuse_id_messages_post_request']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/abuses/{abuseId}/messages', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_abuses_abuse_id_put(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], api_v1_abuses_abuse_id_put_request : Optional[ApiV1AbusesAbuseIdPutRequest] = None, **kwargs) -> None:  # noqa: E501
        """Update an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_put(abuse_id, api_v1_abuses_abuse_id_put_request, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param api_v1_abuses_abuse_id_put_request:
        :type api_v1_abuses_abuse_id_put_request: ApiV1AbusesAbuseIdPutRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_abuse_id_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_abuse_id_put_with_http_info(abuse_id, api_v1_abuses_abuse_id_put_request, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_abuse_id_put_with_http_info(self, abuse_id : Annotated[conint(strict=True, ge=1), Field(..., description="Abuse id")], api_v1_abuses_abuse_id_put_request : Optional[ApiV1AbusesAbuseIdPutRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_abuse_id_put_with_http_info(abuse_id, api_v1_abuses_abuse_id_put_request, async_req=True)
        >>> result = thread.get()

        :param abuse_id: Abuse id (required)
        :type abuse_id: int
        :param api_v1_abuses_abuse_id_put_request:
        :type api_v1_abuses_abuse_id_put_request: ApiV1AbusesAbuseIdPutRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        _params = locals()

        _all_params = [
            'abuse_id',
            'api_v1_abuses_abuse_id_put_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_abuse_id_put" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['abuse_id']:
            _path_params['abuseId'] = _params['abuse_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['api_v1_abuses_abuse_id_put_request'] is not None:
            _body_params = _params['api_v1_abuses_abuse_id_put_request']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/abuses/{abuseId}', 'PUT',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def api_v1_abuses_post(self, api_v1_abuses_post_request : ApiV1AbusesPostRequest, **kwargs) -> ApiV1AbusesPost200Response:  # noqa: E501
        """Report an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_post(api_v1_abuses_post_request, async_req=True)
        >>> result = thread.get()

        :param api_v1_abuses_post_request: (required)
        :type api_v1_abuses_post_request: ApiV1AbusesPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1AbusesPost200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_abuses_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_abuses_post_with_http_info(api_v1_abuses_post_request, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_abuses_post_with_http_info(self, api_v1_abuses_post_request : ApiV1AbusesPostRequest, **kwargs) -> ApiResponse:  # noqa: E501
        """Report an abuse  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_abuses_post_with_http_info(api_v1_abuses_post_request, async_req=True)
        >>> result = thread.get()

        :param api_v1_abuses_post_request: (required)
        :type api_v1_abuses_post_request: ApiV1AbusesPostRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(ApiV1AbusesPost200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'api_v1_abuses_post_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_v1_abuses_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['api_v1_abuses_post_request'] is not None:
            _body_params = _params['api_v1_abuses_post_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "ApiV1AbusesPost200Response",
            '400': None,
        }

        return self.api_client.call_api(
            '/api/v1/abuses', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_abuses(self, id : Annotated[Optional[StrictInt], Field(description="only list the report with this id")] = None, predefined_reason : Annotated[Optional[conlist(StrictStr, max_items=8)], Field(description="predefined reason the listed reports should contain")] = None, search : Annotated[Optional[StrictStr], Field(description="plain search that will match with video titles, reporter names and more")] = None, state : Optional[AbuseStateSet] = None, search_reporter : Annotated[Optional[StrictStr], Field(description="only list reports of a specific reporter")] = None, search_reportee : Annotated[Optional[StrictStr], Field(description="only list reports of a specific reportee")] = None, search_video : Annotated[Optional[StrictStr], Field(description="only list reports of a specific video")] = None, search_video_channel : Annotated[Optional[StrictStr], Field(description="only list reports of a specific video channel")] = None, video_is : Annotated[Optional[StrictStr], Field(description="only list deleted or blocklisted videos")] = None, filter : Annotated[Optional[StrictStr], Field(description="only list account, comment or video reports")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort abuses by criteria")] = None, **kwargs) -> GetMyAbuses200Response:  # noqa: E501
        """List abuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abuses(id, predefined_reason, search, state, search_reporter, search_reportee, search_video, search_video_channel, video_is, filter, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param id: only list the report with this id
        :type id: int
        :param predefined_reason: predefined reason the listed reports should contain
        :type predefined_reason: List[str]
        :param search: plain search that will match with video titles, reporter names and more
        :type search: str
        :param state:
        :type state: AbuseStateSet
        :param search_reporter: only list reports of a specific reporter
        :type search_reporter: str
        :param search_reportee: only list reports of a specific reportee
        :type search_reportee: str
        :param search_video: only list reports of a specific video
        :type search_video: str
        :param search_video_channel: only list reports of a specific video channel
        :type search_video_channel: str
        :param video_is: only list deleted or blocklisted videos
        :type video_is: str
        :param filter: only list account, comment or video reports
        :type filter: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort abuses by criteria
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetMyAbuses200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_abuses_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_abuses_with_http_info(id, predefined_reason, search, state, search_reporter, search_reportee, search_video, search_video_channel, video_is, filter, start, count, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_abuses_with_http_info(self, id : Annotated[Optional[StrictInt], Field(description="only list the report with this id")] = None, predefined_reason : Annotated[Optional[conlist(StrictStr, max_items=8)], Field(description="predefined reason the listed reports should contain")] = None, search : Annotated[Optional[StrictStr], Field(description="plain search that will match with video titles, reporter names and more")] = None, state : Optional[AbuseStateSet] = None, search_reporter : Annotated[Optional[StrictStr], Field(description="only list reports of a specific reporter")] = None, search_reportee : Annotated[Optional[StrictStr], Field(description="only list reports of a specific reportee")] = None, search_video : Annotated[Optional[StrictStr], Field(description="only list reports of a specific video")] = None, search_video_channel : Annotated[Optional[StrictStr], Field(description="only list reports of a specific video channel")] = None, video_is : Annotated[Optional[StrictStr], Field(description="only list deleted or blocklisted videos")] = None, filter : Annotated[Optional[StrictStr], Field(description="only list account, comment or video reports")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort abuses by criteria")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List abuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_abuses_with_http_info(id, predefined_reason, search, state, search_reporter, search_reportee, search_video, search_video_channel, video_is, filter, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param id: only list the report with this id
        :type id: int
        :param predefined_reason: predefined reason the listed reports should contain
        :type predefined_reason: List[str]
        :param search: plain search that will match with video titles, reporter names and more
        :type search: str
        :param state:
        :type state: AbuseStateSet
        :param search_reporter: only list reports of a specific reporter
        :type search_reporter: str
        :param search_reportee: only list reports of a specific reportee
        :type search_reportee: str
        :param search_video: only list reports of a specific video
        :type search_video: str
        :param search_video_channel: only list reports of a specific video channel
        :type search_video_channel: str
        :param video_is: only list deleted or blocklisted videos
        :type video_is: str
        :param filter: only list account, comment or video reports
        :type filter: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort abuses by criteria
        :type sort: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetMyAbuses200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'predefined_reason',
            'search',
            'state',
            'search_reporter',
            'search_reportee',
            'search_video',
            'search_video_channel',
            'video_is',
            'filter',
            'start',
            'count',
            'sort'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_abuses" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        if _params.get('predefined_reason') is not None:  # noqa: E501
            _query_params.append(('predefinedReason', _params['predefined_reason']))
            _collection_formats['predefinedReason'] = 'multi'

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('state') is not None:  # noqa: E501
            _query_params.append(('state', _params['state'].value))

        if _params.get('search_reporter') is not None:  # noqa: E501
            _query_params.append(('searchReporter', _params['search_reporter']))

        if _params.get('search_reportee') is not None:  # noqa: E501
            _query_params.append(('searchReportee', _params['search_reportee']))

        if _params.get('search_video') is not None:  # noqa: E501
            _query_params.append(('searchVideo', _params['search_video']))

        if _params.get('search_video_channel') is not None:  # noqa: E501
            _query_params.append(('searchVideoChannel', _params['search_video_channel']))

        if _params.get('video_is') is not None:  # noqa: E501
            _query_params.append(('videoIs', _params['video_is'].value))

        if _params.get('filter') is not None:  # noqa: E501
            _query_params.append(('filter', _params['filter'].value))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "GetMyAbuses200Response",
        }

        return self.api_client.call_api(
            '/api/v1/abuses', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def get_my_abuses(self, id : Annotated[Optional[StrictInt], Field(description="only list the report with this id")] = None, state : Optional[AbuseStateSet] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort abuses by criteria")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, **kwargs) -> GetMyAbuses200Response:  # noqa: E501
        """List my abuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_my_abuses(id, state, sort, start, count, async_req=True)
        >>> result = thread.get()

        :param id: only list the report with this id
        :type id: int
        :param state:
        :type state: AbuseStateSet
        :param sort: Sort abuses by criteria
        :type sort: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetMyAbuses200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_my_abuses_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_my_abuses_with_http_info(id, state, sort, start, count, **kwargs)  # noqa: E501

    @validate_arguments
    def get_my_abuses_with_http_info(self, id : Annotated[Optional[StrictInt], Field(description="only list the report with this id")] = None, state : Optional[AbuseStateSet] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort abuses by criteria")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List my abuses  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_my_abuses_with_http_info(id, state, sort, start, count, async_req=True)
        >>> result = thread.get()

        :param id: only list the report with this id
        :type id: int
        :param state:
        :type state: AbuseStateSet
        :param sort: Sort abuses by criteria
        :type sort: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(GetMyAbuses200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id',
            'state',
            'sort',
            'start',
            'count'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_my_abuses" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('id') is not None:  # noqa: E501
            _query_params.append(('id', _params['id']))

        if _params.get('state') is not None:  # noqa: E501
            _query_params.append(('state', _params['state'].value))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "GetMyAbuses200Response",
        }

        return self.api_client.call_api(
            '/api/v1/users/me/abuses', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
