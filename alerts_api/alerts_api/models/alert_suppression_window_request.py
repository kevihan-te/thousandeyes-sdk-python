# coding: utf-8

"""
    Alerts API

     ## Overview Manage all alerts, alert rules and alert suppression windows.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from alerts_api.models.alert_suppression_window_state import AlertSuppressionWindowState
from alerts_api.models.end_repeat import EndRepeat
from alerts_api.models.repeat import Repeat
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlertSuppressionWindowRequest(BaseModel):
    """
    AlertSuppressionWindowRequest
    """ # noqa: E501
    alert_suppression_window_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the alert suppression window.", alias="alertSuppressionWindowId")
    name: Optional[StrictStr] = Field(default=None, description="Name of the alert suppression window.")
    is_enabled: Optional[StrictBool] = Field(default=None, description="Set to `false` for `disabled`, `true` for `enabled`.", alias="isEnabled")
    status: Optional[AlertSuppressionWindowState] = None
    start_date: Optional[datetime] = Field(default=None, description="The date/time when the alert suppression window starts (ISO date-time format).", alias="startDate")
    duration: Optional[StrictInt] = Field(default=None, description="Duration in seconds the suppression window is active.")
    repeat: Optional[Repeat] = None
    end_repeat: Optional[EndRepeat] = Field(default=None, alias="endRepeat")
    tests: Optional[List[StrictStr]] = Field(default=None, description="List of tests to assign to the alert suppression window.")
    __properties: ClassVar[List[str]] = ["alertSuppressionWindowId", "name", "isEnabled", "status", "startDate", "duration", "repeat", "endRepeat", "tests"]

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
        """Create an instance of AlertSuppressionWindowRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "alert_suppression_window_id",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of repeat
        if self.repeat:
            _dict['repeat'] = self.repeat.to_dict()
        # override the default output from pydantic by calling `to_dict()` of end_repeat
        if self.end_repeat:
            _dict['endRepeat'] = self.end_repeat.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AlertSuppressionWindowRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertSuppressionWindowId": obj.get("alertSuppressionWindowId"),
            "name": obj.get("name"),
            "isEnabled": obj.get("isEnabled"),
            "status": obj.get("status"),
            "startDate": obj.get("startDate"),
            "duration": obj.get("duration"),
            "repeat": Repeat.from_dict(obj.get("repeat")) if obj.get("repeat") is not None else None,
            "endRepeat": EndRepeat.from_dict(obj.get("endRepeat")) if obj.get("endRepeat") is not None else None,
            "tests": obj.get("tests")
        })
        return _obj


