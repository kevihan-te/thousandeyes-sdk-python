# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_self_link import EndpointTestSelfLink
from thousandeyes_sdk.endpoint_test_results.models.link import Link
from typing import Optional, Set
from typing_extensions import Self

class EndpointTestLinks(BaseModel):
    """
    A list of links that can be accessed to get more information.
    """ # noqa: E501
    var_self: Optional[EndpointTestSelfLink] = Field(default=None, alias="self")
    test_results: Optional[List[Link]] = Field(default=None, description="Reference to the test results.", alias="testResults")
    __properties: ClassVar[List[str]] = ["self", "testResults"]

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
        """Create an instance of EndpointTestLinks from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in test_results (list)
        _items = []
        if self.test_results:
            for _item in self.test_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['testResults'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointTestLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "self": EndpointTestSelfLink.from_dict(obj["self"]) if obj.get("self") is not None else None,
            "testResults": [Link.from_dict(_item) for _item in obj["testResults"]] if obj.get("testResults") is not None else None
        })
        return _obj


