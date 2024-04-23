# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from endpoint_test_results.models.asn_details import AsnDetails
from endpoint_test_results.models.network_profile import NetworkProfile
from endpoint_test_results.models.path_vis_route import PathVisRoute
from endpoint_test_results.models.system_metrics import SystemMetrics
from endpoint_test_results.models.vpn_profile import VpnProfile
from typing import Optional, Set
from typing_extensions import Self

class PathVisDetailTestResult(BaseModel):
    """
    PathVisDetailTestResult
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    server_ip: Optional[StrictStr] = Field(default=None, description="IP address of target server.", alias="serverIp")
    network_profile: Optional[NetworkProfile] = Field(default=None, alias="networkProfile")
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    vpn_profile: Optional[VpnProfile] = Field(default=None, alias="vpnProfile")
    asn_details: Optional[AsnDetails] = Field(default=None, alias="asnDetails")
    server: Optional[StrictStr] = Field(default=None, description="Target server, including port.")
    source_ip: Optional[StrictStr] = Field(default=None, description="IP address of source endpoint agent.", alias="sourceIp")
    source_prefix: Optional[StrictStr] = Field(default=None, description="IP prefix of source endpoint agent.", alias="sourcePrefix")
    path_traces: Optional[List[PathVisRoute]] = Field(default=None, description="Shows iterations of path trace, with each iteration specified by a pathId.", alias="pathTraces")
    vpn_path_traces: Optional[List[PathVisRoute]] = Field(default=None, description="Shows iterations of the VPN path trace, with each iteration specified by a pathId.", alias="vpnPathTraces")
    __properties: ClassVar[List[str]] = ["aid", "agentId", "roundId", "serverIp", "networkProfile", "systemMetrics", "vpnProfile", "asnDetails", "server", "sourceIp", "sourcePrefix", "pathTraces", "vpnPathTraces"]

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
        """Create an instance of PathVisDetailTestResult from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "agent_id",
            "round_id",
            "server_ip",
            "server",
            "source_ip",
            "source_prefix",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of network_profile
        if self.network_profile:
            _dict['networkProfile'] = self.network_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_metrics
        if self.system_metrics:
            _dict['systemMetrics'] = self.system_metrics.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpn_profile
        if self.vpn_profile:
            _dict['vpnProfile'] = self.vpn_profile.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asn_details
        if self.asn_details:
            _dict['asnDetails'] = self.asn_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in path_traces (list)
        _items = []
        if self.path_traces:
            for _item in self.path_traces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['pathTraces'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vpn_path_traces (list)
        _items = []
        if self.vpn_path_traces:
            for _item in self.vpn_path_traces:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vpnPathTraces'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PathVisDetailTestResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "agentId": obj.get("agentId"),
            "roundId": obj.get("roundId"),
            "serverIp": obj.get("serverIp"),
            "networkProfile": NetworkProfile.from_dict(obj["networkProfile"]) if obj.get("networkProfile") is not None else None,
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None,
            "vpnProfile": VpnProfile.from_dict(obj["vpnProfile"]) if obj.get("vpnProfile") is not None else None,
            "asnDetails": AsnDetails.from_dict(obj["asnDetails"]) if obj.get("asnDetails") is not None else None,
            "server": obj.get("server"),
            "sourceIp": obj.get("sourceIp"),
            "sourcePrefix": obj.get("sourcePrefix"),
            "pathTraces": [PathVisRoute.from_dict(_item) for _item in obj["pathTraces"]] if obj.get("pathTraces") is not None else None,
            "vpnPathTraces": [PathVisRoute.from_dict(_item) for _item in obj["vpnPathTraces"]] if obj.get("vpnPathTraces") is not None else None
        })
        return _obj


