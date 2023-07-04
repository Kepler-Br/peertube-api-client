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

from pydantic import Field, StrictBool, StrictBytes, StrictFloat, StrictInt, StrictStr, conint, conlist, constr

from typing import Any, List, Optional, Union

from peertube_api_client.models.live_video_latency_mode import LiveVideoLatencyMode
from peertube_api_client.models.live_video_replay_settings import LiveVideoReplaySettings
from peertube_api_client.models.live_video_response import LiveVideoResponse
from peertube_api_client.models.live_video_update import LiveVideoUpdate
from peertube_api_client.models.user_viewing_video import UserViewingVideo
from peertube_api_client.models.video_details import VideoDetails
from peertube_api_client.models.video_list_response import VideoListResponse
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate
from peertube_api_client.models.video_source import VideoSource
from peertube_api_client.models.video_token_response import VideoTokenResponse
from peertube_api_client.models.video_upload_request_resumable import VideoUploadRequestResumable
from peertube_api_client.models.video_upload_response import VideoUploadResponse

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VideoApi(object):
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
    def add_view(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], user_viewing_video : UserViewingVideo, **kwargs) -> None:  # noqa: E501
        """Notify user is watching a video  # noqa: E501

        Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video's viewers counter. If the user is authenticated, PeerTube will also store the current player time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_view(id, user_viewing_video, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param user_viewing_video: (required)
        :type user_viewing_video: UserViewingVideo
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
            raise ValueError("Error! Please call the add_view_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.add_view_with_http_info(id, user_viewing_video, **kwargs)  # noqa: E501

    @validate_arguments
    def add_view_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], user_viewing_video : UserViewingVideo, **kwargs) -> ApiResponse:  # noqa: E501
        """Notify user is watching a video  # noqa: E501

        Call this endpoint regularly (every 5-10 seconds for example) to notify the server the user is watching the video. After a while, PeerTube will increase video's viewers counter. If the user is authenticated, PeerTube will also store the current player time.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.add_view_with_http_info(id, user_viewing_video, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param user_viewing_video: (required)
        :type user_viewing_video: UserViewingVideo
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
            'user_viewing_video'
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
                    " to method add_view" % _key
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
        if _params['user_viewing_video'] is not None:
            _body_params = _params['user_viewing_video']

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = []  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/videos/{id}/views', 'POST',
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
    def api_v1_videos_id_studio_edit_post(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> None:  # noqa: E501
        """Create a studio task  # noqa: E501

        Create a task to edit a video  (cut, add intro/outro etc)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_studio_edit_post(id, async_req=True)
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the api_v1_videos_id_studio_edit_post_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_videos_id_studio_edit_post_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_videos_id_studio_edit_post_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Create a studio task  # noqa: E501

        Create a task to edit a video  (cut, add intro/outro etc)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_studio_edit_post_with_http_info(id, async_req=True)
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
        :rtype: None
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
                    " to method api_v1_videos_id_studio_edit_post" % _key
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
        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/x-www-form-urlencoded']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/videos/{id}/studio/edit', 'POST',
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
    def api_v1_videos_id_watching_put(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], user_viewing_video : UserViewingVideo, **kwargs) -> None:  # noqa: E501
        """(Deprecated) Set watching progress of a video  # noqa: E501

        This endpoint has been deprecated. Use `/videos/{id}/views` instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_watching_put(id, user_viewing_video, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param user_viewing_video: (required)
        :type user_viewing_video: UserViewingVideo
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
            raise ValueError("Error! Please call the api_v1_videos_id_watching_put_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.api_v1_videos_id_watching_put_with_http_info(id, user_viewing_video, **kwargs)  # noqa: E501

    @validate_arguments
    def api_v1_videos_id_watching_put_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], user_viewing_video : UserViewingVideo, **kwargs) -> ApiResponse:  # noqa: E501
        """(Deprecated) Set watching progress of a video  # noqa: E501

        This endpoint has been deprecated. Use `/videos/{id}/views` instead  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.api_v1_videos_id_watching_put_with_http_info(id, user_viewing_video, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param user_viewing_video: (required)
        :type user_viewing_video: UserViewingVideo
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

        warnings.warn("PUT /api/v1/videos/{id}/watching is deprecated.", DeprecationWarning)

        _params = locals()

        _all_params = [
            'id',
            'user_viewing_video'
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
                    " to method api_v1_videos_id_watching_put" % _key
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
        if _params['user_viewing_video'] is not None:
            _body_params = _params['user_viewing_video']

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
            '/api/v1/videos/{id}/watching', 'PUT',
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
    def del_video(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> None:  # noqa: E501
        """Delete a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video(id, async_req=True)
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
        :rtype: None
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the del_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.del_video_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def del_video_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Delete a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.del_video_with_http_info(id, async_req=True)
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
        :rtype: None
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
                    " to method del_video" % _key
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
        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/videos/{id}', 'DELETE',
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
    def get_account_videos(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> VideoListResponse:  # noqa: E501
        """List videos of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_videos(name, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
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
            raise ValueError("Error! Please call the get_account_videos_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_account_videos_with_http_info(name, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, **kwargs)  # noqa: E501

    @validate_arguments
    def get_account_videos_with_http_info(self, name : Annotated[StrictStr, Field(..., description="The username or handle of the account")], category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List videos of an account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_account_videos_with_http_info(name, category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

        :param name: The username or handle of the account (required)
        :type name: str
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
            'name',
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
                    " to method get_account_videos" % _key
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
            '/api/v1/accounts/{name}/videos', 'GET',
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
    def get_categories(self, **kwargs) -> List[str]:  # noqa: E501
        """List available video categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_categories(async_req=True)
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
            raise ValueError("Error! Please call the get_categories_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_categories_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_categories_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List available video categories  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_categories_with_http_info(async_req=True)
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
                    " to method get_categories" % _key
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
            '/api/v1/videos/categories', 'GET',
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
    def get_languages(self, **kwargs) -> List[str]:  # noqa: E501
        """List available video languages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_languages(async_req=True)
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
            raise ValueError("Error! Please call the get_languages_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_languages_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_languages_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List available video languages  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_languages_with_http_info(async_req=True)
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
                    " to method get_languages" % _key
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
            '/api/v1/videos/languages', 'GET',
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
    def get_licences(self, **kwargs) -> List[str]:  # noqa: E501
        """List available video licences  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_licences(async_req=True)
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
            raise ValueError("Error! Please call the get_licences_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_licences_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_licences_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List available video licences  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_licences_with_http_info(async_req=True)
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
                    " to method get_licences" % _key
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
            '/api/v1/videos/licences', 'GET',
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
    def get_video(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> VideoDetails:  # noqa: E501
        """Get a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video(id, async_req=True)
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
        :rtype: VideoDetails
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_with_http_info(id, async_req=True)
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
        :rtype: tuple(VideoDetails, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_video" % _key
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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoDetails",
        }

        return self.api_client.call_api(
            '/api/v1/videos/{id}', 'GET',
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
    def get_video_desc(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> str:  # noqa: E501
        """Get complete video description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_desc(id, async_req=True)
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
        :rtype: str
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_desc_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_desc_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_desc_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get complete video description  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_desc_with_http_info(id, async_req=True)
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
        :rtype: tuple(str, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_video_desc" % _key
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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "str",
        }

        return self.api_client.call_api(
            '/api/v1/videos/{id}/description', 'GET',
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
    def get_video_privacy_policies(self, **kwargs) -> List[str]:  # noqa: E501
        """List available video privacy policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_privacy_policies(async_req=True)
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
            raise ValueError("Error! Please call the get_video_privacy_policies_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_privacy_policies_with_http_info(**kwargs)  # noqa: E501

    @validate_arguments
    def get_video_privacy_policies_with_http_info(self, **kwargs) -> ApiResponse:  # noqa: E501
        """List available video privacy policies  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_privacy_policies_with_http_info(async_req=True)
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
                    " to method get_video_privacy_policies" % _key
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
            '/api/v1/videos/privacies', 'GET',
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
    def get_video_source(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> VideoSource:  # noqa: E501
        """Get video source file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_source(id, async_req=True)
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
        :rtype: VideoSource
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the get_video_source_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_video_source_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def get_video_source_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Get video source file metadata  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_video_source_with_http_info(id, async_req=True)
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
        :rtype: tuple(VideoSource, status_code(int), headers(HTTPHeaderDict))
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
                    " to method get_video_source" % _key
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
        _auth_settings = []  # noqa: E501

        _response_types_map = {
            '200': "VideoSource",
        }

        return self.api_client.call_api(
            '/api/v1/videos/{id}/source', 'POST',
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
    def get_videos(self, category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> VideoListResponse:  # noqa: E501
        """List videos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_videos(category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

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
            raise ValueError("Error! Please call the get_videos_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.get_videos_with_http_info(category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, **kwargs)  # noqa: E501

    @validate_arguments
    def get_videos_with_http_info(self, category_one_of : Annotated[Optional[Any], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, is_live : Annotated[Optional[StrictBool], Field(description="whether or not the video is a live")] = None, tags_one_of : Annotated[Optional[Any], Field(description="tag(s) of the video")] = None, tags_all_of : Annotated[Optional[Any], Field(description="tag(s) of the video, where all should be present in the video")] = None, licence_one_of : Annotated[Optional[Any], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language_one_of : Annotated[Optional[Any], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages)). Use `_unknown` to filter on videos that don't have a video language")] = None, nsfw : Annotated[Optional[StrictStr], Field(description="whether to include nsfw videos, if any")] = None, is_local : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only local or remote videos")] = None, include : Annotated[Optional[StrictInt], Field(description="**PeerTube >= 4.0** Include additional videos in results (can be combined using bitwise or operator) - `0` NONE - `1` NOT_PUBLISHED_STATE - `2` BLACKLISTED - `4` BLOCKED_OWNER - `8` FILES ")] = None, privacy_one_of : Annotated[Optional[VideoPrivacySet], Field(description="**PeerTube >= 4.0** Display only videos in this specific privacy/privacies")] = None, has_hls_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have HLS files")] = None, has_webtorrent_files : Annotated[Optional[StrictBool], Field(description="**PeerTube >= 4.0** Display only videos that have WebTorrent files")] = None, skip_count : Annotated[Optional[StrictStr], Field(description="if you don't need the `total` in the response")] = None, start : Annotated[Optional[conint(strict=True, ge=0)], Field(description="Offset used to paginate results")] = None, count : Annotated[Optional[conint(strict=True, le=100, ge=1)], Field(description="Number of items to return")] = None, sort : Optional[StrictStr] = None, exclude_already_watched : Annotated[Optional[StrictBool], Field(description="Whether or not to exclude videos that are in the user's video history")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """List videos  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_videos_with_http_info(category_one_of, is_live, tags_one_of, tags_all_of, licence_one_of, language_one_of, nsfw, is_local, include, privacy_one_of, has_hls_files, has_webtorrent_files, skip_count, start, count, sort, exclude_already_watched, async_req=True)
        >>> result = thread.get()

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
                    " to method get_videos" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

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
            '/api/v1/videos', 'GET',
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
    def put_video(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, privacy : Optional[VideoPrivacySet] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictStr], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, name : Annotated[Optional[constr(strict=True, max_length=120, min_length=3)], Field(description="Video name")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, **kwargs) -> None:  # noqa: E501
        """Update a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video(id, thumbnailfile, previewfile, category, licence, language, privacy, description, wait_transcoding, support, nsfw, name, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param thumbnailfile: Video thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Video preview file
        :type previewfile: bytearray
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param privacy:
        :type privacy: VideoPrivacySet
        :param description: Video description
        :type description: str
        :param wait_transcoding: Whether or not we wait transcoding before publish the video
        :type wait_transcoding: str
        :param support: A text tell the audience how to support the video creator
        :type support: str
        :param nsfw: Whether or not this video contains sensitive content
        :type nsfw: bool
        :param name: Video name
        :type name: str
        :param tags: Video tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this video
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for this video
        :type download_enabled: bool
        :param originally_published_at: Date when the content was originally published
        :type originally_published_at: datetime
        :param schedule_update:
        :type schedule_update: VideoScheduledUpdate
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
            raise ValueError("Error! Please call the put_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.put_video_with_http_info(id, thumbnailfile, previewfile, category, licence, language, privacy, description, wait_transcoding, support, nsfw, name, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, **kwargs)  # noqa: E501

    @validate_arguments
    def put_video_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, privacy : Optional[VideoPrivacySet] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictStr], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, name : Annotated[Optional[constr(strict=True, max_length=120, min_length=3)], Field(description="Video name")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Update a video  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put_video_with_http_info(id, thumbnailfile, previewfile, category, licence, language, privacy, description, wait_transcoding, support, nsfw, name, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, async_req=True)
        >>> result = thread.get()

        :param id: The object id, uuid or short uuid (required)
        :type id: ApiV1VideosOwnershipIdAcceptPostIdParameter
        :param thumbnailfile: Video thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Video preview file
        :type previewfile: bytearray
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param privacy:
        :type privacy: VideoPrivacySet
        :param description: Video description
        :type description: str
        :param wait_transcoding: Whether or not we wait transcoding before publish the video
        :type wait_transcoding: str
        :param support: A text tell the audience how to support the video creator
        :type support: str
        :param nsfw: Whether or not this video contains sensitive content
        :type nsfw: bool
        :param name: Video name
        :type name: str
        :param tags: Video tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this video
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for this video
        :type download_enabled: bool
        :param originally_published_at: Date when the content was originally published
        :type originally_published_at: datetime
        :param schedule_update:
        :type schedule_update: VideoScheduledUpdate
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
            'thumbnailfile',
            'previewfile',
            'category',
            'licence',
            'language',
            'privacy',
            'description',
            'wait_transcoding',
            'support',
            'nsfw',
            'name',
            'tags',
            'comments_enabled',
            'download_enabled',
            'originally_published_at',
            'schedule_update'
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
                    " to method put_video" % _key
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
        if _params['thumbnailfile']:
            _files['thumbnailfile'] = _params['thumbnailfile']

        if _params['previewfile']:
            _files['previewfile'] = _params['previewfile']

        if _params['category']:
            _form_params.append(('category', _params['category']))

        if _params['licence']:
            _form_params.append(('licence', _params['licence']))

        if _params['language']:
            _form_params.append(('language', _params['language']))

        if _params['privacy']:
            _form_params.append(('privacy', _params['privacy']))

        if _params['description']:
            _form_params.append(('description', _params['description']))

        if _params['wait_transcoding']:
            _form_params.append(('waitTranscoding', _params['wait_transcoding']))

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

        if _params['originally_published_at']:
            _form_params.append(('originallyPublishedAt', _params['originally_published_at']))

        if _params['schedule_update']:
            _form_params.append(('scheduleUpdate', _params['schedule_update']))

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
            '/api/v1/videos/{id}', 'PUT',
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
    def request_video_token(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> VideoTokenResponse:  # noqa: E501
        """Request video token  # noqa: E501

        Request special tokens that expire quickly to use them in some context (like accessing private static files)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.request_video_token(id, async_req=True)
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
        :rtype: VideoTokenResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the request_video_token_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.request_video_token_with_http_info(id, **kwargs)  # noqa: E501

    @validate_arguments
    def request_video_token_with_http_info(self, id : Annotated[Any, Field(..., description="The object id, uuid or short uuid")], **kwargs) -> ApiResponse:  # noqa: E501
        """Request video token  # noqa: E501

        Request special tokens that expire quickly to use them in some context (like accessing private static files)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.request_video_token_with_http_info(id, async_req=True)
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
        :rtype: tuple(VideoTokenResponse, status_code(int), headers(HTTPHeaderDict))
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
                    " to method request_video_token" % _key
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
            '200': "VideoTokenResponse",
            '400': None,
            '404': None,
        }

        return self.api_client.call_api(
            '/api/v1/videos/{id}/token', 'POST',
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

    @validate_arguments
    def upload_legacy(self, name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Video name")], videofile : Annotated[Union[StrictBytes, StrictStr], Field(..., description="Video file")], channel_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Channel id that will contain this video")] = None, privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictBool], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1, unique_items=True)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, **kwargs) -> VideoUploadResponse:  # noqa: E501
        """Upload a video  # noqa: E501

        Uses a single request to upload a video.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_legacy(name, videofile, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, async_req=True)
        >>> result = thread.get()

        :param name: Video name (required)
        :type name: str
        :param videofile: Video file (required)
        :type videofile: bytearray
        :param channel_id: Channel id that will contain this video
        :type channel_id: int
        :param privacy:
        :type privacy: VideoPrivacySet
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param description: Video description
        :type description: str
        :param wait_transcoding: Whether or not we wait transcoding before publish the video
        :type wait_transcoding: bool
        :param support: A text tell the audience how to support the video creator
        :type support: str
        :param nsfw: Whether or not this video contains sensitive content
        :type nsfw: bool
        :param tags: Video tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this video
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for this video
        :type download_enabled: bool
        :param originally_published_at: Date when the content was originally published
        :type originally_published_at: datetime
        :param schedule_update:
        :type schedule_update: VideoScheduledUpdate
        :param thumbnailfile: Video thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Video preview file
        :type previewfile: bytearray
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
            raise ValueError("Error! Please call the upload_legacy_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_legacy_with_http_info(name, videofile, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_legacy_with_http_info(self, name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Video name")], videofile : Annotated[Union[StrictBytes, StrictStr], Field(..., description="Video file")], channel_id : Annotated[Optional[conint(strict=True, ge=1)], Field(description="Channel id that will contain this video")] = None, privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictBool], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1, unique_items=True)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Upload a video  # noqa: E501

        Uses a single request to upload a video.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_legacy_with_http_info(name, videofile, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, async_req=True)
        >>> result = thread.get()

        :param name: Video name (required)
        :type name: str
        :param videofile: Video file (required)
        :type videofile: bytearray
        :param channel_id: Channel id that will contain this video
        :type channel_id: int
        :param privacy:
        :type privacy: VideoPrivacySet
        :param category: category id of the video (see [/videos/categories](#operation/getCategories))
        :type category: int
        :param licence: licence id of the video (see [/videos/licences](#operation/getLicences))
        :type licence: int
        :param language: language id of the video (see [/videos/languages](#operation/getLanguages))
        :type language: str
        :param description: Video description
        :type description: str
        :param wait_transcoding: Whether or not we wait transcoding before publish the video
        :type wait_transcoding: bool
        :param support: A text tell the audience how to support the video creator
        :type support: str
        :param nsfw: Whether or not this video contains sensitive content
        :type nsfw: bool
        :param tags: Video tags (maximum 5 tags each between 2 and 30 characters)
        :type tags: List[str]
        :param comments_enabled: Enable or disable comments for this video
        :type comments_enabled: bool
        :param download_enabled: Enable or disable downloading for this video
        :type download_enabled: bool
        :param originally_published_at: Date when the content was originally published
        :type originally_published_at: datetime
        :param schedule_update:
        :type schedule_update: VideoScheduledUpdate
        :param thumbnailfile: Video thumbnail file
        :type thumbnailfile: bytearray
        :param previewfile: Video preview file
        :type previewfile: bytearray
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
            'name',
            'videofile',
            'channel_id',
            'privacy',
            'category',
            'licence',
            'language',
            'description',
            'wait_transcoding',
            'support',
            'nsfw',
            'tags',
            'comments_enabled',
            'download_enabled',
            'originally_published_at',
            'schedule_update',
            'thumbnailfile',
            'previewfile'
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
                    " to method upload_legacy" % _key
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
        if _params['name']:
            _form_params.append(('name', _params['name']))

        if _params['channel_id']:
            _form_params.append(('channelId', _params['channel_id']))

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

        if _params['wait_transcoding']:
            _form_params.append(('waitTranscoding', _params['wait_transcoding']))

        if _params['support']:
            _form_params.append(('support', _params['support']))

        if _params['nsfw']:
            _form_params.append(('nsfw', _params['nsfw']))

        if _params['tags']:
            _form_params.append(('tags', _params['tags']))
            _collection_formats['tags'] = 'csv'

        if _params['comments_enabled']:
            _form_params.append(('commentsEnabled', _params['comments_enabled']))

        if _params['download_enabled']:
            _form_params.append(('downloadEnabled', _params['download_enabled']))

        if _params['originally_published_at']:
            _form_params.append(('originallyPublishedAt', _params['originally_published_at']))

        if _params['schedule_update']:
            _form_params.append(('scheduleUpdate', _params['schedule_update']))

        if _params['thumbnailfile']:
            _files['thumbnailfile'] = _params['thumbnailfile']

        if _params['previewfile']:
            _files['previewfile'] = _params['previewfile']

        if _params['videofile']:
            _files['videofile'] = _params['videofile']

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
            '403': None,
            '408': None,
            '413': None,
            '415': None,
            '422': None,
        }

        return self.api_client.call_api(
            '/api/v1/videos/upload', 'POST',
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
    def upload_resumable(self, upload_id : Annotated[StrictStr, Field(..., description="Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. ")], content_range : Annotated[StrictStr, Field(..., description="Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. ")], content_length : Annotated[Union[StrictFloat, StrictInt], Field(..., description="Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. ")], body : Optional[Union[StrictBytes, StrictStr]] = None, **kwargs) -> VideoUploadResponse:  # noqa: E501
        """Send chunk for the resumable upload of a video  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable(upload_id, content_range, content_length, body, async_req=True)
        >>> result = thread.get()

        :param upload_id: Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
        :type upload_id: str
        :param content_range: Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
        :type content_range: str
        :param content_length: Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
        :type content_length: float
        :param body:
        :type body: bytearray
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
            raise ValueError("Error! Please call the upload_resumable_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_resumable_with_http_info(upload_id, content_range, content_length, body, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_resumable_with_http_info(self, upload_id : Annotated[StrictStr, Field(..., description="Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload. ")], content_range : Annotated[StrictStr, Field(..., description="Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file. ")], content_length : Annotated[Union[StrictFloat, StrictInt], Field(..., description="Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health. ")], body : Optional[Union[StrictBytes, StrictStr]] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Send chunk for the resumable upload of a video  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to continue, pause or resume the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable_with_http_info(upload_id, content_range, content_length, body, async_req=True)
        >>> result = thread.get()

        :param upload_id: Created session id to proceed with. If you didn't send chunks in the last hour, it is not valid anymore and you need to initialize a new upload.  (required)
        :type upload_id: str
        :param content_range: Specifies the bytes in the file that the request is uploading.  For example, a value of `bytes 0-262143/2469036` shows that the request is sending the first 262144 bytes (256 x 1024) in a 2,469,036 byte file.  (required)
        :type content_range: str
        :param content_length: Size of the chunk that the request is sending.  Remember that larger chunks are more efficient. PeerTube's web client uses chunks varying from 1048576 bytes (~1MB) and increases or reduces size depending on connection health.  (required)
        :type content_length: float
        :param body:
        :type body: bytearray
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
            'upload_id',
            'content_range',
            'content_length',
            'body'
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
                    " to method upload_resumable" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('upload_id') is not None:  # noqa: E501
            _query_params.append(('upload_id', _params['upload_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_range']:
            _header_params['Content-Range'] = _params['content_range']

        if _params['content_length']:
            _header_params['Content-Length'] = _params['content_length']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['body'] is not None:
            _body_params = _params['body']
            # convert to byte array if the input is a file name (str)
            if isinstance(_body_params, str):
                with io.open(_body_params, "rb") as _fp:
                   _body_params_from_file = _fp.read()
                _body_params = _body_params_from_file

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/octet-stream']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {
            '200': "VideoUploadResponse",
            '308': None,
            '403': None,
            '404': None,
            '409': None,
            '422': None,
            '429': None,
            '503': None,
        }

        return self.api_client.call_api(
            '/api/v1/videos/upload-resumable', 'PUT',
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
    def upload_resumable_cancel(self, upload_id : Annotated[StrictStr, Field(..., description="Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) ")], content_length : Union[StrictFloat, StrictInt], **kwargs) -> None:  # noqa: E501
        """Cancel the resumable upload of a video, deleting any data uploaded so far  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable_cancel(upload_id, content_length, async_req=True)
        >>> result = thread.get()

        :param upload_id: Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
        :type upload_id: str
        :param content_length: (required)
        :type content_length: float
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
            raise ValueError("Error! Please call the upload_resumable_cancel_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_resumable_cancel_with_http_info(upload_id, content_length, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_resumable_cancel_with_http_info(self, upload_id : Annotated[StrictStr, Field(..., description="Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-) ")], content_length : Union[StrictFloat, StrictInt], **kwargs) -> ApiResponse:  # noqa: E501
        """Cancel the resumable upload of a video, deleting any data uploaded so far  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to cancel the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable_cancel_with_http_info(upload_id, content_length, async_req=True)
        >>> result = thread.get()

        :param upload_id: Created session id to proceed with. If you didn't send chunks in the last 12 hours, it is not valid anymore and the upload session has already been deleted with its data ;-)  (required)
        :type upload_id: str
        :param content_length: (required)
        :type content_length: float
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
            'upload_id',
            'content_length'
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
                    " to method upload_resumable_cancel" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('upload_id') is not None:  # noqa: E501
            _query_params.append(('upload_id', _params['upload_id']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        if _params['content_length']:
            _header_params['Content-Length'] = _params['content_length']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # authentication setting
        _auth_settings = ['OAuth2']  # noqa: E501

        _response_types_map = {}

        return self.api_client.call_api(
            '/api/v1/videos/upload-resumable', 'DELETE',
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
    def upload_resumable_init(self, x_upload_content_length : Annotated[Union[StrictFloat, StrictInt], Field(..., description="Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.")], x_upload_content_type : Annotated[StrictStr, Field(..., description="MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.")], video_upload_request_resumable : Optional[VideoUploadRequestResumable] = None, **kwargs) -> None:  # noqa: E501
        """Initialize the resumable upload of a video  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable_init(x_upload_content_length, x_upload_content_type, video_upload_request_resumable, async_req=True)
        >>> result = thread.get()

        :param x_upload_content_length: Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
        :type x_upload_content_length: float
        :param x_upload_content_type: MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
        :type x_upload_content_type: str
        :param video_upload_request_resumable:
        :type video_upload_request_resumable: VideoUploadRequestResumable
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
            raise ValueError("Error! Please call the upload_resumable_init_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.upload_resumable_init_with_http_info(x_upload_content_length, x_upload_content_type, video_upload_request_resumable, **kwargs)  # noqa: E501

    @validate_arguments
    def upload_resumable_init_with_http_info(self, x_upload_content_length : Annotated[Union[StrictFloat, StrictInt], Field(..., description="Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading.")], x_upload_content_type : Annotated[StrictStr, Field(..., description="MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary.")], video_upload_request_resumable : Optional[VideoUploadRequestResumable] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Initialize the resumable upload of a video  # noqa: E501

        Uses [a resumable protocol](https://github.com/kukhariev/node-uploadx/blob/master/proto.md) to initialize the upload of a video  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload_resumable_init_with_http_info(x_upload_content_length, x_upload_content_type, video_upload_request_resumable, async_req=True)
        >>> result = thread.get()

        :param x_upload_content_length: Number of bytes that will be uploaded in subsequent requests. Set this value to the size of the file you are uploading. (required)
        :type x_upload_content_length: float
        :param x_upload_content_type: MIME type of the file that you are uploading. Depending on your instance settings, acceptable values might vary. (required)
        :type x_upload_content_type: str
        :param video_upload_request_resumable:
        :type video_upload_request_resumable: VideoUploadRequestResumable
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
            'x_upload_content_length',
            'x_upload_content_type',
            'video_upload_request_resumable'
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
                    " to method upload_resumable_init" % _key
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
        if _params['x_upload_content_length']:
            _header_params['X-Upload-Content-Length'] = _params['x_upload_content_length']

        if _params['x_upload_content_type']:
            _header_params['X-Upload-Content-Type'] = _params['x_upload_content_type']

        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['video_upload_request_resumable'] is not None:
            _body_params = _params['video_upload_request_resumable']

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
            '/api/v1/videos/upload-resumable', 'POST',
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
