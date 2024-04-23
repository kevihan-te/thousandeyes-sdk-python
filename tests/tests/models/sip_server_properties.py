# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from tests.models.test_ipv6_policy import TestIpv6Policy
from tests.models.test_path_trace_mode import TestPathTraceMode
from tests.models.test_probe_mode import TestProbeMode
from typing import Optional, Set
from typing_extensions import Self

class SipServerProperties(BaseModel):
    """
    SipServerProperties
    """ # noqa: E501
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    options_regex: Optional[StrictStr] = Field(default=None, description="Options regex, this field does not require escaping.", alias="optionsRegex")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    register_enabled: Optional[StrictBool] = Field(default=False, description="Set to true to perform SIP registration on the test target with the SIP REGISTER command.", alias="registerEnabled")
    sip_target_time: Optional[Annotated[int, Field(le=5000, strict=True, ge=100)]] = Field(default=None, description="Target time for test completion in milliseconds.", alias="sipTargetTime")
    sip_time_limit: Optional[Annotated[int, Field(le=10, strict=True, ge=5)]] = Field(default=5, description="Time limit in milliseconds.", alias="sipTimeLimit")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["mtuMeasurements", "networkMeasurements", "numPathTraces", "optionsRegex", "pathTraceMode", "probeMode", "registerEnabled", "sipTargetTime", "sipTimeLimit", "fixedPacketRate", "ipv6Policy", "type"]

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
        """Create an instance of SipServerProperties from a JSON string"""
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
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SipServerProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "optionsRegex": obj.get("optionsRegex"),
            "pathTraceMode": obj.get("pathTraceMode"),
            "probeMode": obj.get("probeMode"),
            "registerEnabled": obj.get("registerEnabled") if obj.get("registerEnabled") is not None else False,
            "sipTargetTime": obj.get("sipTargetTime"),
            "sipTimeLimit": obj.get("sipTimeLimit") if obj.get("sipTimeLimit") is not None else 5,
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "type": obj.get("type")
        })
        return _obj


