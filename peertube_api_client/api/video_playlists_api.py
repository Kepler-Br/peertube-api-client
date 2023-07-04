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

from pydantic import Field, StrictBytes, StrictStr, conint, conlist, constr

from typing import Any, List, Optional, Union

from peertube_api_client.models.add_playlist200_response import AddPlaylist200Response
from peertube_api_client.models.add_video_playlist_video200_response import AddVideoPlaylistVideo200Response
from peertube_api_client.models.add_video_playlist_video_request import AddVideoPlaylistVideoRequest
from peertube_api_client.models.api_v1_users_me_video_playlists_videos_exist_get200_response import ApiV1UsersMeVideoPlaylistsVideosExistGet200Response
from peertube_api_client.models.api_v1_video_channels_channel_handle_video_playlists_get200_response import ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
from peertube_api_client.models.put_video_playlist_video_request import PutVideoPlaylistVideoRequest
from peertube_api_client.models.reorder_video_playlist_request import ReorderVideoPlaylistRequest
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_playlist import VideoPlaylist
from peertube_api_client.models.video_playlist_privacy_set import VideoPlaylistPrivacySet
from peertube_api_client.models.video_playlist_type_set import VideoPlaylistTypeSet

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VideoPlaylistsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_playlist(self, display_name : Annotated[constr(strict=True, max_length=120, min_length=1), Field(..., description="Video playlist display name")], thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video playlist thumbnail file")] = None, privacy : Optional[VideoPlaylistPrivacySet] = None, description : Annotated[Optional[constr(strict=True, max_length=1000, min_length=3)], Field(description="Video playlist description")] = None, video_channel_id : Optional[Any] = None, **kwargs) -> AddPlaylist200Response:  # noqa: E501
        """Create a video playlist  # noqa: E501

        If the video playlist is set as public, `videoChannelId` is mandatory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_playlist(display_name, thumbnailfile, privacy, description, video_channel_id, async_req=True)
        >>> result = thread.get()

        :param display_name: Video playlist display name (required)
        :type display_name: str
        :param thumbnailfile: Video playlist thumbnail file
        :type thumbnailfile: bytearray
        :param privacy:
        :type privacy: VideoPlaylistPrivacySet
        :param description: Video playlist description
        :type description: str
        :param video_channel_id:
        :type video_channel_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddPlaylist200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_playlist_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_playlist_with_http_info(display_name, thumbnailfile, privacy, description, video_channel_id, **kwargs)  # noqa: E501

    @validate_arguments
    def add_playlist_with_http_info(self, display_name : Annotated[constr(strict=True, max_length=120, min_length=1), Field(..., description="Video playlist display name")], thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video playlist thumbnail file")] = None, privacy : Optional[VideoPlaylistPrivacySet] = None, description : Annotated[Optional[constr(strict=True, max_length=1000, min_length=3)], Field(description="Video playlist description")] = None, video_channel_id : Optional[Any] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a video playlist  # noqa: E501

        If the video playlist is set as public, `videoChannelId` is mandatory.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_playlist_with_http_info(display_name, thumbnailfile, privacy, description, video_channel_id, async_req=True)
        >>> result = thread.get()

        :param display_name: Video playlist display name (required)
        :type display_name: str
        :param thumbnailfile: Video playlist thumbnail file
        :type thumbnailfile: bytearray
        :param privacy:
        :type privacy: VideoPlaylistPrivacySet
        :param description: Video playlist description
        :type description: str
        :param video_channel_id:
        :type video_channel_id: int
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
        :rtype: tuple(AddPlaylist200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'display_name',
            'thumbnailfile',
            'privacy',
            'description',
            'video_channel_id'
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
                    " to method add_playlist" % _key
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
        if _params['display_name']:
            _form_params.append(('displayName', _params['display_name']))

        if _params['thumbnailfile']:
            _files['thumbnailfile'] = _params['thumbnailfile']

        if _params['privacy']:
            _form_params.append(('privacy', _params['privacy']))

        if _params['description']:
            _form_params.append(('description', _params['description']))

        if _params['video_channel_id']:
            _form_params.append(('videoChannelId', _params['video_channel_id']))

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
            '200': "AddPlaylist200Response",
        }

        return self.api_client.call_api(
            '/api/v1/video-playlists', 'POST',
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
    def add_video_playlist_video(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], add_video_playlist_video_request : Optional[AddVideoPlaylistVideoRequest] = None, **kwargs) -> AddVideoPlaylistVideo200Response:  # noqa: E501
        """Add a video in a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_video_playlist_video(playlist_id, add_video_playlist_video_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param add_video_playlist_video_request:
        :type add_video_playlist_video_request: AddVideoPlaylistVideoRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AddVideoPlaylistVideo200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_video_playlist_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_video_playlist_video_with_http_info(playlist_id, add_video_playlist_video_request, **kwargs)  # noqa: E501

    @validate_arguments
    def add_video_playlist_video_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], add_video_playlist_video_request : Optional[AddVideoPlaylistVideoRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Add a video in a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_video_playlist_video_with_http_info(playlist_id, add_video_playlist_video_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param add_video_playlist_video_request:
        :type add_video_playlist_video_request: AddVideoPlaylistVideoRequest
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
        :rtype: tuple(AddVideoPlaylistVideo200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'playlist_id',
            'add_video_playlist_video_request'
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
                    " to method add_video_playlist_video" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['add_video_playlist_video_request'] is not None:
            _body_params = _params['add_video_playlist_video_request']

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
            '200': "AddVideoPlaylistVideo200Response",
        }

        return self.api_client.call_api(
            '/api/v1/video-playlists/{playlistId}/videos', 'POST',
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
    def api_v1_accounts_name_video_playlists_get(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, search : Annotated[Optional[StrictStr], Field(description="Plain text search, applied to various parts of the model depending on endpoint")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response:  # noqa: E501
        """List playlists of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_playlists_get(name, start, count, sort, search, playlist_type, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
        :type sort: str
        :param search: Plain text search, applied to various parts of the model depending on endpoint
        :type search: str
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
            raise ValueError("Error! Please call the api_v1_accounts_name_video_playlists_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_accounts_name_video_playlists_get_with_http_info(name, start, count, sort, search, playlist_type, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_accounts_name_video_playlists_get_with_http_info(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, search : Annotated[Optional[StrictStr], Field(description="Plain text search, applied to various parts of the model depending on endpoint")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List playlists of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_accounts_name_video_playlists_get_with_http_info(name, start, count, sort, search, playlist_type, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param sort: Sort column
        :type sort: str
        :param search: Plain text search, applied to various parts of the model depending on endpoint
        :type search: str
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
            'name',
            'start',
            'count',
            'sort',
            'search',
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
                    " to method api_v1_accounts_name_video_playlists_get" % _key
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

        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

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
            '/api/v1/accounts/{name}/video-playlists', 'GET',
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
    def api_v1_users_me_video_playlists_videos_exist_get(self, video_ids : Annotated[conlist(conint(strict=True, ge=1)), Field(..., description="The video ids to check")], **kwargs) -> ApiV1UsersMeVideoPlaylistsVideosExistGet200Response:  # noqa: E501
        """Check video exists in my playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_users_me_video_playlists_videos_exist_get(video_ids, async_req=True)
        >>> result = thread.get()

        :param video_ids: The video ids to check (required)
        :type video_ids: List[int]
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1UsersMeVideoPlaylistsVideosExistGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_users_me_video_playlists_videos_exist_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_users_me_video_playlists_videos_exist_get_with_http_info(video_ids, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_users_me_video_playlists_videos_exist_get_with_http_info(self, video_ids : Annotated[conlist(conint(strict=True, ge=1)), Field(..., description="The video ids to check")], **kwargs) -> ApiResponse:  # noqa: E501
        """Check video exists in my playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_users_me_video_playlists_videos_exist_get_with_http_info(video_ids, async_req=True)
        >>> result = thread.get()

        :param video_ids: The video ids to check (required)
        :type video_ids: List[int]
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
        :rtype: tuple(ApiV1UsersMeVideoPlaylistsVideosExistGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'video_ids'
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
                    " to method api_v1_users_me_video_playlists_videos_exist_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('video_ids') is not None:  # noqa: E501
            _query_params.append(('videoIds', _params['video_ids']))
            _collection_formats['videoIds'] = 'multi'

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
            '200': "ApiV1UsersMeVideoPlaylistsVideosExistGet200Response",
        }

        return self.api_client.call_api(
            '/api/v1/users/me/video-playlists/videos-exist', 'GET',
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
    def api_v1_video_playlists_playlist_id_delete(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], **kwargs) -> None:  # noqa: E501
        """Delete a video playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_delete(playlist_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
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
            raise ValueError("Error! Please call the api_v1_video_playlists_playlist_id_delete_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_playlists_playlist_id_delete_with_http_info(playlist_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_playlists_playlist_id_delete_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a video playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_delete_with_http_info(playlist_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
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
            'playlist_id'
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
                    " to method api_v1_video_playlists_playlist_id_delete" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


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
            '/api/v1/video-playlists/{playlistId}', 'DELETE',
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
    def api_v1_video_playlists_playlist_id_get(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], **kwargs) -> VideoPlaylist:  # noqa: E501
        """Get a video playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_get(playlist_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VideoPlaylist
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_video_playlists_playlist_id_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_playlists_playlist_id_get_with_http_info(playlist_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_playlists_playlist_id_get_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get a video playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_get_with_http_info(playlist_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
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
        :rtype: tuple(VideoPlaylist, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'playlist_id'
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
                    " to method api_v1_video_playlists_playlist_id_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


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
            '200': "VideoPlaylist",
        }

        return self.api_client.call_api(
            '/api/v1/video-playlists/{playlistId}', 'GET',
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
    def api_v1_video_playlists_playlist_id_put(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], display_name : Annotated[Optional[constr(strict=True, max_length=120, min_length=1)], Field(description="Video playlist display name")] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video playlist thumbnail file")] = None, privacy : Optional[VideoPlaylistPrivacySet] = None, description : Annotated[Optional[StrictStr], Field(description="Video playlist description")] = None, video_channel_id : Optional[Any] = None, **kwargs) -> None:  # noqa: E501
        """Update a video playlist  # noqa: E501

        If the video playlist is set as public, the playlist must have a assigned channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_put(playlist_id, display_name, thumbnailfile, privacy, description, video_channel_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param display_name: Video playlist display name
        :type display_name: str
        :param thumbnailfile: Video playlist thumbnail file
        :type thumbnailfile: bytearray
        :param privacy:
        :type privacy: VideoPlaylistPrivacySet
        :param description: Video playlist description
        :type description: str
        :param video_channel_id:
        :type video_channel_id: int
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
            raise ValueError("Error! Please call the api_v1_video_playlists_playlist_id_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_video_playlists_playlist_id_put_with_http_info(playlist_id, display_name, thumbnailfile, privacy, description, video_channel_id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_video_playlists_playlist_id_put_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], display_name : Annotated[Optional[constr(strict=True, max_length=120, min_length=1)], Field(description="Video playlist display name")] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video playlist thumbnail file")] = None, privacy : Optional[VideoPlaylistPrivacySet] = None, description : Annotated[Optional[StrictStr], Field(description="Video playlist description")] = None, video_channel_id : Optional[Any] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a video playlist  # noqa: E501

        If the video playlist is set as public, the playlist must have a assigned channel.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_video_playlists_playlist_id_put_with_http_info(playlist_id, display_name, thumbnailfile, privacy, description, video_channel_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param display_name: Video playlist display name
        :type display_name: str
        :param thumbnailfile: Video playlist thumbnail file
        :type thumbnailfile: bytearray
        :param privacy:
        :type privacy: VideoPlaylistPrivacySet
        :param description: Video playlist description
        :type description: str
        :param video_channel_id:
        :type video_channel_id: int
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
            'playlist_id',
            'display_name',
            'thumbnailfile',
            'privacy',
            'description',
            'video_channel_id'
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
                    " to method api_v1_video_playlists_playlist_id_put" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        if _params['display_name']:
            _form_params.append(('displayName', _params['display_name']))

        if _params['thumbnailfile']:
            _files['thumbnailfile'] = _params['thumbnailfile']

        if _params['privacy']:
            _form_params.append(('privacy', _params['privacy']))

        if _params['description']:
            _form_params.append(('description', _params['description']))

        if _params['video_channel_id']:
            _form_params.append(('videoChannelId', _params['video_channel_id']))

        # process the body parameter
        _body_params = None
        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['multipart/form-data']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/video-playlists/{playlistId}', 'PUT',
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
    def del_video_playlist_video(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], playlist_element_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist element id")], **kwargs) -> None:  # noqa: E501
        """Delete an element from a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video_playlist_video(playlist_id, playlist_element_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param playlist_element_id: Playlist element id (required)
        :type playlist_element_id: int
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
            raise ValueError("Error! Please call the del_video_playlist_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.del_video_playlist_video_with_http_info(playlist_id, playlist_element_id, **kwargs)  # noqa: E501

    @validate_arguments
    def del_video_playlist_video_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], playlist_element_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist element id")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete an element from a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video_playlist_video_with_http_info(playlist_id, playlist_element_id, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param playlist_element_id: Playlist element id (required)
        :type playlist_element_id: int
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
            'playlist_id',
            'playlist_element_id'
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
                    " to method del_video_playlist_video" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']

        if _params['playlist_element_id']:
            _path_params['playlistElementId'] = _params['playlist_element_id']


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
            '/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}', 'DELETE',
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
    def get_playlist_privacy_policies(self, **kwargs) -> List[str]:  # noqa: E501
        """List available playlist privacy policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_playlist_privacy_policies(async_req=True)
        >>> result = thread.get()

        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: List[str]
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_playlist_privacy_policies_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_playlist_privacy_policies_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_playlist_privacy_policies_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List available playlist privacy policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_playlist_privacy_policies_with_http_info(async_req=True)
        >>> result = thread.get()

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
        :rtype: tuple(List[str], status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
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
                    " to method get_playlist_privacy_policies" % _key
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
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "List[str]",
        }

        return self.api_client.call_api(
            '/api/v1/video-playlists/privacies', 'GET',
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
    def get_playlists(self, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response:  # noqa: E501
        """List video playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_playlists(start, count, sort, playlist_type, async_req=True)
        >>> result = thread.get()

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
            raise ValueError("Error! Please call the get_playlists_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_playlists_with_http_info(start, count, sort, playlist_type, **kwargs)  # noqa: E501

    @validate_arguments
    def get_playlists_with_http_info(self, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, playlist_type : Optional[VideoPlaylistTypeSet] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List video playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_playlists_with_http_info(start, count, sort, playlist_type, async_req=True)
        >>> result = thread.get()

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
                    " to method get_playlists" % _key
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
            '/api/v1/video-playlists', 'GET',
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
    def get_video_playlist_videos(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, **kwargs) -> VideoListResponse:  # noqa: E501
        """List videos of a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_playlist_videos(playlist_id, start, count, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
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
        :rtype: VideoListResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_playlist_videos_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_playlist_videos_with_http_info(playlist_id, start, count, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_playlist_videos_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List videos of a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_playlist_videos_with_http_info(playlist_id, start, count, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
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
        :rtype: tuple(VideoListResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'playlist_id',
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
                    " to method get_video_playlist_videos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


        # process the query parameters
        _query_params = []
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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoListResponse",
        }

        return self.api_client.call_api(
            '/api/v1/video-playlists/{playlistId}/videos', 'GET',
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
    def put_video_playlist_video(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], playlist_element_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist element id")], put_video_playlist_video_request : Optional[PutVideoPlaylistVideoRequest] = None, **kwargs) -> None:  # noqa: E501
        """Update a playlist element  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video_playlist_video(playlist_id, playlist_element_id, put_video_playlist_video_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param playlist_element_id: Playlist element id (required)
        :type playlist_element_id: int
        :param put_video_playlist_video_request:
        :type put_video_playlist_video_request: PutVideoPlaylistVideoRequest
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
            raise ValueError("Error! Please call the put_video_playlist_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.put_video_playlist_video_with_http_info(playlist_id, playlist_element_id, put_video_playlist_video_request, **kwargs)  # noqa: E501

    @validate_arguments
    def put_video_playlist_video_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], playlist_element_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist element id")], put_video_playlist_video_request : Optional[PutVideoPlaylistVideoRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a playlist element  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video_playlist_video_with_http_info(playlist_id, playlist_element_id, put_video_playlist_video_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param playlist_element_id: Playlist element id (required)
        :type playlist_element_id: int
        :param put_video_playlist_video_request:
        :type put_video_playlist_video_request: PutVideoPlaylistVideoRequest
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
            'playlist_id',
            'playlist_element_id',
            'put_video_playlist_video_request'
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
                    " to method put_video_playlist_video" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']

        if _params['playlist_element_id']:
            _path_params['playlistElementId'] = _params['playlist_element_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['put_video_playlist_video_request'] is not None:
            _body_params = _params['put_video_playlist_video_request']

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
            '/api/v1/video-playlists/{playlistId}/videos/{playlistElementId}', 'PUT',
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
    def reorder_video_playlist(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], reorder_video_playlist_request : Optional[ReorderVideoPlaylistRequest] = None, **kwargs) -> None:  # noqa: E501
        """Reorder a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reorder_video_playlist(playlist_id, reorder_video_playlist_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param reorder_video_playlist_request:
        :type reorder_video_playlist_request: ReorderVideoPlaylistRequest
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
            raise ValueError("Error! Please call the reorder_video_playlist_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.reorder_video_playlist_with_http_info(playlist_id, reorder_video_playlist_request, **kwargs)  # noqa: E501

    @validate_arguments
    def reorder_video_playlist_with_http_info(self, playlist_id : Annotated[conint(strict=True, ge=1), Field(..., description="Playlist id")], reorder_video_playlist_request : Optional[ReorderVideoPlaylistRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Reorder a playlist  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.reorder_video_playlist_with_http_info(playlist_id, reorder_video_playlist_request, async_req=True)
        >>> result = thread.get()

        :param playlist_id: Playlist id (required)
        :type playlist_id: int
        :param reorder_video_playlist_request:
        :type reorder_video_playlist_request: ReorderVideoPlaylistRequest
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
            'playlist_id',
            'reorder_video_playlist_request'
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
                    " to method reorder_video_playlist" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['playlist_id']:
            _path_params['playlistId'] = _params['playlist_id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['reorder_video_playlist_request'] is not None:
            _body_params = _params['reorder_video_playlist_request']

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
            '/api/v1/video-playlists/{playlistId}/videos/reorder', 'POST',
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
