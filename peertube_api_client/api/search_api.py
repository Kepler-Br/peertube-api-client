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

from datetime import datetime

from pydantic import Field, StrictBool, StrictInt, StrictStr, conint, conlist

from typing import Any, Optional

from peertube_api_client.models.api_v1_video_channels_channel_handle_video_playlists_get200_response import ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
from peertube_api_client.models.video_channel_list import VideoChannelList
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class SearchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def search_channels(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it. ")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> VideoChannelList:  # noqa: E501
        """Search channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_channels(search, start, count, search_target, sort, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it.  (required)
        :type search: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
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
            raise ValueError("Error! Please call the search_channels_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.search_channels_with_http_info(search, start, count, search_target, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_channels_with_http_info(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it. ")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search channels  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_channels_with_http_info(search, start, count, search_target, sort, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete channel information and interact with it.  (required)
        :type search: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
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
            'search',
            'start',
            'count',
            'search_target',
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
                    " to method search_channels" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('search_target') is not None:  # noqa: E501
            _query_params.append(('searchTarget', _params['search_target'].value))

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
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/search/video-channels', 'GET',
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
    def search_playlists(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it. ")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response:  # noqa: E501
        """Search playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_playlists(search, start, count, search_target, sort, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it.  (required)
        :type search: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
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
        :rtype: ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the search_playlists_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.search_playlists_with_http_info(search, start, count, search_target, sort, **kwargs)  # noqa: E501

    @validate_arguments
    def search_playlists_with_http_info(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it. ")], start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort column")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search playlists  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_playlists_with_http_info(search, start, count, search_target, sort, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete playlist information and interact with it.  (required)
        :type search: str
        :param start: Offset used to paginate results
        :type start: int
        :param count: Number of items to return
        :type count: int
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
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
        :rtype: tuple(ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'search',
            'start',
            'count',
            'search_target',
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
                    " to method search_playlists" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

        if _params.get('start') is not None:  # noqa: E501
            _query_params.append(('start', _params['start']))

        if _params.get('count') is not None:  # noqa: E501
            _query_params.append(('count', _params['count']))

        if _params.get('search_target') is not None:  # noqa: E501
            _query_params.append(('searchTarget', _params['search_target'].value))

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
            '200': "ApiV1VideoChannelsChannelHandleVideoPlaylistsGet200Response",
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/search/video-playlists', 'GET',
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
    def search_videos(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it. ")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, uuids : Annotated[Optional[conlist(StrictStr)], Field(description="Find videos with specific UUIDs")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort videos by criteria (prefixing with `-` means `DESC` order): ")] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, start_date : Annotated[Optional[datetime], Field(description="Get videos that are published after this date")] = None, end_date : Annotated[Optional[datetime], Field(description="Get videos that are published before this date")] = None, originally_published_start_date : Annotated[Optional[datetime], Field(description="Get videos that are originally published after this date")] = None, originally_published_end_date : Annotated[Optional[datetime], Field(description="Get videos that are originally published before this date")] = None, duration_min : Annotated[Optional[StrictInt], Field(description="Get videos that have this minimum duration")] = None, duration_max : Annotated[Optional[StrictInt], Field(description="Get videos that have this maximum duration")] = None, **kwargs) -> VideoListResponse:  # noqa: E501
        """Search videos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_videos(search, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, uuids, has_hls_files, has_webtorrent_files, skip_count, start, count, search_target, sort, exclude_already_watched, start_date, end_date, originally_published_start_date, originally_published_end_date, duration_min, duration_max, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it.  (required)
        :type search: str
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
        :param uuids: Find videos with specific UUIDs
        :type uuids: List[str]
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
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
        :param sort: Sort videos by criteria (prefixing with `-` means `DESC` order): 
        :type sort: str
        :param exclude_already_watched: Whether or not to exclude videos that are in the user's video history
        :type exclude_already_watched: bool
        :param start_date: Get videos that are published after this date
        :type start_date: datetime
        :param end_date: Get videos that are published before this date
        :type end_date: datetime
        :param originally_published_start_date: Get videos that are originally published after this date
        :type originally_published_start_date: datetime
        :param originally_published_end_date: Get videos that are originally published before this date
        :type originally_published_end_date: datetime
        :param duration_min: Get videos that have this minimum duration
        :type duration_min: int
        :param duration_max: Get videos that have this maximum duration
        :type duration_max: int
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
            raise ValueError("Error! Please call the search_videos_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.search_videos_with_http_info(search, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, uuids, has_hls_files, has_webtorrent_files, skip_count, start, count, search_target, sort, exclude_already_watched, start_date, end_date, originally_published_start_date, originally_published_end_date, duration_min, duration_max, **kwargs)  # noqa: E501

    @validate_arguments
    def search_videos_with_http_info(self, search : Annotated[StrictStr, Field(..., description="String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it. ")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, uuids : Annotated[Optional[conlist(StrictStr)], Field(description="Find videos with specific UUIDs")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, search_target : Annotated[Optional[StrictStr], Field(description="If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API ")] = None, sort : Annotated[Optional[StrictStr], Field(description="Sort videos by criteria (prefixing with `-` means `DESC` order): ")] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, start_date : Annotated[Optional[datetime], Field(description="Get videos that are published after this date")] = None, end_date : Annotated[Optional[datetime], Field(description="Get videos that are published before this date")] = None, originally_published_start_date : Annotated[Optional[datetime], Field(description="Get videos that are originally published after this date")] = None, originally_published_end_date : Annotated[Optional[datetime], Field(description="Get videos that are originally published before this date")] = None, duration_min : Annotated[Optional[StrictInt], Field(description="Get videos that have this minimum duration")] = None, duration_max : Annotated[Optional[StrictInt], Field(description="Get videos that have this maximum duration")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Search videos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.search_videos_with_http_info(search, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, uuids, has_hls_files, has_webtorrent_files, skip_count, start, count, search_target, sort, exclude_already_watched, start_date, end_date, originally_published_start_date, originally_published_end_date, duration_min, duration_max, async_req=True)
        >>> result = thread.get()

        :param search: String to search. If the user can make a remote URI search, and the string is an URI then the PeerTube instance will fetch the remote object and add it to its database. Then, you can use the REST API to fetch the complete video information and interact with it.  (required)
        :type search: str
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
        :param uuids: Find videos with specific UUIDs
        :type uuids: List[str]
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
        :param search_target: If the administrator enabled search index support, you can override the default search target.  **Warning**: If you choose to make an index search, PeerTube will get results from a third party service. It means the instance may not yet know the objects you fetched. If you want to load video/channel information:   * If the current user has the ability to make a remote URI search (this information is available in the config endpoint),   then reuse the search API to make a search using the object URI so PeerTube instance fetches the remote object and fill its database.   After that, you can use the classic REST API endpoints to fetch the complete object or interact with it   * If the current user doesn't have the ability to make a remote URI search, then redirect the user on the origin instance or fetch   the data from the origin instance API 
        :type search_target: str
        :param sort: Sort videos by criteria (prefixing with `-` means `DESC` order): 
        :type sort: str
        :param exclude_already_watched: Whether or not to exclude videos that are in the user's video history
        :type exclude_already_watched: bool
        :param start_date: Get videos that are published after this date
        :type start_date: datetime
        :param end_date: Get videos that are published before this date
        :type end_date: datetime
        :param originally_published_start_date: Get videos that are originally published after this date
        :type originally_published_start_date: datetime
        :param originally_published_end_date: Get videos that are originally published before this date
        :type originally_published_end_date: datetime
        :param duration_min: Get videos that have this minimum duration
        :type duration_min: int
        :param duration_max: Get videos that have this maximum duration
        :type duration_max: int
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
            'search',
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
            'uuids',
            'has_hls_files',
            'has_webtorrent_files',
            'skip_count',
            'start',
            'count',
            'search_target',
            'sort',
            'exclude_already_watched',
            'start_date',
            'end_date',
            'originally_published_start_date',
            'originally_published_end_date',
            'duration_min',
            'duration_max'
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
                    " to method search_videos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('search') is not None:  # noqa: E501
            _query_params.append(('search', _params['search']))

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

        if _params.get('uuids') is not None:  # noqa: E501
            _query_params.append(('uuids', _params['uuids']))
            _collection_formats['uuids'] = 'multi'

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

        if _params.get('search_target') is not None:  # noqa: E501
            _query_params.append(('searchTarget', _params['search_target'].value))

        if _params.get('sort') is not None:  # noqa: E501
            _query_params.append(('sort', _params['sort'].value))

        if _params.get('exclude_already_watched') is not None:  # noqa: E501
            _query_params.append(('excludeAlreadyWatched', _params['exclude_already_watched']))

        if _params.get('start_date') is not None:  # noqa: E501
            if isinstance(_params['start_date'], datetime):
                _query_params.append(('startDate', _params['start_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('startDate', _params['start_date']))

        if _params.get('end_date') is not None:  # noqa: E501
            if isinstance(_params['end_date'], datetime):
                _query_params.append(('endDate', _params['end_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('endDate', _params['end_date']))

        if _params.get('originally_published_start_date') is not None:  # noqa: E501
            if isinstance(_params['originally_published_start_date'], datetime):
                _query_params.append(('originallyPublishedStartDate', _params['originally_published_start_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('originallyPublishedStartDate', _params['originally_published_start_date']))

        if _params.get('originally_published_end_date') is not None:  # noqa: E501
            if isinstance(_params['originally_published_end_date'], datetime):
                _query_params.append(('originallyPublishedEndDate', _params['originally_published_end_date'].strftime(self.api_client.configuration.datetime_format)))
            else:
                _query_params.append(('originallyPublishedEndDate', _params['originally_published_end_date']))

        if _params.get('duration_min') is not None:  # noqa: E501
            _query_params.append(('durationMin', _params['duration_min']))

        if _params.get('duration_max') is not None:  # noqa: E501
            _query_params.append(('durationMax', _params['duration_max']))

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
            '500': None,
        }

        return self.api_client.call_api(
            '/api/v1/search/videos', 'GET',
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
