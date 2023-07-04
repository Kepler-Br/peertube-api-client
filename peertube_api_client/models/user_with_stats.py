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
from peertube_api_client.models.nsfw_policy import NSFWPolicy
from peertube_api_client.models.user_role import UserRole
from peertube_api_client.models.video_channel import VideoChannel

class UserWithStats(BaseModel):
    """
    UserWithStats
    """
    account: Optional[Account] = None
    auto_play_next_video: Optional[StrictBool] = Field(None, alias="autoPlayNextVideo", description="Automatically start playing the upcoming video after the currently playing video")
    auto_play_next_video_playlist: Optional[StrictBool] = Field(None, alias="autoPlayNextVideoPlaylist", description="Automatically start playing the video on the playlist after the currently playing video")
    auto_play_video: Optional[StrictBool] = Field(None, alias="autoPlayVideo", description="Automatically start playing the video on the watch page")
    blocked: Optional[StrictBool] = None
    blocked_reason: Optional[StrictStr] = Field(None, alias="blockedReason")
    created_at: Optional[StrictStr] = Field(None, alias="createdAt")
    email: Optional[StrictStr] = Field(None, description="The user email")
    email_verified: Optional[StrictBool] = Field(None, alias="emailVerified", description="Has the user confirmed their email address?")
    id: Optional[conint(strict=True, ge=1)] = None
    plugin_auth: Optional[StrictStr] = Field(None, alias="pluginAuth", description="Auth plugin to use to authenticate the user")
    last_login_date: Optional[datetime] = Field(None, alias="lastLoginDate")
    no_instance_config_warning_modal: Optional[StrictBool] = Field(None, alias="noInstanceConfigWarningModal")
    no_account_setup_warning_modal: Optional[StrictBool] = Field(None, alias="noAccountSetupWarningModal")
    no_welcome_modal: Optional[StrictBool] = Field(None, alias="noWelcomeModal")
    nsfw_policy: Optional[NSFWPolicy] = Field(None, alias="nsfwPolicy")
    role: Optional[UserRole] = None
    theme: Optional[StrictStr] = Field(None, description="Theme enabled by this user")
    username: Optional[constr(strict=True, max_length=50, min_length=1)] = Field(None, description="immutable name of the user, used to find or mention its actor")
    video_channels: Optional[conlist(VideoChannel)] = Field(None, alias="videoChannels")
    video_quota: Optional[StrictInt] = Field(None, alias="videoQuota", description="The user video quota in bytes")
    video_quota_daily: Optional[StrictInt] = Field(None, alias="videoQuotaDaily", description="The user daily video quota in bytes")
    p2p_enabled: Optional[StrictBool] = Field(None, alias="p2pEnabled", description="Enable P2P in the player")
    videos_count: Optional[StrictInt] = Field(None, alias="videosCount", description="Count of videos published")
    abuses_count: Optional[StrictInt] = Field(None, alias="abusesCount", description="Count of reports/abuses of which the user is a target")
    abuses_accepted_count: Optional[StrictInt] = Field(None, alias="abusesAcceptedCount", description="Count of reports/abuses created by the user and accepted/acted upon by the moderation team")
    abuses_created_count: Optional[StrictInt] = Field(None, alias="abusesCreatedCount", description="Count of reports/abuses created by the user")
    video_comments_count: Optional[StrictInt] = Field(None, alias="videoCommentsCount", description="Count of comments published")
    __properties = ["account", "autoPlayNextVideo", "autoPlayNextVideoPlaylist", "autoPlayVideo", "blocked", "blockedReason", "createdAt", "email", "emailVerified", "id", "pluginAuth", "lastLoginDate", "noInstanceConfigWarningModal", "noAccountSetupWarningModal", "noWelcomeModal", "nsfwPolicy", "role", "theme", "username", "videoChannels", "videoQuota", "videoQuotaDaily", "p2pEnabled", "videosCount", "abusesCount", "abusesAcceptedCount", "abusesCreatedCount", "videoCommentsCount"]

    @validator('username')
    def username_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-z0-9._]+$", value):
            raise ValueError(r"must validate the regular expression /^[a-z0-9._]+$/")
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
    def from_json(cls, json_str: str) -> UserWithStats:
        """Create an instance of UserWithStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of role
        if self.role:
            _dict['role'] = self.role.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in video_channels (list)
        _items = []
        if self.video_channels:
            for _item in self.video_channels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['videoChannels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UserWithStats:
        """Create an instance of UserWithStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return UserWithStats.parse_obj(obj)

        _obj = UserWithStats.parse_obj({
            "account": Account.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "auto_play_next_video": obj.get("autoPlayNextVideo"),
            "auto_play_next_video_playlist": obj.get("autoPlayNextVideoPlaylist"),
            "auto_play_video": obj.get("autoPlayVideo"),
            "blocked": obj.get("blocked"),
            "blocked_reason": obj.get("blockedReason"),
            "created_at": obj.get("createdAt"),
            "email": obj.get("email"),
            "email_verified": obj.get("emailVerified"),
            "id": obj.get("id"),
            "plugin_auth": obj.get("pluginAuth"),
            "last_login_date": obj.get("lastLoginDate"),
            "no_instance_config_warning_modal": obj.get("noInstanceConfigWarningModal"),
            "no_account_setup_warning_modal": obj.get("noAccountSetupWarningModal"),
            "no_welcome_modal": obj.get("noWelcomeModal"),
            "nsfw_policy": obj.get("nsfwPolicy"),
            "role": UserRole.from_dict(obj.get("role")) if obj.get("role") is not None else None,
            "theme": obj.get("theme"),
            "username": obj.get("username"),
            "video_channels": [VideoChannel.from_dict(_item) for _item in obj.get("videoChannels")] if obj.get("videoChannels") is not None else None,
            "video_quota": obj.get("videoQuota"),
            "video_quota_daily": obj.get("videoQuotaDaily"),
            "p2p_enabled": obj.get("p2pEnabled"),
            "videos_count": obj.get("videosCount"),
            "abuses_count": obj.get("abusesCount"),
            "abuses_accepted_count": obj.get("abusesAcceptedCount"),
            "abuses_created_count": obj.get("abusesCreatedCount"),
            "video_comments_count": obj.get("videoCommentsCount")
        })
        return _obj

