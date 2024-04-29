# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from endpoint_agents.models.endpoint_browser_extension import EndpointBrowserExtension
from endpoint_agents.models.endpoint_user_profile import EndpointUserProfile
from typing import Optional, Set
from typing_extensions import Self

class EndpointClient(BaseModel):
    """
    Information about the user who has the agent installed.
    """ # noqa: E501
    user_profile: Optional[EndpointUserProfile] = Field(default=None, alias="userProfile")
    browser_extensions: Optional[List[EndpointBrowserExtension]] = Field(default=None, alias="browserExtensions")
    __properties: ClassVar[List[str]] = ["userProfile", "browserExtensions"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of EndpointClient from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of user_profile
        if self.user_profile:
            _dict['userProfile'] = self.user_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in browser_extensions (list)
        _items = []
        if self.browser_extensions:
            for _item in self.browser_extensions:
                if _item:
                    _items.append(_item.to_dict())
            _dict['browserExtensions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "userProfile": EndpointUserProfile.from_dict(obj["userProfile"]) if obj.get("userProfile") is not None else None,
            "browserExtensions": [EndpointBrowserExtension.from_dict(_item) for _item in obj["browserExtensions"]] if obj.get("browserExtensions") is not None else None
        })
        return _obj


