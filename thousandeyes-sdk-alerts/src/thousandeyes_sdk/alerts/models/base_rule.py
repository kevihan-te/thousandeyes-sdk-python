# coding: utf-8

"""
    Alerts API

    You can manage the following alert functionalities on the ThousandEyes platform using the Alerts API:  * **Alerts**: Retrieve alert details. Alerts are assigned to tests through alert rules.  * **Alert Rules**: Conditions that you configure in order to highlight or be notified of events of interest in your ThousandEyes tests. When an alert rule’s conditions are met, the associated alert is triggered and the alert becomes active. It remains active until the alert is cleared. Alert rules are reusable across multiple tests..  * **Alert Suppression Windows**: Suppress alerts for tests during periods such as planned maintenance. Windows can be one-time events or recurring events to handle periodic occurrences such as monthly downtime for maintenance.  For more information about the alerts, see [Alerts](https://docs.thousandeyes.com/product-documentation/alerts). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.alerts.models.alert_direction import AlertDirection
from thousandeyes_sdk.alerts.models.alert_rounds_violation_mode import AlertRoundsViolationMode
from thousandeyes_sdk.alerts.models.alert_type import AlertType
from thousandeyes_sdk.alerts.models.sensitivity_level import SensitivityLevel
from thousandeyes_sdk.alerts.models.severity import Severity
from typing import Optional, Set
from typing_extensions import Self

class BaseRule(BaseModel):
    """
    BaseRule
    """ # noqa: E501
    rule_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the rule.", alias="ruleId")
    rule_name: StrictStr = Field(description="Name of the alert rule.", alias="ruleName")
    expression: StrictStr = Field(description="The expression of the alert rule.")
    direction: Optional[AlertDirection] = None
    notify_on_clear: Optional[StrictBool] = Field(default=None, description="Send notification when alert clears.", alias="notifyOnClear")
    is_default: Optional[StrictBool] = Field(default=None, description="If set to `true`, this alert rule becomes the default for its test type and is automatically applied to newly created tests with relevant metrics. Only one default alert rule is allowed per test type.", alias="isDefault")
    alert_type: AlertType = Field(alias="alertType")
    minimum_sources: Optional[StrictInt] = Field(default=None, description="The minimum number of agents or monitors that must meet the specified criteria to trigger the alert.", alias="minimumSources")
    minimum_sources_pct: Optional[StrictInt] = Field(default=None, description="The minimum percentage of all assigned agents or monitors that must meet the specified criteria to trigger the alert.", alias="minimumSourcesPct")
    rounds_violating_mode: Optional[AlertRoundsViolationMode] = Field(default=None, alias="roundsViolatingMode")
    rounds_violating_out_of: StrictInt = Field(description="Specifies the divisor (y value) in the “X of Y times” condition.", alias="roundsViolatingOutOf")
    rounds_violating_required: StrictInt = Field(description="Specifies the numerator (x value) in the “X of Y times” condition.", alias="roundsViolatingRequired")
    include_covered_prefixes: Optional[StrictBool] = Field(default=None, description="Set true to include covered prefixes in the BGP alert rule. Only applicable to BGP alert rules.", alias="includeCoveredPrefixes")
    sensitivity_level: Optional[SensitivityLevel] = Field(default=None, alias="sensitivityLevel")
    severity: Optional[Severity] = None
    __properties: ClassVar[List[str]] = ["ruleId", "ruleName", "expression", "direction", "notifyOnClear", "isDefault", "alertType", "minimumSources", "minimumSourcesPct", "roundsViolatingMode", "roundsViolatingOutOf", "roundsViolatingRequired", "includeCoveredPrefixes", "sensitivityLevel", "severity"]

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
        """Create an instance of BaseRule from a JSON string"""
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
        excluded_fields: Set[str] = set([
            "rule_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BaseRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ruleId": obj.get("ruleId"),
            "ruleName": obj.get("ruleName"),
            "expression": obj.get("expression"),
            "direction": obj.get("direction"),
            "notifyOnClear": obj.get("notifyOnClear"),
            "isDefault": obj.get("isDefault"),
            "alertType": obj.get("alertType"),
            "minimumSources": obj.get("minimumSources"),
            "minimumSourcesPct": obj.get("minimumSourcesPct"),
            "roundsViolatingMode": obj.get("roundsViolatingMode"),
            "roundsViolatingOutOf": obj.get("roundsViolatingOutOf"),
            "roundsViolatingRequired": obj.get("roundsViolatingRequired"),
            "includeCoveredPrefixes": obj.get("includeCoveredPrefixes"),
            "sensitivityLevel": obj.get("sensitivityLevel"),
            "severity": obj.get("severity")
        })
        return _obj


