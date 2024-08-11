# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.instant_tests.models.request_method import RequestMethod
from thousandeyes_sdk.instant_tests.models.test_auth_type import TestAuthType
from typing import Optional, Set
from typing_extensions import Self

class OAuth(BaseModel):
    """
    Use this only if you want to use OAuth as the authentication mechanism.
    """ # noqa: E501
    config_id: Optional[StrictStr] = Field(default=None, description="The ID of the OAuth configuration.", alias="configId")
    test_url: Optional[StrictStr] = Field(default=None, description="Target for the test.", alias="testUrl")
    request_method: Optional[RequestMethod] = Field(default=None, alias="requestMethod")
    post_body: Optional[StrictStr] = Field(default=None, description="Enter the OAuth body for the HTTP POST request in this field when using OAuth as the authentication mechanism. No special escaping is required. If content is provided in the post body, the `requestMethod` is automatically set to POST.", alias="postBody")
    headers: Optional[StrictStr] = Field(default=None, description="Request headers used for OAuth.")
    auth_type: Optional[TestAuthType] = Field(default=None, alias="authType")
    username: Optional[StrictStr] = Field(default=None, description="OAuth username")
    password: Optional[StrictStr] = Field(default=None, description="OAuth password")
    __properties: ClassVar[List[str]] = ["configId", "testUrl", "requestMethod", "postBody", "headers", "authType", "username", "password"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
        extra="allow",
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return self.model_dump_json(by_alias=True, exclude_unset=True, exclude_none=True)

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of OAuth from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OAuth from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "configId": obj.get("configId"),
            "testUrl": obj.get("testUrl"),
            "requestMethod": obj.get("requestMethod"),
            "postBody": obj.get("postBody"),
            "headers": obj.get("headers"),
            "authType": obj.get("authType"),
            "username": obj.get("username"),
            "password": obj.get("password")
        })
        return _obj


