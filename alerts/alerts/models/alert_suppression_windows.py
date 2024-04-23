# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

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
from alerts.models.alert_suppression_windows_alert_suppression_windows_inner import AlertSuppressionWindowsAlertSuppressionWindowsInner
from typing import Optional, Set
from typing_extensions import Self

class AlertSuppressionWindows(BaseModel):
    """
    Alert suppression windows.
    """ # noqa: E501
    alert_suppression_windows: Optional[List[AlertSuppressionWindowsAlertSuppressionWindowsInner]] = Field(default=None, alias="alertSuppressionWindows")
    __properties: ClassVar[List[str]] = ["alertSuppressionWindows"]

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
        """Create an instance of AlertSuppressionWindows from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in alert_suppression_windows (list)
        _items = []
        if self.alert_suppression_windows:
            for _item in self.alert_suppression_windows:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alertSuppressionWindows'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlertSuppressionWindows from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alertSuppressionWindows": [AlertSuppressionWindowsAlertSuppressionWindowsInner.from_dict(_item) for _item in obj["alertSuppressionWindows"]] if obj.get("alertSuppressionWindows") is not None else None
        })
        return _obj


