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
from pydantic import BaseModel, Field, StrictInt, StrictStr, constr, validator
from peertube_api_client.models.runner_job_parent import RunnerJobParent
from peertube_api_client.models.runner_job_payload import RunnerJobPayload
from peertube_api_client.models.runner_job_runner import RunnerJobRunner
from peertube_api_client.models.runner_job_state_constant import RunnerJobStateConstant
from peertube_api_client.models.runner_job_type import RunnerJobType

class RunnerJob(BaseModel):
    """
    RunnerJob
    """
    uuid: Optional[constr(strict=True, max_length=36, min_length=36)] = None
    type: Optional[RunnerJobType] = None
    state: Optional[RunnerJobStateConstant] = None
    payload: Optional[RunnerJobPayload] = None
    failures: Optional[StrictInt] = Field(None, description="Number of times a remote runner failed to process this job. After too many failures, the job in \"error\" state")
    error: Optional[StrictStr] = Field(None, description="Error message if the job is errored")
    progress: Optional[StrictInt] = Field(None, description="Percentage progress")
    priority: Optional[StrictInt] = Field(None, description="Job priority (less has more priority)")
    updated_at: Optional[datetime] = Field(None, alias="updatedAt")
    created_at: Optional[datetime] = Field(None, alias="createdAt")
    started_at: Optional[datetime] = Field(None, alias="startedAt")
    finished_at: Optional[datetime] = Field(None, alias="finishedAt")
    parent: Optional[RunnerJobParent] = None
    runner: Optional[RunnerJobRunner] = None
    __properties = ["uuid", "type", "state", "payload", "failures", "error", "progress", "priority", "updatedAt", "createdAt", "startedAt", "finishedAt", "parent", "runner"]

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
    def from_json(cls, json_str: str) -> RunnerJob:
        """Create an instance of RunnerJob from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of state
        if self.state:
            _dict['state'] = self.state.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payload
        if self.payload:
            _dict['payload'] = self.payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of runner
        if self.runner:
            _dict['runner'] = self.runner.to_dict()
        # set to None if error (nullable) is None
        # and __fields_set__ contains the field
        if self.error is None and "error" in self.__fields_set__:
            _dict['error'] = None

        # set to None if parent (nullable) is None
        # and __fields_set__ contains the field
        if self.parent is None and "parent" in self.__fields_set__:
            _dict['parent'] = None

        # set to None if runner (nullable) is None
        # and __fields_set__ contains the field
        if self.runner is None and "runner" in self.__fields_set__:
            _dict['runner'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> RunnerJob:
        """Create an instance of RunnerJob from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return RunnerJob.parse_obj(obj)

        _obj = RunnerJob.parse_obj({
            "uuid": obj.get("uuid"),
            "type": obj.get("type"),
            "state": RunnerJobStateConstant.from_dict(obj.get("state")) if obj.get("state") is not None else None,
            "payload": RunnerJobPayload.from_dict(obj.get("payload")) if obj.get("payload") is not None else None,
            "failures": obj.get("failures"),
            "error": obj.get("error"),
            "progress": obj.get("progress"),
            "priority": obj.get("priority"),
            "updated_at": obj.get("updatedAt"),
            "created_at": obj.get("createdAt"),
            "started_at": obj.get("startedAt"),
            "finished_at": obj.get("finishedAt"),
            "parent": RunnerJobParent.from_dict(obj.get("parent")) if obj.get("parent") is not None else None,
            "runner": RunnerJobRunner.from_dict(obj.get("runner")) if obj.get("runner") is not None else None
        })
        return _obj

