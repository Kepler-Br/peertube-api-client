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
from pydantic import BaseModel, Field, StrictInt, StrictStr, conlist, validator
from peertube_api_client.models.videos_for_xml_inner_enclosure import VideosForXMLInnerEnclosure
from peertube_api_client.models.videos_for_xml_inner_media_community import VideosForXMLInnerMediaCommunity
from peertube_api_client.models.videos_for_xml_inner_media_embed import VideosForXMLInnerMediaEmbed
from peertube_api_client.models.videos_for_xml_inner_media_group_inner import VideosForXMLInnerMediaGroupInner
from peertube_api_client.models.videos_for_xml_inner_media_player import VideosForXMLInnerMediaPlayer
from peertube_api_client.models.videos_for_xml_inner_media_thumbnail import VideosForXMLInnerMediaThumbnail

class VideosForXMLInner(BaseModel):
    """
    VideosForXMLInner
    """
    link: Optional[StrictStr] = Field(None, description="video watch page URL")
    guid: Optional[StrictStr] = Field(None, description="video canonical URL")
    pub_date: Optional[datetime] = Field(None, alias="pubDate", description="video publication date")
    description: Optional[StrictStr] = Field(None, description="video description")
    contentencoded: Optional[StrictStr] = Field(None, alias="content:encoded", description="video description")
    dccreator: Optional[StrictStr] = Field(None, alias="dc:creator", description="publisher user name")
    mediacategory: Optional[StrictInt] = Field(None, alias="media:category", description="video category (MRSS)")
    mediacommunity: Optional[VideosForXMLInnerMediaCommunity] = Field(None, alias="media:community")
    mediaembed: Optional[VideosForXMLInnerMediaEmbed] = Field(None, alias="media:embed")
    mediaplayer: Optional[VideosForXMLInnerMediaPlayer] = Field(None, alias="media:player")
    mediathumbnail: Optional[VideosForXMLInnerMediaThumbnail] = Field(None, alias="media:thumbnail")
    mediatitle: Optional[StrictStr] = Field(None, alias="media:title", description="see [media:title](https://www.rssboard.org/media-rss#media-title) (MRSS). We only use `plain` titles.")
    mediadescription: Optional[StrictStr] = Field(None, alias="media:description")
    mediarating: Optional[StrictStr] = Field(None, alias="media:rating", description="see [media:rating](https://www.rssboard.org/media-rss#media-rating) (MRSS)")
    enclosure: Optional[VideosForXMLInnerEnclosure] = None
    mediagroup: Optional[conlist(VideosForXMLInnerMediaGroupInner)] = Field(None, alias="media:group", description="list of streamable files for the video. see [media:peerLink](https://www.rssboard.org/media-rss#media-peerlink) and [media:content](https://www.rssboard.org/media-rss#media-content) or  (MRSS)")
    __properties = ["link", "guid", "pubDate", "description", "content:encoded", "dc:creator", "media:category", "media:community", "media:embed", "media:player", "media:thumbnail", "media:title", "media:description", "media:rating", "enclosure", "media:group"]

    @validator('mediarating')
    def mediarating_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('nonadult', 'adult'):
            raise ValueError("must be one of enum values ('nonadult', 'adult')")
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
    def from_json(cls, json_str: str) -> VideosForXMLInner:
        """Create an instance of VideosForXMLInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of mediacommunity
        if self.mediacommunity:
            _dict['media:community'] = self.mediacommunity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mediaembed
        if self.mediaembed:
            _dict['media:embed'] = self.mediaembed.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mediaplayer
        if self.mediaplayer:
            _dict['media:player'] = self.mediaplayer.to_dict()
        # override the default output from pydantic by calling `to_dict()` of mediathumbnail
        if self.mediathumbnail:
            _dict['media:thumbnail'] = self.mediathumbnail.to_dict()
        # override the default output from pydantic by calling `to_dict()` of enclosure
        if self.enclosure:
            _dict['enclosure'] = self.enclosure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in mediagroup (list)
        _items = []
        if self.mediagroup:
            for _item in self.mediagroup:
                if _item:
                    _items.append(_item.to_dict())
            _dict['media:group'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> VideosForXMLInner:
        """Create an instance of VideosForXMLInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return VideosForXMLInner.parse_obj(obj)

        _obj = VideosForXMLInner.parse_obj({
            "link": obj.get("link"),
            "guid": obj.get("guid"),
            "pub_date": obj.get("pubDate"),
            "description": obj.get("description"),
            "contentencoded": obj.get("content:encoded"),
            "dccreator": obj.get("dc:creator"),
            "mediacategory": obj.get("media:category"),
            "mediacommunity": VideosForXMLInnerMediaCommunity.from_dict(obj.get("media:community")) if obj.get("media:community") is not None else None,
            "mediaembed": VideosForXMLInnerMediaEmbed.from_dict(obj.get("media:embed")) if obj.get("media:embed") is not None else None,
            "mediaplayer": VideosForXMLInnerMediaPlayer.from_dict(obj.get("media:player")) if obj.get("media:player") is not None else None,
            "mediathumbnail": VideosForXMLInnerMediaThumbnail.from_dict(obj.get("media:thumbnail")) if obj.get("media:thumbnail") is not None else None,
            "mediatitle": obj.get("media:title"),
            "mediadescription": obj.get("media:description"),
            "mediarating": obj.get("media:rating"),
            "enclosure": VideosForXMLInnerEnclosure.from_dict(obj.get("enclosure")) if obj.get("enclosure") is not None else None,
            "mediagroup": [VideosForXMLInnerMediaGroupInner.from_dict(_item) for _item in obj.get("media:group")] if obj.get("media:group") is not None else None
        })
        return _obj

