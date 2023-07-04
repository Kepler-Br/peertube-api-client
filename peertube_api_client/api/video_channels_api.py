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

from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr, conint

from typing import Any, Optional, Union

from peertube_api_client.models.add_video_channel200_response import AddVideoChannel200Response
from peertube_api_client.models.api_v1_users_me_avatar_pick_post200_response import ApiV1UsersMeAvatarPickPost200Response
from peertube_api_client.models.api_v1_video_channels_channel_handle_banner_pick_post200_response import ApiV1VideoChannelsChannelHandleBannerPickPost200Response
from peertube_api_client.models.api_v1_video_channels_channel_handle_video_playlists_get200_response import ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
from peertube_api_client.models.get_account_followers200_response import GetAccountFollowers200Response
from peertube_api_client.models.import_videos_in_channel_create import ImportVideosInChannelCreate
from peertube_api_client.models.video_channel import VideoChannel
from peertube_api_client.models.video_channel_create import VideoChannelCreate
from peertube_api_client.models.video_channel_list import VideoChannelList
from peertube_api_client.models.video_channel_sync_list import VideoChannelSyncList
from peertube_api_client.models.video_channel_update import VideoChannelUpdate
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_playlist_type_set import VideoPlaylistTypeSet
from peertube_api_client.models.video_privacy_set import VideoPrivacySet

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VideoChannelsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_video_channel(self, video_channel_create : Optional[VideoChannelCreate] = None, **kwargs) -> AddVideoChannel200Response:  # noqa: E501
        """Create a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_video_channel(video_channel_create, async_req=True)
        >>> result = thread.get()

        :param video_channel_create:
        :type video_channel_create: VideoChannelCreate
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddVideoChannel200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_video_channel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_video_channel_with_http_info(video_channel_create, **kwargs)  # noqa: E501

    @validate_arguments
    def add_video_channel_with_http_info(self, video_channel_create : Optional[VideoChannelCreate] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_video_channel_with_http_info(video_channel_create, async_req=True)
        >>> result = thread.get()

        :param video_channel_create:
        :type video_channel_create: VideoChannelCreate
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
        :rtype: tuple(AddVideoChannel200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'video_channel_create'
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
                    " to method add_video_channel" % _key
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
        if _params['video_channel_create'] is not None:
            _body_params = _params['video_channel_create']

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
            '200': "AddVideoChannel200Response",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels', 'POST',
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
    def api_v1_accounts_name_video_channel_syncs_get(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> VideoChannelSyncList:  # noqa: E501
        """List the synchronizations of video channels of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_channel_syncs_get(name, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: VideoChannelSyncList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_accounts_name_video_channel_syncs_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_accounts_name_video_channel_syncs_get_with_http_info(name, start, count, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_accounts_name_video_channel_syncs_get_with_http_info(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List the synchronizations of video channels of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_channel_syncs_get_with_http_info(name, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: tuple(VideoChannelSyncList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
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
                    " to method api_v1_accounts_name_video_channel_syncs_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['name']:
            _path_params['name'] = _params['name']


        # process the query parameters
        _query_params = []
        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoChannelSyncList",
        }

        return self.api_client.call_api(
            '/api/v1/accounts/{name}/video-channel-syncs', 'GET',
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
    def api_v1_accounts_name_video_channels_get(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], with_stats : Annotated[Optional[StrictBool], Field(description="include daily view statistics for the last 30 days and total views (only if authentified as the account user)")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> VideoChannelList:  # noqa: E501
        """List video channels of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_channels_get(name, with_stats, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param with_stats: include daily view statistics for the last 30 days and total views (only if authentified as the account user)
        :type with_stats: bool
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: VideoChannelList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_accounts_name_video_channels_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_accounts_name_video_channels_get_with_http_info(name, with_stats, start, count, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_accounts_name_video_channels_get_with_http_info(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], with_stats : Annotated[Optional[StrictBool], Field(description="include daily view statistics for the last 30 days and total views (only if authentified as the account user)")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List video channels of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_channels_get_with_http_info(name, with_stats, start, count, sort, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param with_stats: include daily view statistics for the last 30 days and total views (only if authentified as the account user)
        :type with_stats: bool
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: tuple(VideoChannelList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'name',
            'with_stats',
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
                    " to method api_v1_accounts_name_video_channels_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['name']:
            _path_params['name'] = _params['name']


        # process the query parameters
        _query_params = []
        if _params.get('with_stats') is not None:  # noqa: E501
            _query_params.append(('withStats', _params['with_stats']))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoChannelList",
        }

        return self.api_client.call_api(
            '/api/v1/accounts/{name}/video-channels', 'GET',
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
    def api_v1_video_channels_channel_handle_avatar_delete(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> None:  # noqa: E501
        """Delete channel avatar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_avatar_delete(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_avatar_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_avatar_delete_with_http_info(channel_handle, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_avatar_delete_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete channel avatar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_avatar_delete_with_http_info(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            'channel_handle'
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
                    " to method api_v1_video_channels_channel_handle_avatar_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


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
            '/api/v1/video-channels/{channelHandle}/avatar', 'DELETE',
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
    def api_v1_video_channels_channel_handle_avatar_pick_post(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], avatarfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The file to upload.")] = None, **kwargs) -> ApiV1UsersMeAvatarPickPost200Response:  # noqa: E501
        """Update channel avatar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_avatar_pick_post(channel_handle, avatarfile, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param avatarfile: The file to upload.
        :type avatarfile: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1UsersMeAvatarPickPost200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_avatar_pick_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_avatar_pick_post_with_http_info(channel_handle, avatarfile, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_avatar_pick_post_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], avatarfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The file to upload.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update channel avatar  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_avatar_pick_post_with_http_info(channel_handle, avatarfile, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param avatarfile: The file to upload.
        :type avatarfile: bytearray
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
        :rtype: tuple(ApiV1UsersMeAvatarPickPost200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle',
            'avatarfile'
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
                    " to method api_v1_video_channels_channel_handle_avatar_pick_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['avatarfile']:
            _files['avatarfile'] = _params['avatarfile']

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "ApiV1UsersMeAvatarPickPost200Response",
            '413': None,
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}/avatar/pick', 'POST',
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
    def api_v1_video_channels_channel_handle_banner_delete(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> None:  # noqa: E501
        """Delete channel banner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_banner_delete(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_banner_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_banner_delete_with_http_info(channel_handle, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_banner_delete_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete channel banner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_banner_delete_with_http_info(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            'channel_handle'
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
                    " to method api_v1_video_channels_channel_handle_banner_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


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
            '/api/v1/video-channels/{channelHandle}/banner', 'DELETE',
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
    def api_v1_video_channels_channel_handle_banner_pick_post(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], bannerfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The file to upload.")] = None, **kwargs) -> ApiV1VideoChannelsChannelHandleBannerPickPost200Response:  # noqa: E501
        """Update channel banner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_banner_pick_post(channel_handle, bannerfile, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param bannerfile: The file to upload.
        :type bannerfile: bytearray
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1VideoChannelsChannelHandleBannerPickPost200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_banner_pick_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_banner_pick_post_with_http_info(channel_handle, bannerfile, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_banner_pick_post_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], bannerfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="The file to upload.")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update channel banner  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_banner_pick_post_with_http_info(channel_handle, bannerfile, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param bannerfile: The file to upload.
        :type bannerfile: bytearray
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
        :rtype: tuple(ApiV1VideoChannelsChannelHandleBannerPickPost200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle',
            'bannerfile'
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
                    " to method api_v1_video_channels_channel_handle_banner_pick_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['bannerfile']:
            _files['bannerfile'] = _params['bannerfile']

        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "ApiV1VideoChannelsChannelHandleBannerPickPost200Response",
            '413': None,
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}/banner/pick', 'POST',
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
    def api_v1_video_channels_channel_handle_import_videos_post(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], import_videos_in_channel_create : Optional[ImportVideosInChannelCreate] = None, **kwargs) -> None:  # noqa: E501
        """Import videos in channel  # noqa: E501

        Import a remote channel/playlist videos into a channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_import_videos_post(channel_handle, import_videos_in_channel_create, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param import_videos_in_channel_create:
        :type import_videos_in_channel_create: ImportVideosInChannelCreate
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
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_import_videos_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_import_videos_post_with_http_info(channel_handle, import_videos_in_channel_create, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_import_videos_post_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], import_videos_in_channel_create : Optional[ImportVideosInChannelCreate] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Import videos in channel  # noqa: E501

        Import a remote channel/playlist videos into a channel  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_import_videos_post_with_http_info(channel_handle, import_videos_in_channel_create, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param import_videos_in_channel_create:
        :type import_videos_in_channel_create: ImportVideosInChannelCreate
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
            'channel_handle',
            'import_videos_in_channel_create'
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
                    " to method api_v1_video_channels_channel_handle_import_videos_post" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['import_videos_in_channel_create'] is not None:
            _body_params = _params['import_videos_in_channel_create']

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
            '/api/v1/video-channels/{channelHandle}/import-videos', 'POST',
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
    def api_v1_video_channels_channel_handle_video_playlists_get(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response:  # noqa: E501
        """List playlists of a channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_video_playlists_get(channel_handle, start, count, sort, playlist_type, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
        :type sort: str
        :param playlist_type:
        :type playlist_type: VideoPlaylistTypeSet
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_video_channels_channel_handle_video_playlists_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_channels_channel_handle_video_playlists_get_with_http_info(channel_handle, start, count, sort, playlist_type, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_channels_channel_handle_video_playlists_get_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List playlists of a channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_channels_channel_handle_video_playlists_get_with_http_info(channel_handle, start, count, sort, playlist_type, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
        :type sort: str
        :param playlist_type:
        :type playlist_type: VideoPlaylistTypeSet
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
        :rtype: tuple(ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle',
            'start',
            'count',
            'sort',
            'playlist_type'
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
                    " to method api_v1_video_channels_channel_handle_video_playlists_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

        if _params.get('playlist_type') is not None:  # noqa: E501
            _query_params.append(('playlistType', _params['playlist_type'].value))

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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}/video-playlists', 'GET',
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
    def del_video_channel(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> None:  # noqa: E501
        """Delete a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video_channel(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            raise ValueError("Error! Please call the del_video_channel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.del_video_channel_with_http_info(channel_handle, **kwargs)  # noqa: E501

    @validate_arguments
    def del_video_channel_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video_channel_with_http_info(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
            'channel_handle'
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
                    " to method del_video_channel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


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
            '/api/v1/video-channels/{channelHandle}', 'DELETE',
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
    def get_video_channel(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> VideoChannel:  # noqa: E501
        """Get a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VideoChannel
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_channel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_channel_with_http_info(channel_handle, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_channel_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel_with_http_info(channel_handle, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
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
        :rtype: tuple(VideoChannel, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle'
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
                    " to method get_video_channel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoChannel",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}', 'GET',
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
    def get_video_channel_followers(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort followers by criteria")] = None, search : Annotated[Optional[StrictStr], Field(description="Plain text search, applied to various parts of the model depending on endpoint")] = None, **kwargs) -> GetAccountFollowers200Response:  # noqa: E501
        """List followers of a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel_followers(channel_handle, start, count, sort, search, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort followers by criteria
        :type sort: str
        :param search: Plain text search, applied to various parts of the model depending on endpoint
        :type search: str
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: GetAccountFollowers200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_channel_followers_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_channel_followers_with_http_info(channel_handle, start, count, sort, search, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_channel_followers_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort followers by criteria")] = None, search : Annotated[Optional[StrictStr], Field(description="Plain text search, applied to various parts of the model depending on endpoint")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List followers of a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel_followers_with_http_info(channel_handle, start, count, sort, search, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort followers by criteria
        :type sort: str
        :param search: Plain text search, applied to various parts of the model depending on endpoint
        :type search: str
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
        :rtype: tuple(GetAccountFollowers200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle',
            'start',
            'count',
            'sort',
            'search'
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
                    " to method get_video_channel_followers" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

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
            '200': "GetAccountFollowers200Response",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}/followers', 'GET',
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
    def get_video_channel_videos(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> VideoListResponse:  # noqa: E501
        """List videos of a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel_videos(channel_handle, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param category_one_of: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category_one_of: GetAccountVideosCategoryOneOfParameter
        :param is_live: whether or not the video is a live
        :type is_live: bool
        :param tags_one_of: tag(s) of the video
        :type tags_one_of: GetAccountVideosTagsOneOfParameter
        :param tags_all_of: tag(s) of the video, where all should be present in the video
        :type tags_all_of: GetAccountVideosTagsAllOfParameter
        :param licence_one_of: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence_one_of: GetAccountVideosLicenceOneOfParameter
        :param language_one_of: language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
        :type language_one_of: GetAccountVideosLanguageOneOfParameter
        :param nsfw: whether to include nsfw videos, if any
        :type nsfw: str
        :param is_local: **PeerTube >= 4.0** Display only local or remote videos
        :type is_local: bool
        :param include: **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
        :type include: int
        :param privacy_one_of: **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
        :type privacy_one_of: VideoPrivacySet
        :param has_hls_files: **PeerTube >= 4.0** Display only videos that have HLS files
        :type has_hls_files: bool
        :param has_webtorrent_files: **PeerTube >= 4.0** Display only videos that have WebTorrent files
        :type has_webtorrent_files: bool
        :param skip_count: if you don't need the `total` in the response
        :type skip_count: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort:
        :type sort: str
        :param exclude_already_watched: Whether or not to exclude videos that are in the user's video history
        :type exclude_already_watched: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VideoListResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_channel_videos_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_channel_videos_with_http_info(channel_handle, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_channel_videos_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List videos of a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channel_videos_with_http_info(channel_handle, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param category_one_of: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category_one_of: GetAccountVideosCategoryOneOfParameter
        :param is_live: whether or not the video is a live
        :type is_live: bool
        :param tags_one_of: tag(s) of the video
        :type tags_one_of: GetAccountVideosTagsOneOfParameter
        :param tags_all_of: tag(s) of the video, where all should be present in the video
        :type tags_all_of: GetAccountVideosTagsAllOfParameter
        :param licence_one_of: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence_one_of: GetAccountVideosLicenceOneOfParameter
        :param language_one_of: language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language
        :type language_one_of: GetAccountVideosLanguageOneOfParameter
        :param nsfw: whether to include nsfw videos, if any
        :type nsfw: str
        :param is_local: **PeerTube >= 4.0** Display only local or remote videos
        :type is_local: bool
        :param include: **PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES 
        :type include: int
        :param privacy_one_of: **PeerTube >= 4.0** Display only videos in this specific privacy/privacies
        :type privacy_one_of: VideoPrivacySet
        :param has_hls_files: **PeerTube >= 4.0** Display only videos that have HLS files
        :type has_hls_files: bool
        :param has_webtorrent_files: **PeerTube >= 4.0** Display only videos that have WebTorrent files
        :type has_webtorrent_files: bool
        :param skip_count: if you don't need the `total` in the response
        :type skip_count: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort:
        :type sort: str
        :param exclude_already_watched: Whether or not to exclude videos that are in the user's video history
        :type exclude_already_watched: bool
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
        :rtype: tuple(VideoListResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_handle',
            'category_one_of',
            'is_live',
            'tags_one_of',
            'tags_all_of',
            'licence_one_of',
            'language_one_of',
            'nsfw',
            'is_local',
            'include',
            'privacy_one_of',
            'has_hls_files',
            'has_webtorrent_files',
            'skip_count',
            'start',
            'count',
            'sort',
            'exclude_already_watched'
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
                    " to method get_video_channel_videos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        if _params.get('category_one_of') is not None:  # noqa: E501
            _query_params.append(('categoryOneOf', _params['category_one_of']))

        if _params.get('is_live') is not None:  # noqa: E501
            _query_params.append(('isLive', _params['is_live']))

        if _params.get('tags_one_of') is not None:  # noqa: E501
            _query_params.append(('tagsOneOf', _params['tags_one_of']))

        if _params.get('tags_all_of') is not None:  # noqa: E501
            _query_params.append(('tagsAllOf', _params['tags_all_of']))

        if _params.get('licence_one_of') is not None:  # noqa: E501
            _query_params.append(('licenceOneOf', _params['licence_one_of']))

        if _params.get('language_one_of') is not None:  # noqa: E501
            _query_params.append(('languageOneOf', _params['language_one_of']))

        if _params.get('nsfw') is not None:  # noqa: E501
            _query_params.append(('nsfw', _params['nsfw'].value))

        if _params.get('is_local') is not None:  # noqa: E501
            _query_params.append(('isLocal', _params['is_local']))

        if _params.get('include') is not None:  # noqa: E501
            _query_params.append(('include', _params['include'].value))

        if _params.get('privacy_one_of') is not None:  # noqa: E501
            _query_params.append(('privacyOneOf', _params['privacy_one_of'].value))

        if _params.get('has_hls_files') is not None:  # noqa: E501
            _query_params.append(('hasHLSFiles', _params['has_hls_files']))

        if _params.get('has_webtorrent_files') is not None:  # noqa: E501
            _query_params.append(('hasWebtorrentFiles', _params['has_webtorrent_files']))

        if _params.get('skip_count') is not None:  # noqa: E501
            _query_params.append(('skipCount', _params['skip_count'].value))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('exclude_already_watched') is not None:  # noqa: E501
            _query_params.append(('excludeAlreadyWatched', _params['exclude_already_watched']))

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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoListResponse",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels/{channelHandle}/videos', 'GET',
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
    def get_video_channels(self, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> VideoChannelList:  # noqa: E501
        """List video channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channels(start, count, sort, async_req=True)
        >>> result = thread.get()

        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: VideoChannelList
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_channels_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_channels_with_http_info(start, count, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_channels_with_http_info(self, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List video channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_channels_with_http_info(start, count, sort, async_req=True)
        >>> result = thread.get()

        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
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
        :rtype: tuple(VideoChannelList, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method get_video_channels" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort']))

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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoChannelList",
        }

        return self.api_client.call_api(
            '/api/v1/video-channels', 'GET',
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
    def put_video_channel(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], video_channel_update : Optional[VideoChannelUpdate] = None, **kwargs) -> None:  # noqa: E501
        """Update a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video_channel(channel_handle, video_channel_update, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param video_channel_update:
        :type video_channel_update: VideoChannelUpdate
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
            raise ValueError("Error! Please call the put_video_channel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.put_video_channel_with_http_info(channel_handle, video_channel_update, **kwargs)  # noqa: E501

    @validate_arguments
    def put_video_channel_with_http_info(self, channel_handle : Annotated[StrictStr, Field(..., description="The video channel handle")], video_channel_update : Optional[VideoChannelUpdate] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a video channel  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video_channel_with_http_info(channel_handle, video_channel_update, async_req=True)
        >>> result = thread.get()

        :param channel_handle: The video channel handle (required)
        :type channel_handle: str
        :param video_channel_update:
        :type video_channel_update: VideoChannelUpdate
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
            'channel_handle',
            'video_channel_update'
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
                    " to method put_video_channel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['channel_handle']:
            _path_params['channelHandle'] = _params['channel_handle']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['video_channel_update'] is not None:
            _body_params = _params['video_channel_update']

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
            '/api/v1/video-channels/{channelHandle}', 'PUT',
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
