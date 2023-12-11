# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

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
from test_results_api.models.rtp_stream_test_result import RtpStreamTestResult
from test_results_api.models.simple_test import SimpleTest
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class RtpStreamTestResults(BaseModel):
    """
    RtpStreamTestResults
    """ # noqa: E501
    results: Optional[List[RtpStreamTestResult]] = None
    test: Optional[SimpleTest] = None
    __properties: ClassVar[List[str]] = ["results", "test"]

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
        """Create an instance of RtpStreamTestResults from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in results (list)
        _items = []
        if self.results:
            for _item in self.results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['results'] = _items
        # override the default output from pydantic by calling `to_dict()` of test
        if self.test:
            _dict['test'] = self.test.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of RtpStreamTestResults from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "results": [RtpStreamTestResult.from_dict(_item) for _item in obj.get("results")] if obj.get("results") is not None else None,
            "test": SimpleTest.from_dict(obj.get("test")) if obj.get("test") is not None else None
        })
        return _obj


