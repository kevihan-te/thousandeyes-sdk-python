# coding: utf-8

"""
    Agents API

     ## Overview Manage Cloud and Enterprise Agents available to your account in ThousandEyes.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.agents.models.agent_notification import AgentNotification
from thousandeyes_sdk.agents.models.agent_response import AgentResponse
from thousandeyes_sdk.agents.models.self_links import SelfLinks
from typing import Optional, Set
from typing_extensions import Self

class NotificationRuleDetail(BaseModel):
    """
    NotificationRuleDetail
    """ # noqa: E501
    rule_id: Optional[StrictStr] = Field(default=None, description="Agent notification rule ID", alias="ruleId")
    rule_name: Optional[StrictStr] = Field(default=None, description="Name of the agent notification rule", alias="ruleName")
    expression: Optional[StrictStr] = Field(default=None, description="Expression of agent notification rule")
    notify_on_clear: Optional[StrictBool] = Field(default=None, description="Send notification when notification clears", alias="notifyOnClear")
    is_default: Optional[StrictBool] = Field(default=None, description="Agent notification rule will be automatically included on all new Enterprise Agents.", alias="isDefault")
    notifications: Optional[AgentNotification] = None
    agents: Optional[List[AgentResponse]] = None
    links: Optional[SelfLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["ruleId", "ruleName", "expression", "notifyOnClear", "isDefault", "notifications", "agents", "_links"]

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
        """Create an instance of NotificationRuleDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of notifications
        if self.notifications:
            _dict['notifications'] = self.notifications.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item in self.agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agents'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NotificationRuleDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ruleId": obj.get("ruleId"),
            "ruleName": obj.get("ruleName"),
            "expression": obj.get("expression"),
            "notifyOnClear": obj.get("notifyOnClear"),
            "isDefault": obj.get("isDefault"),
            "notifications": AgentNotification.from_dict(obj["notifications"]) if obj.get("notifications") is not None else None,
            "agents": [AgentResponse.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None,
            "_links": SelfLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None
        })
        return _obj


