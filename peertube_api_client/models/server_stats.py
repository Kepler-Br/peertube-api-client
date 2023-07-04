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


from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictFloat, StrictInt, conlist
from peertube_api_client.models.server_stats_videos_redundancy_inner import ServerStatsVideosRedundancyInner

class ServerStats(BaseModel):
    """
    ServerStats
    """
    total_users: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalUsers")
    total_daily_active_users: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalDailyActiveUsers")
    total_weekly_active_users: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalWeeklyActiveUsers")
    total_monthly_active_users: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalMonthlyActiveUsers")
    total_local_videos: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalVideos")
    total_local_video_views: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalVideoViews", description="Total video views made on the instance")
    total_local_video_comments: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalVideoComments", description="Total comments made by local users")
    total_local_video_files_size: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalVideoFilesSize")
    total_videos: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalVideos")
    total_video_comments: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalVideoComments")
    total_local_video_channels: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalVideoChannels")
    total_local_daily_active_video_channels: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalDailyActiveVideoChannels")
    total_local_weekly_active_video_channels: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalWeeklyActiveVideoChannels")
    total_local_monthly_active_video_channels: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalMonthlyActiveVideoChannels")
    total_local_playlists: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalLocalPlaylists")
    total_instance_followers: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalInstanceFollowers")
    total_instance_following: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalInstanceFollowing")
    videos_redundancy: Optional[conlist(ServerStatsVideosRedundancyInner)] = Field(None, alias="videosRedundancy")
    total_activity_pub_messages_processed: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalActivityPubMessagesProcessed")
    total_activity_pub_messages_successes: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalActivityPubMessagesSuccesses")
    total_activity_pub_messages_errors: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalActivityPubMessagesErrors")
    activity_pub_messages_processed_per_second: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="activityPubMessagesProcessedPerSecond")
    total_activity_pub_messages_waiting: Optional[Union[StrictFloat, StrictInt]] = Field(None, alias="totalActivityPubMessagesWaiting")
    __properties = ["totalUsers", "totalDailyActiveUsers", "totalWeeklyActiveUsers", "totalMonthlyActiveUsers", "totalLocalVideos", "totalLocalVideoViews", "totalLocalVideoComments", "totalLocalVideoFilesSize", "totalVideos", "totalVideoComments", "totalLocalVideoChannels", "totalLocalDailyActiveVideoChannels", "totalLocalWeeklyActiveVideoChannels", "totalLocalMonthlyActiveVideoChannels", "totalLocalPlaylists", "totalInstanceFollowers", "totalInstanceFollowing", "videosRedundancy", "totalActivityPubMessagesProcessed", "totalActivityPubMessagesSuccesses", "totalActivityPubMessagesErrors", "activityPubMessagesProcessedPerSecond", "totalActivityPubMessagesWaiting"]

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
    def from_json(cls, json_str: str) -> ServerStats:
        """Create an instance of ServerStats from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in videos_redundancy (list)
        _items = []
        if self.videos_redundancy:
            for _item in self.videos_redundancy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['videosRedundancy'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerStats:
        """Create an instance of ServerStats from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServerStats.parse_obj(obj)

        _obj = ServerStats.parse_obj({
            "total_users": obj.get("totalUsers"),
            "total_daily_active_users": obj.get("totalDailyActiveUsers"),
            "total_weekly_active_users": obj.get("totalWeeklyActiveUsers"),
            "total_monthly_active_users": obj.get("totalMonthlyActiveUsers"),
            "total_local_videos": obj.get("totalLocalVideos"),
            "total_local_video_views": obj.get("totalLocalVideoViews"),
            "total_local_video_comments": obj.get("totalLocalVideoComments"),
            "total_local_video_files_size": obj.get("totalLocalVideoFilesSize"),
            "total_videos": obj.get("totalVideos"),
            "total_video_comments": obj.get("totalVideoComments"),
            "total_local_video_channels": obj.get("totalLocalVideoChannels"),
            "total_local_daily_active_video_channels": obj.get("totalLocalDailyActiveVideoChannels"),
            "total_local_weekly_active_video_channels": obj.get("totalLocalWeeklyActiveVideoChannels"),
            "total_local_monthly_active_video_channels": obj.get("totalLocalMonthlyActiveVideoChannels"),
            "total_local_playlists": obj.get("totalLocalPlaylists"),
            "total_instance_followers": obj.get("totalInstanceFollowers"),
            "total_instance_following": obj.get("totalInstanceFollowing"),
            "videos_redundancy": [ServerStatsVideosRedundancyInner.from_dict(_item) for _item in obj.get("videosRedundancy")] if obj.get("videosRedundancy") is not None else None,
            "total_activity_pub_messages_processed": obj.get("totalActivityPubMessagesProcessed"),
            "total_activity_pub_messages_successes": obj.get("totalActivityPubMessagesSuccesses"),
            "total_activity_pub_messages_errors": obj.get("totalActivityPubMessagesErrors"),
            "activity_pub_messages_processed_per_second": obj.get("activityPubMessagesProcessedPerSecond"),
            "total_activity_pub_messages_waiting": obj.get("totalActivityPubMessagesWaiting")
        })
        return _obj

