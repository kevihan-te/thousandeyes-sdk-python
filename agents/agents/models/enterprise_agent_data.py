# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from agents.models.account_group import AccountGroup
from agents.models.cluster_member import ClusterMember
from agents.models.enterprise_agent_ipv6_policy import EnterpriseAgentIpv6Policy
from agents.models.enterprise_agent_state import EnterpriseAgentState
from agents.models.error_detail import ErrorDetail
from agents.models.interface_ip_mapping import InterfaceIpMapping
from typing import Optional, Set
from typing_extensions import Self

class EnterpriseAgentData(BaseModel):
    """
    EnterpriseAgentData
    """ # noqa: E501
    cluster_members: Optional[List[ClusterMember]] = Field(default=None, description="If an enterprise agent is clustered, detailed information about each cluster member will be shown as array entries in the clusterMembers field. This field is not shown for Enterprise Agents in standalone mode, or for Cloud Agents.", alias="clusterMembers")
    utilization: Optional[StrictInt] = Field(default=None, description="Shows overall utilization percentage (online Enterprise Agents and Enterprise Clusters only).")
    account_groups: Optional[List[AccountGroup]] = Field(default=None, description="List of account groups. See /accounts-groups to pull a list of account IDs", alias="accountGroups")
    ipv6_policy: Optional[EnterpriseAgentIpv6Policy] = Field(default=None, alias="ipv6Policy")
    error_details: Optional[List[ErrorDetail]] = Field(default=None, description="If an enterprise agent or a cluster member presents at least one error, the errors will be shown as an array of entries in the errorDetails field (Enterprise Agents and Enterprise Cluster members only)", alias="errorDetails")
    hostname: Optional[StrictStr] = Field(default=None, description="Fully qualified domain name of the agent (Enterprise Agents only)")
    last_seen: Optional[datetime] = Field(default=None, description="UTC last seen date (ISO date-time format).", alias="lastSeen")
    agent_state: Optional[EnterpriseAgentState] = Field(default=None, alias="agentState")
    keep_browser_cache: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent retains cache.", alias="keepBrowserCache")
    created_date: Optional[datetime] = Field(default=None, description="UTC Agent creation date (ISO date-time format).", alias="createdDate")
    target_for_tests: Optional[StrictStr] = Field(default=None, description="Test target IP address.", alias="targetForTests")
    local_resolution_prefixes: Optional[List[StrictStr]] = Field(default=None, description="To perform rDNS lookups for public IP ranges, this field represents the public IP ranges. The range must be in CIDR notation; for example, 10.1.1.0/24. Maximum of 5 prefixes allowed (Enterprise Agents and Enterprise Agent clusters only).", alias="localResolutionPrefixes")
    interface_ip_mappings: Optional[List[InterfaceIpMapping]] = Field(default=None, alias="interfaceIpMappings")
    __properties: ClassVar[List[str]] = ["clusterMembers", "utilization", "accountGroups", "ipv6Policy", "errorDetails", "hostname", "lastSeen", "agentState", "keepBrowserCache", "createdDate", "targetForTests", "localResolutionPrefixes", "interfaceIpMappings"]

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
        """Create an instance of EnterpriseAgentData from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "cluster_members",
            "utilization",
            "error_details",
            "hostname",
            "last_seen",
            "created_date",
            "interface_ip_mappings",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in cluster_members (list)
        _items = []
        if self.cluster_members:
            for _item in self.cluster_members:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clusterMembers'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in account_groups (list)
        _items = []
        if self.account_groups:
            for _item in self.account_groups:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountGroups'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in error_details (list)
        _items = []
        if self.error_details:
            for _item in self.error_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errorDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in interface_ip_mappings (list)
        _items = []
        if self.interface_ip_mappings:
            for _item in self.interface_ip_mappings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['interfaceIpMappings'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EnterpriseAgentData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "clusterMembers": [ClusterMember.from_dict(_item) for _item in obj["clusterMembers"]] if obj.get("clusterMembers") is not None else None,
            "utilization": obj.get("utilization"),
            "accountGroups": [AccountGroup.from_dict(_item) for _item in obj["accountGroups"]] if obj.get("accountGroups") is not None else None,
            "ipv6Policy": obj.get("ipv6Policy"),
            "errorDetails": [ErrorDetail.from_dict(_item) for _item in obj["errorDetails"]] if obj.get("errorDetails") is not None else None,
            "hostname": obj.get("hostname"),
            "lastSeen": obj.get("lastSeen"),
            "agentState": obj.get("agentState"),
            "keepBrowserCache": obj.get("keepBrowserCache"),
            "createdDate": obj.get("createdDate"),
            "targetForTests": obj.get("targetForTests"),
            "localResolutionPrefixes": obj.get("localResolutionPrefixes"),
            "interfaceIpMappings": [InterfaceIpMapping.from_dict(_item) for _item in obj["interfaceIpMappings"]] if obj.get("interfaceIpMappings") is not None else None
        })
        return _obj


