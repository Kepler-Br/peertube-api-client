# coding: utf-8

"""
    PeerTube

    The PeerTube API is built on HTTP(S) and is RESTful. You can use your favorite HTTP/REST library for your programming language to use PeerTube. The spec API is fully compatible with [openapi-generator](https://github.com/OpenAPITools/openapi-generator/wiki/API-client-generator-HOWTO) which generates a client SDK in the language of your choice - we generate some client SDKs automatically:  - [Python](https://framagit.org/framasoft/peertube/clients/python) - [Go](https://framagit.org/framasoft/peertube/clients/go) - [Kotlin](https://framagit.org/framasoft/peertube/clients/kotlin)  See the [REST API quick start](https://docs.joinpeertube.org/api/rest-getting-started) for a few examples of using the PeerTube API.  # Authentication  When you sign up for an account on a PeerTube instance, you are given the possibility to generate sessions on it, and authenticate there using an access token. Only __one access token can currently be used at a time__.  ## Roles  Accounts are given permissions based on their role. There are three roles on PeerTube: Administrator, Moderator, and User. See the [roles guide](https://docs.joinpeertube.org/admin/managing-users#roles) for a detail of their permissions.  # Errors  The API uses standard HTTP status codes to indicate the success or failure of the API call, completed by a [RFC7807-compliant](https://tools.ietf.org/html/rfc7807) response body.  ``` HTTP 1.1 404 Not Found Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Video not found\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"status\": 404,   \"title\": \"Not Found\",   \"type\": \"about:blank\" } ```  We provide error `type` values for [a growing number of cases](https://github.com/Chocobozzz/PeerTube/blob/develop/shared/models/server/server-error-code.enum.ts), but it is still optional. Types are used to disambiguate errors that bear the same status code and are non-obvious:  ``` HTTP 1.1 403 Forbidden Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Cannot get this video regarding follow constraints\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"status\": 403,   \"title\": \"Forbidden\",   \"type\": \"https://docs.joinpeertube.org/api-rest-reference.html#section/Errors/does_not_respect_follow_constraints\" } ```  Here a 403 error could otherwise mean that the video is private or blocklisted.  ### Validation errors  Each parameter is evaluated on its own against a set of rules before the route validator proceeds with potential testing involving parameter combinations. Errors coming from validation errors appear earlier and benefit from a more detailed error description:  ``` HTTP 1.1 400 Bad Request Content-Type: application/problem+json; charset=utf-8  {   \"detail\": \"Incorrect request parameters: id\",   \"docs\": \"https://docs.joinpeertube.org/api-rest-reference.html#operation/getVideo\",   \"instance\": \"/api/v1/videos/9c9de5e8-0a1e-484a-b099-e80766180\",   \"invalid-params\": {     \"id\": {       \"location\": \"params\",       \"msg\": \"Invalid value\",       \"param\": \"id\",       \"value\": \"9c9de5e8-0a1e-484a-b099-e80766180\"     }   },   \"status\": 400,   \"title\": \"Bad Request\",   \"type\": \"about:blank\" } ```  Where `id` is the name of the field concerned by the error, within the route definition. `invalid-params.<field>.location` can be either 'params', 'body', 'header', 'query' or 'cookies', and `invalid-params.<field>.value` reports the value that didn't pass validation whose `invalid-params.<field>.msg` is about.  ### Deprecated error fields  Some fields could be included with previous versions. They are still included but their use is deprecated: - `error`: superseded by `detail` - `code`: superseded by `type` (which is now an URI)  # Rate limits  We are rate-limiting all endpoints of PeerTube's API. Custom values can be set by administrators:  | Endpoint (prefix: `/api/v1`) | Calls         | Time frame   | |------------------------------|---------------|--------------| | `/*`                         | 50            | 10 seconds   | | `POST /users/token`          | 15            | 5 minutes    | | `POST /users/register`       | 2<sup>*</sup> | 5 minutes    | | `POST /users/ask-send-verify-email` | 3      | 5 minutes    |  Depending on the endpoint, <sup>*</sup>failed requests are not taken into account. A service limit is announced by a `429 Too Many Requests` status code.  You can get details about the current state of your rate limit by reading the following headers:  | Header                  | Description                                                | |-------------------------|------------------------------------------------------------| | `X-RateLimit-Limit`     | Number of max requests allowed in the current time period  | | `X-RateLimit-Remaining` | Number of remaining requests in the current time period    | | `X-RateLimit-Reset`     | Timestamp of end of current time period as UNIX timestamp  | | `Retry-After`           | Seconds to delay after the first `429` is received         |  # CORS  This API features [Cross-Origin Resource Sharing (CORS)](https://fetch.spec.whatwg.org/), allowing cross-domain communication from the browser for some routes:  | Endpoint                    | |------------------------- ---| | `/api/*`                    | | `/download/*`               | | `/lazy-static/*`            | | `/.well-known/webfinger`    |  In addition, all routes serving ActivityPub are CORS-enabled for all origins.   # noqa: E501

    The version of the OpenAPI document: 5.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr, conint, conlist, constr, validator
from peertube_api_client.models.account import Account
from peertube_api_client.models.video_category import VideoCategory
from peertube_api_client.models.video_channel import VideoChannel
from peertube_api_client.models.video_file import VideoFile
from peertube_api_client.models.video_language import VideoLanguage
from peertube_api_client.models.video_licence import VideoLicence
from peertube_api_client.models.video_privacy import VideoPrivacy
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate
from peertube_api_client.models.video_state import VideoState
from peertube_api_client.models.video_streaming_playlists import VideoStreamingPlaylists
from peertube_api_client.models.video_user_history import VideoUserHistory

class VideoDetails(BaseModel):
    """
    VideoDetails
    """
    id: Optional[conint(strict=True, ge=1)] = None
    uuid: Optional[constr(strict=True, max_length=36, min_length=36)] = None
    short_uuid: Optional[StrictStr] = Field(None, alias="shortUUID", description="translation of a uuid v4 with a bigger alphabet to have a shorter uuid")
    is_live: Optional[StrictBool] = Field(None, alias="isLive")
    created_at: Optional[datetime] = Field(None, alias="createdAt", description="time at which the video object was first drafted")
    published_at: Optional[datetime] = Field(None, alias="publishedAt", description="time at which the video was marked as ready for playback (with restrictions depending on `privacy`). Usually set after a `state` evolution.")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt", description="last time the video's metadata was modified")
    originally_published_at: Optional[datetime] = Field(None, alias="originallyPublishedAt", description="used to represent a date of first publication, prior to the practical publication date of `publishedAt`")
    category: Optional[VideoCategory] = None
    licence: Optional[VideoLicence] = None
    language: Optional[VideoLanguage] = None
    privacy: Optional[VideoPrivacy] = None
    description: Optional[constr(strict=True, max_length=250, min_length=3)] = Field(None, description="truncated description of the video, written in Markdown. Resolve `descriptionPath` to get the full description of maximum `10000` characters. ")
    duration: Optional[StrictInt] = Field(None, description="duration of the video in seconds")
    is_local: Optional[StrictBool] = Field(None, alias="isLocal")
    name: Optional[constr(strict=True, max_length=120, min_length=3)] = Field(None, description="title of the video")
    thumbnail_path: Optional[StrictStr] = Field(None, alias="thumbnailPath")
    preview_path: Optional[StrictStr] = Field(None, alias="previewPath")
    embed_path: Optional[StrictStr] = Field(None, alias="embedPath")
    views: Optional[StrictInt] = None
    likes: Optional[StrictInt] = None
    dislikes: Optional[StrictInt] = None
    nsfw: Optional[StrictBool] = None
    wait_transcoding: Optional[StrictBool] = Field(None, alias="waitTranscoding")
    state: Optional[VideoState] = None
    scheduled_update: Optional[VideoScheduledUpdate] = Field(None, alias="scheduledUpdate")
    blacklisted: Optional[StrictBool] = None
    blacklisted_reason: Optional[StrictStr] = Field(None, alias="blacklistedReason")
    account: Optional[Account] = None
    channel: Optional[VideoChannel] = None
    user_history: Optional[VideoUserHistory] = Field(None, alias="userHistory")
    viewers: Optional[StrictInt] = Field(None, description="If the video is a live, you have the amount of current viewers")
    description_path: Optional[StrictStr] = Field(None, alias="descriptionPath", description="path at which to get the full description of maximum `10000` characters")
    support: Optional[constr(strict=True, max_length=1000, min_length=3)] = Field(None, description="A text tell the audience how to support the video creator")
    tags: Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1)] = None
    comments_enabled: Optional[StrictBool] = Field(None, alias="commentsEnabled")
    download_enabled: Optional[StrictBool] = Field(None, alias="downloadEnabled")
    tracker_urls: Optional[conlist(StrictStr)] = Field(None, alias="trackerUrls")
    files: Optional[conlist(VideoFile)] = Field(None, description="WebTorrent/raw video files. If WebTorrent is disabled on the server:  - field will be empty - video files will be found in `streamingPlaylists[].files` field ")
    streaming_playlists: Optional[conlist(VideoStreamingPlaylists)] = Field(None, alias="streamingPlaylists", description="HLS playlists/manifest files. If HLS is disabled on the server:  - field will be empty - video files will be found in `files` field ")
    __properties = ["id", "uuid", "shortUUID", "isLive", "createdAt", "publishedAt", "updatedAt", "originallyPublishedAt", "category", "licence", "language", "privacy", "description", "duration", "isLocal", "name", "thumbnailPath", "previewPath", "embedPath", "views", "likes", "dislikes", "nsfw", "waitTranscoding", "state", "scheduledUpdate", "blacklisted", "blacklistedReason", "account", "channel", "userHistory", "viewers", "descriptionPath", "support", "tags", "commentsEnabled", "downloadEnabled", "trackerUrls", "files", "streamingPlaylists"]

    @validator('uuid')
    def uuid_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", value):
            raise ValueError(r"must validate the regular expression /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/")
        return value

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> VideoDetails:
        """Create an instance of VideoDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        # override the default output from pydantic by calling `to_dict()` of licence
        if self.licence:
            _dict['licence'] = self.licence.to_dict()
        # override the default output from pydantic by calling `to_dict()` of language
        if self.language:
            _dict['language'] = self.language.to_dict()
        # override the default output from pydantic by calling `to_dict()` of privacy
        if self.privacy:
            _dict['privacy'] = self.privacy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scheduled_update
        if self.scheduled_update:
            _dict['scheduledUpdate'] = self.scheduled_update.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of channel
        if self.channel:
            _dict['channel'] = self.channel.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_history
        if self.user_history:
            _dict['userHistory'] = self.user_history.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in files (list)
        _items = []
        if self.files:
            for _item in self.files:
                if _item:
                    _items.append(_item.to_dict())
            _dict['files'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in streaming_playlists (list)
        _items = []
        if self.streaming_playlists:
            for _item in self.streaming_playlists:
                if _item:
                    _items.append(_item.to_dict())
            _dict['streamingPlaylists'] = _items
        # set to None if wait_transcoding (nullable) is None
        # and __fields_set__ contains the field
        if self.wait_transcoding is None and "wait_transcoding" in self.__fields_set__:
            _dict['waitTranscoding'] = None

        # set to None if scheduled_update (nullable) is None
        # and __fields_set__ contains the field
        if self.scheduled_update is None and "scheduled_update" in self.__fields_set__:
            _dict['scheduledUpdate'] = None

        # set to None if blacklisted (nullable) is None
        # and __fields_set__ contains the field
        if self.blacklisted is None and "blacklisted" in self.__fields_set__:
            _dict['blacklisted'] = None

        # set to None if blacklisted_reason (nullable) is None
        # and __fields_set__ contains the field
        if self.blacklisted_reason is None and "blacklisted_reason" in self.__fields_set__:
            _dict['blacklistedReason'] = None

        # set to None if user_history (nullable) is None
        # and __fields_set__ contains the field
        if self.user_history is None and "user_history" in self.__fields_set__:
            _dict['userHistory'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoDetails:
        """Create an instance of VideoDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoDetails.parse_obj(obj)

        _obj = VideoDetails.parse_obj({
            "id": obj.get("id"),
            "uuid": obj.get("uuid"),
            "short_uuid": obj.get("shortUUID"),
            "is_live": obj.get("isLive"),
            "created_at": obj.get("createdAt"),
            "published_at": obj.get("publishedAt"),
            "updated_at": obj.get("updatedAt"),
            "originally_published_at": obj.get("originallyPublishedAt"),
            "category": VideoCategory.from_dict(obj.get("category")) if obj.get("category") is not None else None,
            "licence": VideoLicence.from_dict(obj.get("licence")) if obj.get("licence") is not None else None,
            "language": VideoLanguage.from_dict(obj.get("language")) if obj.get("language") is not None else None,
            "privacy": VideoPrivacy.from_dict(obj.get("privacy")) if obj.get("privacy") is not None else None,
            "description": obj.get("description"),
            "duration": obj.get("duration"),
            "is_local": obj.get("isLocal"),
            "name": obj.get("name"),
            "thumbnail_path": obj.get("thumbnailPath"),
            "preview_path": obj.get("previewPath"),
            "embed_path": obj.get("embedPath"),
            "views": obj.get("views"),
            "likes": obj.get("likes"),
            "dislikes": obj.get("dislikes"),
            "nsfw": obj.get("nsfw"),
            "wait_transcoding": obj.get("waitTranscoding"),
            "state": VideoState.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "scheduled_update": VideoScheduledUpdate.from_dict(obj.get("scheduledUpdate")) if obj.get("scheduledUpdate") is not None else None,
            "blacklisted": obj.get("blacklisted"),
            "blacklisted_reason": obj.get("blacklistedReason"),
            "account": Account.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "channel": VideoChannel.from_dict(obj.get("channel")) if obj.get("channel") is not None else None,
            "user_history": VideoUserHistory.from_dict(obj.get("userHistory")) if obj.get("userHistory") is not None else None,
            "viewers": obj.get("viewers"),
            "description_path": obj.get("descriptionPath"),
            "support": obj.get("support"),
            "tags": obj.get("tags"),
            "comments_enabled": obj.get("commentsEnabled"),
            "download_enabled": obj.get("downloadEnabled"),
            "tracker_urls": obj.get("trackerUrls"),
            "files": [VideoFile.from_dict(_item) for _item in obj.get("files")] if obj.get("files") is not None else None,
            "streaming_playlists": [VideoStreamingPlaylists.from_dict(_item) for _item in obj.get("streamingPlaylists")] if obj.get("streamingPlaylists") is not None else None
        })
        return _obj

