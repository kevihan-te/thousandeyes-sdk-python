# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from snapshots_api.models.unexpanded_instant_test_links_self import UnexpandedInstantTestLinksSelf
from snapshots_api.models.unexpanded_instant_test_links_test_results import UnexpandedInstantTestLinksTestResults
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class UnexpandedInstantTestLinks(BaseModel):
    """
    A list of links that can be accessed to get more information
    """ # noqa: E501
    var_self: Optional[UnexpandedInstantTestLinksSelf] = Field(default=None, alias="self")
    test_results: Optional[UnexpandedInstantTestLinksTestResults] = Field(default=None, alias="testResults")
    __properties: ClassVar[List[str]] = ["self", "testResults"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UnexpandedInstantTestLinks from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of var_self
        if self.var_self:
            _dict['self'] = self.var_self.to_dict()
        # override the default output from pydantic by calling `to_dict()` of test_results
        if self.test_results:
            _dict['testResults'] = self.test_results.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of UnexpandedInstantTestLinks from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "self": UnexpandedInstantTestLinksSelf.from_dict(obj.get("self")) if obj.get("self") is not None else None,
            "testResults": UnexpandedInstantTestLinksTestResults.from_dict(obj.get("testResults")) if obj.get("testResults") is not None else None
        })
        return _obj


