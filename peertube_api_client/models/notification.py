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
from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictInt, conint
from peertube_api_client.models.actor_info import ActorInfo
from peertube_api_client.models.notification_actor_follow import NotificationActorFollow
from peertube_api_client.models.notification_comment import NotificationComment
from peertube_api_client.models.notification_video import NotificationVideo
from peertube_api_client.models.notification_video_abuse import NotificationVideoAbuse
from peertube_api_client.models.notification_video_import import NotificationVideoImport

class Notification(BaseModel):
    """
    Notification
    """
    id: Optional[conint(strict=True, ge=1)] = None
    type: Optional[StrictInt] = Field(None, description="Notification type, following the `UserNotificationType` enum: - `1` NEW_VIDEO_FROM_SUBSCRIPTION - `2` NEW_COMMENT_ON_MY_VIDEO - `3` NEW_ABUSE_FOR_MODERATORS - `4` BLACKLIST_ON_MY_VIDEO - `5` UNBLACKLIST_ON_MY_VIDEO - `6` MY_VIDEO_PUBLISHED - `7` MY_VIDEO_IMPORT_SUCCESS - `8` MY_VIDEO_IMPORT_ERROR - `9` NEW_USER_REGISTRATION - `10` NEW_FOLLOW - `11` COMMENT_MENTION - `12` VIDEO_AUTO_BLACKLIST_FOR_MODERATORS - `13` NEW_INSTANCE_FOLLOWER - `14` AUTO_INSTANCE_FOLLOWING - `15` ABUSE_STATE_CHANGE - `16` ABUSE_NEW_MESSAGE - `17` NEW_PLUGIN_VERSION - `18` NEW_PEERTUBE_VERSION ")
    read: Optional[StrictBool] = None
    video: Optional[NotificationVideo] = None
    video_import: Optional[NotificationVideoImport] = Field(None, alias="videoImport")
    comment: Optional[NotificationComment] = None
    video_abuse: Optional[NotificationVideoAbuse] = Field(None, alias="videoAbuse")
    video_blacklist: Optional[NotificationVideoAbuse] = Field(None, alias="videoBlacklist")
    account: Optional[ActorInfo] = None
    actor_follow: Optional[NotificationActorFollow] = Field(None, alias="actorFollow")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    __properties = ["id", "type", "read", "video", "videoImport", "comment", "videoAbuse", "videoBlacklist", "account", "actorFollow", "createdAt", "updatedAt"]

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
    def from_json(cls, json_str: str) -> Notification:
        """Create an instance of Notification from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_import
        if self.video_import:
            _dict['videoImport'] = self.video_import.to_dict()
        # override the default output from pydantic by calling `to_dict()` of comment
        if self.comment:
            _dict['comment'] = self.comment.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_abuse
        if self.video_abuse:
            _dict['videoAbuse'] = self.video_abuse.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_blacklist
        if self.video_blacklist:
            _dict['videoBlacklist'] = self.video_blacklist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of actor_follow
        if self.actor_follow:
            _dict['actorFollow'] = self.actor_follow.to_dict()
        # set to None if video (nullable) is None
        # and __fields_set__ contains the field
        if self.video is None and "video" in self.__fields_set__:
            _dict['video'] = None

        # set to None if video_import (nullable) is None
        # and __fields_set__ contains the field
        if self.video_import is None and "video_import" in self.__fields_set__:
            _dict['videoImport'] = None

        # set to None if comment (nullable) is None
        # and __fields_set__ contains the field
        if self.comment is None and "comment" in self.__fields_set__:
            _dict['comment'] = None

        # set to None if video_abuse (nullable) is None
        # and __fields_set__ contains the field
        if self.video_abuse is None and "video_abuse" in self.__fields_set__:
            _dict['videoAbuse'] = None

        # set to None if video_blacklist (nullable) is None
        # and __fields_set__ contains the field
        if self.video_blacklist is None and "video_blacklist" in self.__fields_set__:
            _dict['videoBlacklist'] = None

        # set to None if account (nullable) is None
        # and __fields_set__ contains the field
        if self.account is None and "account" in self.__fields_set__:
            _dict['account'] = None

        # set to None if actor_follow (nullable) is None
        # and __fields_set__ contains the field
        if self.actor_follow is None and "actor_follow" in self.__fields_set__:
            _dict['actorFollow'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Notification:
        """Create an instance of Notification from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return Notification.parse_obj(obj)

        _obj = Notification.parse_obj({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "read": obj.get("read"),
            "video": NotificationVideo.from_dict(obj.get("video")) if obj.get("video") is not None else None,
            "video_import": NotificationVideoImport.from_dict(obj.get("videoImport")) if obj.get("videoImport") is not None else None,
            "comment": NotificationComment.from_dict(obj.get("comment")) if obj.get("comment") is not None else None,
            "video_abuse": NotificationVideoAbuse.from_dict(obj.get("videoAbuse")) if obj.get("videoAbuse") is not None else None,
            "video_blacklist": NotificationVideoAbuse.from_dict(obj.get("videoBlacklist")) if obj.get("videoBlacklist") is not None else None,
            "account": ActorInfo.from_dict(obj.get("account")) if obj.get("account") is not None else None,
            "actor_follow": NotificationActorFollow.from_dict(obj.get("actorFollow")) if obj.get("actorFollow") is not None else None,
            "created_at": obj.get("createdAt"),
            "updated_at": obj.get("updatedAt")
        })
        return _obj

