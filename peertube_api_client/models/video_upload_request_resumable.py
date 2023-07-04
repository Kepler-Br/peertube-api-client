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
from typing import List, Optional, Union
from pydantic import BaseModel, Field, StrictBool, StrictBytes, StrictInt, StrictStr, conint, conlist, constr
from peertube_api_client.models.video_privacy_set import VideoPrivacySet
from peertube_api_client.models.video_scheduled_update import VideoScheduledUpdate

class VideoUploadRequestResumable(BaseModel):
    """
    VideoUploadRequestResumable
    """
    name: constr(strict=True, max_length=120, min_length=3) = Field(..., description="Video name")
    channel_id: conint(strict=True, ge=1) = Field(..., alias="channelId", description="Channel id that will contain this video")
    privacy: Optional[VideoPrivacySet] = None
    category: Optional[StrictInt] = Field(None, description="category id of the video (see [/videos/categories](#operation/getCategories))")
    licence: Optional[StrictInt] = Field(None, description="licence id of the video (see [/videos/licences](#operation/getLicences))")
    language: Optional[StrictStr] = Field(None, description="language id of the video (see [/videos/languages](#operation/getLanguages))")
    description: Optional[StrictStr] = Field(None, description="Video description")
    wait_transcoding: Optional[StrictBool] = Field(None, alias="waitTranscoding", description="Whether or not we wait transcoding before publish the video")
    support: Optional[StrictStr] = Field(None, description="A text tell the audience how to support the video creator")
    nsfw: Optional[StrictBool] = Field(None, description="Whether or not this video contains sensitive content")
    tags: Optional[conlist(constr(strict=True, max_length=30, min_length=2), max_items=5, min_items=1, unique_items=True)] = Field(None, description="Video tags (maximum 5 tags each between 2 and 30 characters)")
    comments_enabled: Optional[StrictBool] = Field(None, alias="commentsEnabled", description="Enable or disable comments for this video")
    download_enabled: Optional[StrictBool] = Field(None, alias="downloadEnabled", description="Enable or disable downloading for this video")
    originally_published_at: Optional[datetime] = Field(None, alias="originallyPublishedAt", description="Date when the content was originally published")
    schedule_update: Optional[VideoScheduledUpdate] = Field(None, alias="scheduleUpdate")
    thumbnailfile: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="Video thumbnail file")
    previewfile: Optional[Union[StrictBytes, StrictStr]] = Field(None, description="Video preview file")
    filename: StrictStr = Field(..., description="Video filename including extension")
    __properties = ["name", "channelId", "privacy", "category", "licence", "language", "description", "waitTranscoding", "support", "nsfw", "tags", "commentsEnabled", "downloadEnabled", "originallyPublishedAt", "scheduleUpdate", "thumbnailfile", "previewfile", "filename"]

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
    def from_json(cls, json_str: str) -> VideoUploadRequestResumable:
        """Create an instance of VideoUploadRequestResumable from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of schedule_update
        if self.schedule_update:
            _dict['scheduleUpdate'] = self.schedule_update.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideoUploadRequestResumable:
        """Create an instance of VideoUploadRequestResumable from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideoUploadRequestResumable.parse_obj(obj)

        _obj = VideoUploadRequestResumable.parse_obj({
            "name": obj.get("name"),
            "channel_id": obj.get("channelId"),
            "privacy": obj.get("privacy"),
            "category": obj.get("category"),
            "licence": obj.get("licence"),
            "language": obj.get("language"),
            "description": obj.get("description"),
            "wait_transcoding": obj.get("waitTranscoding"),
            "support": obj.get("support"),
            "nsfw": obj.get("nsfw"),
            "tags": obj.get("tags"),
            "comments_enabled": obj.get("commentsEnabled"),
            "download_enabled": obj.get("downloadEnabled"),
            "originally_published_at": obj.get("originallyPublishedAt"),
            "schedule_update": VideoScheduledUpdate.from_dict(obj.get("scheduleUpdate")) if obj.get("scheduleUpdate") is not None else None,
            "thumbnailfile": obj.get("thumbnailfile"),
            "previewfile": obj.get("previewfile"),
            "filename": obj.get("filename")
        })
        return _obj

