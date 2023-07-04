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


from typing import Optional
from pydantic import BaseModel, Field, StrictStr
from peertube_api_client.models.server_config_auto_blacklist import ServerConfigAutoBlacklist
from peertube_api_client.models.server_config_avatar import ServerConfigAvatar
from peertube_api_client.models.server_config_email import ServerConfigEmail
from peertube_api_client.models.server_config_followings import ServerConfigFollowings
from peertube_api_client.models.server_config_import import ServerConfigImport
from peertube_api_client.models.server_config_instance import ServerConfigInstance
from peertube_api_client.models.server_config_plugin import ServerConfigPlugin
from peertube_api_client.models.server_config_search import ServerConfigSearch
from peertube_api_client.models.server_config_signup import ServerConfigSignup
from peertube_api_client.models.server_config_transcoding import ServerConfigTranscoding
from peertube_api_client.models.server_config_trending import ServerConfigTrending
from peertube_api_client.models.server_config_user import ServerConfigUser
from peertube_api_client.models.server_config_video import ServerConfigVideo
from peertube_api_client.models.server_config_video_caption import ServerConfigVideoCaption

class ServerConfig(BaseModel):
    """
    ServerConfig
    """
    instance: Optional[ServerConfigInstance] = None
    search: Optional[ServerConfigSearch] = None
    plugin: Optional[ServerConfigPlugin] = None
    theme: Optional[ServerConfigPlugin] = None
    email: Optional[ServerConfigEmail] = None
    contact_form: Optional[ServerConfigEmail] = Field(None, alias="contactForm")
    server_version: Optional[StrictStr] = Field(None, alias="serverVersion")
    server_commit: Optional[StrictStr] = Field(None, alias="serverCommit")
    signup: Optional[ServerConfigSignup] = None
    transcoding: Optional[ServerConfigTranscoding] = None
    var_import: Optional[ServerConfigImport] = Field(None, alias="import")
    auto_blacklist: Optional[ServerConfigAutoBlacklist] = Field(None, alias="autoBlacklist")
    avatar: Optional[ServerConfigAvatar] = None
    video: Optional[ServerConfigVideo] = None
    video_caption: Optional[ServerConfigVideoCaption] = Field(None, alias="videoCaption")
    user: Optional[ServerConfigUser] = None
    trending: Optional[ServerConfigTrending] = None
    tracker: Optional[ServerConfigEmail] = None
    followings: Optional[ServerConfigFollowings] = None
    homepage: Optional[ServerConfigEmail] = None
    __properties = ["instance", "search", "plugin", "theme", "email", "contactForm", "serverVersion", "serverCommit", "signup", "transcoding", "import", "autoBlacklist", "avatar", "video", "videoCaption", "user", "trending", "tracker", "followings", "homepage"]

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
    def from_json(cls, json_str: str) -> ServerConfig:
        """Create an instance of ServerConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of instance
        if self.instance:
            _dict['instance'] = self.instance.to_dict()
        # override the default output from pydantic by calling `to_dict()` of search
        if self.search:
            _dict['search'] = self.search.to_dict()
        # override the default output from pydantic by calling `to_dict()` of plugin
        if self.plugin:
            _dict['plugin'] = self.plugin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of theme
        if self.theme:
            _dict['theme'] = self.theme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of email
        if self.email:
            _dict['email'] = self.email.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_form
        if self.contact_form:
            _dict['contactForm'] = self.contact_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signup
        if self.signup:
            _dict['signup'] = self.signup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transcoding
        if self.transcoding:
            _dict['transcoding'] = self.transcoding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_import
        if self.var_import:
            _dict['import'] = self.var_import.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_blacklist
        if self.auto_blacklist:
            _dict['autoBlacklist'] = self.auto_blacklist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of avatar
        if self.avatar:
            _dict['avatar'] = self.avatar.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video
        if self.video:
            _dict['video'] = self.video.to_dict()
        # override the default output from pydantic by calling `to_dict()` of video_caption
        if self.video_caption:
            _dict['videoCaption'] = self.video_caption.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trending
        if self.trending:
            _dict['trending'] = self.trending.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tracker
        if self.tracker:
            _dict['tracker'] = self.tracker.to_dict()
        # override the default output from pydantic by calling `to_dict()` of followings
        if self.followings:
            _dict['followings'] = self.followings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of homepage
        if self.homepage:
            _dict['homepage'] = self.homepage.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerConfig:
        """Create an instance of ServerConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServerConfig.parse_obj(obj)

        _obj = ServerConfig.parse_obj({
            "instance": ServerConfigInstance.from_dict(obj.get("instance")) if obj.get("instance") is not None else None,
            "search": ServerConfigSearch.from_dict(obj.get("search")) if obj.get("search") is not None else None,
            "plugin": ServerConfigPlugin.from_dict(obj.get("plugin")) if obj.get("plugin") is not None else None,
            "theme": ServerConfigPlugin.from_dict(obj.get("theme")) if obj.get("theme") is not None else None,
            "email": ServerConfigEmail.from_dict(obj.get("email")) if obj.get("email") is not None else None,
            "contact_form": ServerConfigEmail.from_dict(obj.get("contactForm")) if obj.get("contactForm") is not None else None,
            "server_version": obj.get("serverVersion"),
            "server_commit": obj.get("serverCommit"),
            "signup": ServerConfigSignup.from_dict(obj.get("signup")) if obj.get("signup") is not None else None,
            "transcoding": ServerConfigTranscoding.from_dict(obj.get("transcoding")) if obj.get("transcoding") is not None else None,
            "var_import": ServerConfigImport.from_dict(obj.get("import")) if obj.get("import") is not None else None,
            "auto_blacklist": ServerConfigAutoBlacklist.from_dict(obj.get("autoBlacklist")) if obj.get("autoBlacklist") is not None else None,
            "avatar": ServerConfigAvatar.from_dict(obj.get("avatar")) if obj.get("avatar") is not None else None,
            "video": ServerConfigVideo.from_dict(obj.get("video")) if obj.get("video") is not None else None,
            "video_caption": ServerConfigVideoCaption.from_dict(obj.get("videoCaption")) if obj.get("videoCaption") is not None else None,
            "user": ServerConfigUser.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "trending": ServerConfigTrending.from_dict(obj.get("trending")) if obj.get("trending") is not None else None,
            "tracker": ServerConfigEmail.from_dict(obj.get("tracker")) if obj.get("tracker") is not None else None,
            "followings": ServerConfigFollowings.from_dict(obj.get("followings")) if obj.get("followings") is not None else None,
            "homepage": ServerConfigEmail.from_dict(obj.get("homepage")) if obj.get("homepage") is not None else None
        })
        return _obj

