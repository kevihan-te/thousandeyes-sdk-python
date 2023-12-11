# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.

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
from agents_api.models.agent_license_type import AgentLicenseType
from agents_api.models.endpoint_agent_aid import EndpointAgentAid
from agents_api.models.endpoint_agent_location import EndpointAgentLocation
from agents_api.models.endpoint_asn_details import EndpointAsnDetails
from agents_api.models.endpoint_client import EndpointClient
from agents_api.models.endpoint_vpn_profile import EndpointVpnProfile
from agents_api.models.interface_profile import InterfaceProfile
from agents_api.models.platform import Platform
from agents_api.models.status import Status
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class EndpointAgent(BaseModel):
    """
    The `EndpointAgent` object, which may include multiple clients.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the agent this applies to.")
    aid: Optional[EndpointAgentAid] = None
    name: Optional[StrictStr] = Field(default=None, description="The name of the agent.")
    computer_name: Optional[StrictStr] = Field(default=None, alias="computerName")
    os_version: Optional[StrictStr] = Field(default=None, alias="osVersion")
    platform: Optional[Platform] = None
    kernel_version: Optional[StrictStr] = Field(default=None, alias="kernelVersion")
    manufacturer: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    last_seen: Optional[datetime] = Field(default=None, description="The last time the agent checked-in.", alias="lastSeen")
    status: Optional[Status] = None
    deleted: Optional[StrictBool] = None
    version: Optional[StrictStr] = Field(default=None, description="Version of the agent software running.")
    created_at: Optional[datetime] = Field(default=None, alias="createdAt")
    number_of_clients: Optional[StrictInt] = Field(default=None, alias="numberOfClients")
    public_ip: Optional[StrictStr] = Field(default=None, alias="publicIP")
    location: Optional[EndpointAgentLocation] = None
    clients: Optional[List[EndpointClient]] = Field(default=None, description="List of clients (user accounts) that the agent works with. Not populated by default. ")
    total_memory: Optional[StrictStr] = Field(default=None, alias="totalMemory")
    agent_type: Optional[StrictStr] = Field(default=None, alias="agentType")
    vpn_profiles: Optional[List[EndpointVpnProfile]] = Field(default=None, description="List of VPN connections on the agent. Not populated by default. ", alias="vpnProfiles")
    network_interface_profiles: Optional[List[InterfaceProfile]] = Field(default=None, description="List of network interfaces on the agent. Not populated by default. ", alias="networkInterfaceProfiles")
    asn_details: Optional[EndpointAsnDetails] = Field(default=None, alias="asnDetails")
    license_type: Optional[AgentLicenseType] = Field(default=None, alias="licenseType")
    tcp_driver_available: Optional[StrictBool] = Field(default=None, description="Status of TCP test support on the agent.", alias="tcpDriverAvailable")
    npcap_version: Optional[StrictStr] = Field(default=None, description="For Windows agents, the version of the NPCAP driver that the agent has loaded.", alias="npcapVersion")
    __properties: ClassVar[List[str]] = ["id", "aid", "name", "computerName", "osVersion", "platform", "kernelVersion", "manufacturer", "model", "lastSeen", "status", "deleted", "version", "createdAt", "numberOfClients", "publicIP", "location", "clients", "totalMemory", "agentType", "vpnProfiles", "networkInterfaceProfiles", "asnDetails", "licenseType", "tcpDriverAvailable", "npcapVersion"]

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
        """Create an instance of EndpointAgent from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "computer_name",
                "os_version",
                "kernel_version",
                "manufacturer",
                "model",
                "last_seen",
                "deleted",
                "version",
                "created_at",
                "number_of_clients",
                "public_ip",
                "clients",
                "total_memory",
                "agent_type",
                "vpn_profiles",
                "network_interface_profiles",
                "tcp_driver_available",
                "npcap_version",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of aid
        if self.aid:
            _dict['aid'] = self.aid.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in clients (list)
        _items = []
        if self.clients:
            for _item in self.clients:
                if _item:
                    _items.append(_item.to_dict())
            _dict['clients'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in vpn_profiles (list)
        _items = []
        if self.vpn_profiles:
            for _item in self.vpn_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['vpnProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in network_interface_profiles (list)
        _items = []
        if self.network_interface_profiles:
            for _item in self.network_interface_profiles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['networkInterfaceProfiles'] = _items
        # override the default output from pydantic by calling `to_dict()` of asn_details
        if self.asn_details:
            _dict['asnDetails'] = self.asn_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of EndpointAgent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "aid": EndpointAgentAid.from_dict(obj.get("aid")) if obj.get("aid") is not None else None,
            "name": obj.get("name"),
            "computerName": obj.get("computerName"),
            "osVersion": obj.get("osVersion"),
            "platform": obj.get("platform"),
            "kernelVersion": obj.get("kernelVersion"),
            "manufacturer": obj.get("manufacturer"),
            "model": obj.get("model"),
            "lastSeen": obj.get("lastSeen"),
            "status": obj.get("status"),
            "deleted": obj.get("deleted"),
            "version": obj.get("version"),
            "createdAt": obj.get("createdAt"),
            "numberOfClients": obj.get("numberOfClients"),
            "publicIP": obj.get("publicIP"),
            "location": EndpointAgentLocation.from_dict(obj.get("location")) if obj.get("location") is not None else None,
            "clients": [EndpointClient.from_dict(_item) for _item in obj.get("clients")] if obj.get("clients") is not None else None,
            "totalMemory": obj.get("totalMemory"),
            "agentType": obj.get("agentType"),
            "vpnProfiles": [EndpointVpnProfile.from_dict(_item) for _item in obj.get("vpnProfiles")] if obj.get("vpnProfiles") is not None else None,
            "networkInterfaceProfiles": [InterfaceProfile.from_dict(_item) for _item in obj.get("networkInterfaceProfiles")] if obj.get("networkInterfaceProfiles") is not None else None,
            "asnDetails": EndpointAsnDetails.from_dict(obj.get("asnDetails")) if obj.get("asnDetails") is not None else None,
            "licenseType": obj.get("licenseType"),
            "tcpDriverAvailable": obj.get("tcpDriverAvailable"),
            "npcapVersion": obj.get("npcapVersion")
        })
        return _obj


