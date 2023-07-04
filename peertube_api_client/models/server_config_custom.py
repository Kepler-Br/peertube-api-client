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
from pydantic import BaseModel, Field
from peertube_api_client.models.server_config_auto_blacklist import ServerConfigAutoBlacklist
from peertube_api_client.models.server_config_custom_admin import ServerConfigCustomAdmin
from peertube_api_client.models.server_config_custom_cache import ServerConfigCustomCache
from peertube_api_client.models.server_config_custom_followers import ServerConfigCustomFollowers
from peertube_api_client.models.server_config_custom_import import ServerConfigCustomImport
from peertube_api_client.models.server_config_custom_instance import ServerConfigCustomInstance
from peertube_api_client.models.server_config_custom_services import ServerConfigCustomServices
from peertube_api_client.models.server_config_custom_signup import ServerConfigCustomSignup
from peertube_api_client.models.server_config_custom_theme import ServerConfigCustomTheme
from peertube_api_client.models.server_config_custom_transcoding import ServerConfigCustomTranscoding
from peertube_api_client.models.server_config_custom_user import ServerConfigCustomUser
from peertube_api_client.models.server_config_email import ServerConfigEmail

class ServerConfigCustom(BaseModel):
    """
    ServerConfigCustom
    """
    instance: Optional[ServerConfigCustomInstance] = None
    theme: Optional[ServerConfigCustomTheme] = None
    services: Optional[ServerConfigCustomServices] = None
    cache: Optional[ServerConfigCustomCache] = None
    signup: Optional[ServerConfigCustomSignup] = None
    admin: Optional[ServerConfigCustomAdmin] = None
    contact_form: Optional[ServerConfigEmail] = Field(None, alias="contactForm")
    user: Optional[ServerConfigCustomUser] = None
    transcoding: Optional[ServerConfigCustomTranscoding] = None
    var_import: Optional[ServerConfigCustomImport] = Field(None, alias="import")
    auto_blacklist: Optional[ServerConfigAutoBlacklist] = Field(None, alias="autoBlacklist")
    followers: Optional[ServerConfigCustomFollowers] = None
    __properties = ["instance", "theme", "services", "cache", "signup", "admin", "contactForm", "user", "transcoding", "import", "autoBlacklist", "followers"]

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
    def from_json(cls, json_str: str) -> ServerConfigCustom:
        """Create an instance of ServerConfigCustom from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of theme
        if self.theme:
            _dict['theme'] = self.theme.to_dict()
        # override the default output from pydantic by calling `to_dict()` of services
        if self.services:
            _dict['services'] = self.services.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cache
        if self.cache:
            _dict['cache'] = self.cache.to_dict()
        # override the default output from pydantic by calling `to_dict()` of signup
        if self.signup:
            _dict['signup'] = self.signup.to_dict()
        # override the default output from pydantic by calling `to_dict()` of admin
        if self.admin:
            _dict['admin'] = self.admin.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_form
        if self.contact_form:
            _dict['contactForm'] = self.contact_form.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user
        if self.user:
            _dict['user'] = self.user.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transcoding
        if self.transcoding:
            _dict['transcoding'] = self.transcoding.to_dict()
        # override the default output from pydantic by calling `to_dict()` of var_import
        if self.var_import:
            _dict['import'] = self.var_import.to_dict()
        # override the default output from pydantic by calling `to_dict()` of auto_blacklist
        if self.auto_blacklist:
            _dict['autoBlacklist'] = self.auto_blacklist.to_dict()
        # override the default output from pydantic by calling `to_dict()` of followers
        if self.followers:
            _dict['followers'] = self.followers.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ServerConfigCustom:
        """Create an instance of ServerConfigCustom from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ServerConfigCustom.parse_obj(obj)

        _obj = ServerConfigCustom.parse_obj({
            "instance": ServerConfigCustomInstance.from_dict(obj.get("instance")) if obj.get("instance") is not None else None,
            "theme": ServerConfigCustomTheme.from_dict(obj.get("theme")) if obj.get("theme") is not None else None,
            "services": ServerConfigCustomServices.from_dict(obj.get("services")) if obj.get("services") is not None else None,
            "cache": ServerConfigCustomCache.from_dict(obj.get("cache")) if obj.get("cache") is not None else None,
            "signup": ServerConfigCustomSignup.from_dict(obj.get("signup")) if obj.get("signup") is not None else None,
            "admin": ServerConfigCustomAdmin.from_dict(obj.get("admin")) if obj.get("admin") is not None else None,
            "contact_form": ServerConfigEmail.from_dict(obj.get("contactForm")) if obj.get("contactForm") is not None else None,
            "user": ServerConfigCustomUser.from_dict(obj.get("user")) if obj.get("user") is not None else None,
            "transcoding": ServerConfigCustomTranscoding.from_dict(obj.get("transcoding")) if obj.get("transcoding") is not None else None,
            "var_import": ServerConfigCustomImport.from_dict(obj.get("import")) if obj.get("import") is not None else None,
            "auto_blacklist": ServerConfigAutoBlacklist.from_dict(obj.get("autoBlacklist")) if obj.get("autoBlacklist") is not None else None,
            "followers": ServerConfigCustomFollowers.from_dict(obj.get("followers")) if obj.get("followers") is not None else None
        })
        return _obj

