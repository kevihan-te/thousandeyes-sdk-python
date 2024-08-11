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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from thousandeyes_sdk.endpoint_test_results.models.gateway_network_ping import GatewayNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.target_network_ping import TargetNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.target_traceroute import TargetTraceroute
from thousandeyes_sdk.endpoint_test_results.models.vpn_network_ping import VpnNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.vpn_traceroute import VpnTraceroute
from typing import Optional, Set
from typing_extensions import Self

class RealUserTestNetwork(BaseModel):
    """
    Contains details about network profile and conditions during session.
    """ # noqa: E501
    network_profile: Optional[NetworkProfile] = Field(default=None, alias="networkProfile")
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    gateway_ping: Optional[GatewayNetworkPing] = Field(default=None, alias="gatewayPing")
    ping: Optional[TargetNetworkPing] = None
    traceroute: Optional[TargetTraceroute] = None
    connect_rtt: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Represents the number of milliseconds required to establish TCP connectivity with the target.", alias="connectRtt")
    is_icmp_blocked: Optional[StrictBool] = Field(default=None, description="Set to `true` if network target is blocking ICMP echo (ping) queries.", alias="isIcmpBlocked")
    errors: Optional[List[StrictStr]] = Field(default=None, description="Array of string representing possible network errors.")
    vpn_ping: Optional[VpnNetworkPing] = Field(default=None, alias="vpnPing")
    vpn_traceroute: Optional[VpnTraceroute] = Field(default=None, alias="vpnTraceroute")
    __properties: ClassVar[List[str]] = ["networkProfile", "systemMetrics", "gatewayPing", "ping", "traceroute", "connectRtt", "isIcmpBlocked", "errors", "vpnPing", "vpnTraceroute"]

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
        """Create an instance of RealUserTestNetwork from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "connect_rtt",
            "is_icmp_blocked",
            "errors",
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
        # override the default output from pydantic by calling `to_dict()` of gateway_ping
        if self.gateway_ping:
            _dict['gatewayPing'] = self.gateway_ping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ping
        if self.ping:
            _dict['ping'] = self.ping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of traceroute
        if self.traceroute:
            _dict['traceroute'] = self.traceroute.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpn_ping
        if self.vpn_ping:
            _dict['vpnPing'] = self.vpn_ping.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpn_traceroute
        if self.vpn_traceroute:
            _dict['vpnTraceroute'] = self.vpn_traceroute.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RealUserTestNetwork from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "networkProfile": NetworkProfile.from_dict(obj["networkProfile"]) if obj.get("networkProfile") is not None else None,
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None,
            "gatewayPing": GatewayNetworkPing.from_dict(obj["gatewayPing"]) if obj.get("gatewayPing") is not None else None,
            "ping": TargetNetworkPing.from_dict(obj["ping"]) if obj.get("ping") is not None else None,
            "traceroute": TargetTraceroute.from_dict(obj["traceroute"]) if obj.get("traceroute") is not None else None,
            "connectRtt": obj.get("connectRtt"),
            "isIcmpBlocked": obj.get("isIcmpBlocked"),
            "errors": obj.get("errors"),
            "vpnPing": VpnNetworkPing.from_dict(obj["vpnPing"]) if obj.get("vpnPing") is not None else None,
            "vpnTraceroute": VpnTraceroute.from_dict(obj["vpnTraceroute"]) if obj.get("vpnTraceroute") is not None else None
        })
        return _obj


