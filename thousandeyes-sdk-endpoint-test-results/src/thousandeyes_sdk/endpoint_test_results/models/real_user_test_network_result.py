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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_test_results.models.network_metrics import NetworkMetrics
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from typing import Optional, Set
from typing_extensions import Self

class RealUserTestNetworkResult(BaseModel):
    """
    RealUserTestNetworkResult
    """ # noqa: E501
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of endpoint agent, from `/endpoint/agents` endpoint.", alias="agentId")
    var_date: Optional[datetime] = Field(default=None, description="UTC date when endpoint real user test took place (ISO date-time format).", alias="date")
    id: Optional[StrictStr] = Field(default=None, description="Endpoint real user test ID. Each endpoint real user test occurrence has a unique ID.")
    round_id: Optional[StrictInt] = Field(default=None, description="Epoch time (seconds) indicating the start time of the round.", alias="roundId")
    destination: Optional[NetworkMetrics] = None
    vpn: Optional[NetworkMetrics] = None
    proxy: Optional[NetworkMetrics] = None
    system_metrics: Optional[SystemMetrics] = Field(default=None, alias="systemMetrics")
    __properties: ClassVar[List[str]] = ["agentId", "date", "id", "roundId", "destination", "vpn", "proxy", "systemMetrics"]

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
        """Create an instance of RealUserTestNetworkResult from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "agent_id",
            "var_date",
            "id",
            "round_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of destination
        if self.destination:
            _dict['destination'] = self.destination.to_dict()
        # override the default output from pydantic by calling `to_dict()` of vpn
        if self.vpn:
            _dict['vpn'] = self.vpn.to_dict()
        # override the default output from pydantic by calling `to_dict()` of proxy
        if self.proxy:
            _dict['proxy'] = self.proxy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system_metrics
        if self.system_metrics:
            _dict['systemMetrics'] = self.system_metrics.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RealUserTestNetworkResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentId": obj.get("agentId"),
            "date": obj.get("date"),
            "id": obj.get("id"),
            "roundId": obj.get("roundId"),
            "destination": NetworkMetrics.from_dict(obj["destination"]) if obj.get("destination") is not None else None,
            "vpn": NetworkMetrics.from_dict(obj["vpn"]) if obj.get("vpn") is not None else None,
            "proxy": NetworkMetrics.from_dict(obj["proxy"]) if obj.get("proxy") is not None else None,
            "systemMetrics": SystemMetrics.from_dict(obj["systemMetrics"]) if obj.get("systemMetrics") is not None else None
        })
        return _obj


