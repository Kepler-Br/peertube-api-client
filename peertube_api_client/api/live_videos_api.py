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

from pydantic import Field, StrictBool, StrictBytes, StrictInt, StrictStr, conlist, constr

from typing import Any, Optional, Union

from peertube_api_client.models.api_v1_videos_live_id_sessions_get200_response import ApiV1VideosLiveIdSessionsGet200Response
from peertube_api_client.models.live_video_latency_mode import LiveVideoLatencyMode
from peertube_api_client.models.live_video_replay_settings import LiveVideoReplaySettings
from peertube_api_client.models.live_video_response import LiveVideoResponse
from peertube_api_client.models.live_video_session_response import LiveVideoSessionResponse
from peertube_api_client.models.live_video_update import LiveVideoUpdate
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_upload_response import VideoUploadResponse

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class LiveVideosApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def add_live(self, channel_id : Annotated[StrictInt, Field(..., description="Channel id that will contain this live video")], name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Live video/replay name")], save_replay : Optional[StrictBool] = None, replay_settings : Optional[LiveVideoReplaySettings] = None, permanent_live : Annotated[Optional[StrictBool], Field(description="User can stream multiple times in a permanent live")] = None, latency_mode : Optional[LiveVideoLatencyMode] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Live video/replay thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Live video/replay preview file")] = None, privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Live video/replay description")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this live video/replay contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1)], Field(description="Live video/replay tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this live video/replay")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for the replay of this live video")] = None, **kwargs) -> VideoUploadResponse:  # noqa: E501
        """Create a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_live(channel_id, name, save_replay, replay_settings, permanent_live, latency_mode, thumbnailfile, previewfile, privacy, category, licence, language, description, support, nsfw, tags, comments_enabled, download_enabled, async_req=True)
        >>> result = thread.get()

        :param channel_id: Channel id that will contain this live video (required)
        :type channel_id: int
        :param name: Live video/replay name (required)
        :type name: str
        :param save_replay:
        :type save_replay: bool
        :param replay_settings:
        :type replay_settings: LiveVideoReplaySettings
        :param permanent_live: User can stream multiple times in a permanent live
        :type permanent_live: bool
        :param latency_mode:
        :type latency_mode: LiveVideoLatencyMode
        :param thumbnailfile: Live video/replay thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Live video/replay preview file
        :type previewfile: bytearray
        :param privacy:
        :type privacy: VideoPrivacySet
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param description: Live video/replay description
        :type description: str
        :param support: A text tell the audience how to support the creator
        :type support: str
        :param nsfw: Whether or not this live video/replay contains sensitive content
        :type nsfw: bool
        :param tags: Live video/replay tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this live video/replay
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for the replay of this live video
        :type download_enabled: bool
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: VideoUploadResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the add_live_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_live_with_http_info(channel_id, name, save_replay, replay_settings, permanent_live, latency_mode, thumbnailfile, previewfile, privacy, category, licence, language, description, support, nsfw, tags, comments_enabled, download_enabled, **kwargs)  # noqa: E501

    @validate_arguments
    def add_live_with_http_info(self, channel_id : Annotated[StrictInt, Field(..., description="Channel id that will contain this live video")], name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Live video/replay name")], save_replay : Optional[StrictBool] = None, replay_settings : Optional[LiveVideoReplaySettings] = None, permanent_live : Annotated[Optional[StrictBool], Field(description="User can stream multiple times in a permanent live")] = None, latency_mode : Optional[LiveVideoLatencyMode] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Live video/replay thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Live video/replay preview file")] = None, privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Live video/replay description")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this live video/replay contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1)], Field(description="Live video/replay tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this live video/replay")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for the replay of this live video")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Create a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_live_with_http_info(channel_id, name, save_replay, replay_settings, permanent_live, latency_mode, thumbnailfile, previewfile, privacy, category, licence, language, description, support, nsfw, tags, comments_enabled, download_enabled, async_req=True)
        >>> result = thread.get()

        :param channel_id: Channel id that will contain this live video (required)
        :type channel_id: int
        :param name: Live video/replay name (required)
        :type name: str
        :param save_replay:
        :type save_replay: bool
        :param replay_settings:
        :type replay_settings: LiveVideoReplaySettings
        :param permanent_live: User can stream multiple times in a permanent live
        :type permanent_live: bool
        :param latency_mode:
        :type latency_mode: LiveVideoLatencyMode
        :param thumbnailfile: Live video/replay thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Live video/replay preview file
        :type previewfile: bytearray
        :param privacy:
        :type privacy: VideoPrivacySet
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param description: Live video/replay description
        :type description: str
        :param support: A text tell the audience how to support the creator
        :type support: str
        :param nsfw: Whether or not this live video/replay contains sensitive content
        :type nsfw: bool
        :param tags: Live video/replay tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this live video/replay
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for the replay of this live video
        :type download_enabled: bool
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
        :rtype: tuple(VideoUploadResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'channel_id',
            'name',
            'save_replay',
            'replay_settings',
            'permanent_live',
            'latency_mode',
            'thumbnailfile',
            'previewfile',
            'privacy',
            'category',
            'licence',
            'language',
            'description',
            'support',
            'nsfw',
            'tags',
            'comments_enabled',
            'download_enabled'
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
                    " to method add_live" % _key
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
        if _params['channel_id']:
            _form_params.append(('channelId', _params['channel_id']))

        if _params['save_replay']:
            _form_params.append(('saveReplay', _params['save_replay']))

        if _params['replay_settings']:
            _form_params.append(('replaySettings', _params['replay_settings']))

        if _params['permanent_live']:
            _form_params.append(('permanentLive', _params['permanent_live']))

        if _params['latency_mode']:
            _form_params.append(('latencyMode', _params['latency_mode']))

        if _params['thumbnailfile']:
            _files['thumbnailfile'] = _params['thumbnailfile']

        if _params['previewfile']:
            _files['previewfile'] = _params['previewfile']

        if _params['privacy']:
            _form_params.append(('privacy', _params['privacy']))

        if _params['category']:
            _form_params.append(('category', _params['category']))

        if _params['licence']:
            _form_params.append(('licence', _params['licence']))

        if _params['language']:
            _form_params.append(('language', _params['language']))

        if _params['description']:
            _form_params.append(('description', _params['description']))

        if _params['support']:
            _form_params.append(('support', _params['support']))

        if _params['nsfw']:
            _form_params.append(('nsfw', _params['nsfw']))

        if _params['name']:
            _form_params.append(('name', _params['name']))

        if _params['tags']:
            _form_params.append(('tags', _params['tags']))
            _collection_formats['tags'] = 'csv'

        if _params['comments_enabled']:
            _form_params.append(('commentsEnabled', _params['comments_enabled']))

        if _params['download_enabled']:
            _form_params.append(('downloadEnabled', _params['download_enabled']))

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
            '200': "VideoUploadResponse",
            '400': None,
            '403': None,
        }

        return self.api_client.call_api(
            '/api/v1/videos/live', 'POST',
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
    def api_v1_videos_id_live_session_get(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> LiveVideoSessionResponse:  # noqa: E501
        """Get live session of a replay  # noqa: E501

        If the video is a replay of a live, you can find the associated live session using this endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_live_session_get(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LiveVideoSessionResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_videos_id_live_session_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_videos_id_live_session_get_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_videos_id_live_session_get_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get live session of a replay  # noqa: E501

        If the video is a replay of a live, you can find the associated live session using this endpoint  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_live_session_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
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
        :rtype: tuple(LiveVideoSessionResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method api_v1_videos_id_live_session_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
            '200': "LiveVideoSessionResponse",
        }

        return self.api_client.call_api(
            '/api/v1/videos/{id}/live-session', 'GET',
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
    def api_v1_videos_live_id_sessions_get(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiV1VideosLiveIdSessionsGet200Response:  # noqa: E501
        """List live sessions  # noqa: E501

        List all sessions created in a particular live  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_live_id_sessions_get(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: ApiV1VideosLiveIdSessionsGet200Response
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_videos_live_id_sessions_get_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_videos_live_id_sessions_get_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_videos_live_id_sessions_get_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """List live sessions  # noqa: E501

        List all sessions created in a particular live  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_live_id_sessions_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
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
        :rtype: tuple(ApiV1VideosLiveIdSessionsGet200Response, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method api_v1_videos_live_id_sessions_get" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
            '200': "ApiV1VideosLiveIdSessionsGet200Response",
        }

        return self.api_client.call_api(
            '/api/v1/videos/live/{id}/sessions', 'GET',
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
    def get_live_id(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> LiveVideoResponse:  # noqa: E501
        """Get information about a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_live_id(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: LiveVideoResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_live_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_live_id_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_live_id_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get information about a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_live_id_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
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
        :rtype: tuple(LiveVideoResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'id'
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
                    " to method get_live_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


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
            '200': "LiveVideoResponse",
        }

        return self.api_client.call_api(
            '/api/v1/videos/live/{id}', 'GET',
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
    def update_live_id(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], live_video_update : Optional[LiveVideoUpdate] = None, **kwargs) -> None:  # noqa: E501
        """Update information about a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_live_id(id, live_video_update, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param live_video_update:
        :type live_video_update: LiveVideoUpdate
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
            raise ValueError("Error! Please call the update_live_id_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.update_live_id_with_http_info(id, live_video_update, **kwargs)  # noqa: E501

    @validate_arguments
    def update_live_id_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], live_video_update : Optional[LiveVideoUpdate] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update information about a live  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_live_id_with_http_info(id, live_video_update, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param live_video_update:
        :type live_video_update: LiveVideoUpdate
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
            'id',
            'live_video_update'
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
                    " to method update_live_id" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}
        if _params['id']:
            _path_params['id'] = _params['id']


        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['live_video_update'] is not None:
            _body_params = _params['live_video_update']

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
            '/api/v1/videos/live/{id}', 'PUT',
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
