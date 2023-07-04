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

from typing import Optional, Union

from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate
from peertube_api_client.models.video_upload_request_resumable import VideoUploadRequestResumable
from peertube_api_client.models.video_upload_response import VideoUploadResponse

from peertube_api_client.api_client import ApiClient
from peertube_api_client.api_response import ApiResponse
from peertube_api_client.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class VideoUploadApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def import_video(self, name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Video name")], channel_id : Annotated[conint(strict=True, ge=1), Field(..., description="Channel id that will contain this video")], privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictBool], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1, unique_items=True)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, **kwargs) -> VideoUploadResponse:  # noqa: E501
        """Import a video  # noqa: E501

        Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_video(name, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, async_req=True)
        >>> result = thread.get()

        :param name: Video name (required)
        :type name: str
        :param channel_id: Channel id that will contain this video (required)
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
            raise ValueError("Error! Please call the import_video_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.import_video_with_http_info(name, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, **kwargs)  # noqa: E501

    @validate_arguments
    def import_video_with_http_info(self, name : Annotated[constr(strict=True, max_length=120, min_length=3), Field(..., description="Video name")], channel_id : Annotated[conint(strict=True, ge=1), Field(..., description="Channel id that will contain this video")], privacy : Optional[VideoPrivacySet] = None, category : Annotated[Optional[StrictInt], Field(description="category id of the video (see [/videos/categories](#operation/getCategories))")] = None, licence : Annotated[Optional[StrictInt], Field(description="licence id of the video (see [/videos/licences](#operation/getLicences))")] = None, language : Annotated[Optional[StrictStr], Field(description="language id of the video (see [/videos/languages](#operation/getLanguages))")] = None, description : Annotated[Optional[StrictStr], Field(description="Video description")] = None, wait_transcoding : Annotated[Optional[StrictBool], Field(description="Whether or not we wait transcoding before publish the video")] = None, support : Annotated[Optional[StrictStr], Field(description="A text tell the audience how to support the video creator")] = None, nsfw : Annotated[Optional[StrictBool], Field(description="Whether or not this video contains sensitive content")] = None, tags : Annotated[Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1, unique_items=True)], Field(description="Video tags (maximum 5 tags each between 2 and 30 characters)")] = None, comments_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable comments for this video")] = None, download_enabled : Annotated[Optional[StrictBool], Field(description="Enable or disable downloading for this video")] = None, originally_published_at : Annotated[Optional[datetime], Field(description="Date when the content was originally published")] = None, schedule_update : Optional[VideoScheduledUpdate] = None, thumbnailfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video thumbnail file")] = None, previewfile : Annotated[Optional[Union[StrictBytes, StrictStr]], Field(description="Video preview file")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Import a video  # noqa: E501

        Import a torrent or magnetURI or HTTP resource (if enabled by the instance administrator)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.import_video_with_http_info(name, channel_id, privacy, category, licence, language, description, wait_transcoding, support, nsfw, tags, comments_enabled, download_enabled, originally_published_at, schedule_update, thumbnailfile, previewfile, async_req=True)
        >>> result = thread.get()

        :param name: Video name (required)
        :type name: str
        :param channel_id: Channel id that will contain this video (required)
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
                    " to method import_video" % _key
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
            '409': None,
        }

        return self.api_client.call_api(
            '/api/v1/videos/imports', 'POST',
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
