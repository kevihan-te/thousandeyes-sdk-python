# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.tests.models.agent_to_agent_test_protocol import AgentToAgentTestProtocol
from thousandeyes_sdk.tests.models.alert_rule import AlertRule
from thousandeyes_sdk.tests.models.monitor import Monitor
from thousandeyes_sdk.tests.models.shared_with_account import SharedWithAccount
from thousandeyes_sdk.tests.models.test_direction import TestDirection
from thousandeyes_sdk.tests.models.test_dscp_id import TestDscpId
from thousandeyes_sdk.tests.models.test_interval import TestInterval
from thousandeyes_sdk.tests.models.test_label import TestLabel
from thousandeyes_sdk.tests.models.test_links import TestLinks
from thousandeyes_sdk.tests.models.test_path_trace_mode import TestPathTraceMode
from typing import Optional, Set
from typing_extensions import Self

class AgentToAgentTest(BaseModel):
    """
    AgentToAgentTest
    """ # noqa: E501
    interval: TestInterval
    alerts_enabled: Optional[StrictBool] = Field(default=None, description="Indicates if alerts are enabled.", alias="alertsEnabled")
    enabled: Optional[StrictBool] = Field(default=True, description="Test is enabled.")
    alert_rules: Optional[List[AlertRule]] = Field(default=None, description="Contains list of enabled alert rule objects.", alias="alertRules")
    created_by: Optional[StrictStr] = Field(default=None, description="User that created the test.", alias="createdBy")
    created_date: Optional[datetime] = Field(default=None, description="UTC created date (ISO date-time format).", alias="createdDate")
    description: Optional[StrictStr] = Field(default=None, description="A description of the test.")
    live_share: Optional[StrictBool] = Field(default=None, description="Indicates if the test is shared with the account group.", alias="liveShare")
    modified_by: Optional[StrictStr] = Field(default=None, description="User that modified the test.", alias="modifiedBy")
    modified_date: Optional[datetime] = Field(default=None, description="UTC last modification date (ISO date-time format).", alias="modifiedDate")
    saved_event: Optional[StrictBool] = Field(default=None, description="Indicates if the test is a saved event.", alias="savedEvent")
    test_id: Optional[StrictStr] = Field(default=None, description="Each test is assigned an unique ID; this is used to access test information and results from other endpoints.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="The name of the test. Test name must be unique.", alias="testName")
    type: Optional[StrictStr] = None
    links: Optional[TestLinks] = Field(default=None, alias="_links")
    labels: Optional[List[TestLabel]] = None
    shared_with_accounts: Optional[List[SharedWithAccount]] = Field(default=None, alias="sharedWithAccounts")
    direction: Optional[TestDirection] = None
    dscp: Optional[StrictStr] = Field(default=None, description="DSCP label.")
    dscp_id: Optional[TestDscpId] = Field(default=None, alias="dscpId")
    mss: Optional[Annotated[int, Field(le=1400, strict=True, ge=20)]] = Field(default=None, description="Maximum segment size, in bytes.")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=49153, description="Target port.")
    protocol: Optional[AgentToAgentTestProtocol] = None
    randomized_start_time: Optional[StrictBool] = Field(default=False, description="Indicates whether agents should randomize the start time in each test round.", alias="randomizedStartTime")
    target_agent_id: StrictStr = Field(description="`agentId` of the target agent for the test.", alias="targetAgentId")
    throughput_measurements: Optional[StrictBool] = Field(default=False, description="Enable or disable throughput measurements. Throughput measurements cannot be enabled when the source or target of the test is a cloud agent.", alias="throughputMeasurements")
    throughput_duration: Optional[Annotated[int, Field(le=30000, strict=True, ge=5000)]] = Field(default=10000, description="The throughput duration.", alias="throughputDuration")
    throughput_rate: Optional[Annotated[int, Field(le=1000, strict=True, ge=8)]] = Field(default=None, description="The throughput rate, only applicable for UDP protocol.", alias="throughputRate")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    bgp_measurements: Optional[StrictBool] = Field(default=True, description="Set to `true` to enable bgp measurements.", alias="bgpMeasurements")
    use_public_bgp: Optional[StrictBool] = Field(default=True, description="Indicate if all available public BGP monitors should be used, when ommited defaults to `bgpMeasurements` value.", alias="usePublicBgp")
    monitors: Optional[List[Monitor]] = Field(default=None, description="Contains list of enabled BGP monitors.")
    __properties: ClassVar[List[str]] = ["interval", "alertsEnabled", "enabled", "alertRules", "createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "direction", "dscp", "dscpId", "mss", "numPathTraces", "pathTraceMode", "port", "protocol", "randomizedStartTime", "targetAgentId", "throughputMeasurements", "throughputDuration", "throughputRate", "fixedPacketRate", "bgpMeasurements", "usePublicBgp", "monitors"]

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
        """Create an instance of AgentToAgentTest from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created_by",
            "created_date",
            "live_share",
            "modified_by",
            "modified_date",
            "saved_event",
            "test_id",
            "type",
            "labels",
            "shared_with_accounts",
            "dscp",
            "monitors",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alert_rules (list)
        _items = []
        if self.alert_rules:
            for _item in self.alert_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alertRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in shared_with_accounts (list)
        _items = []
        if self.shared_with_accounts:
            for _item in self.shared_with_accounts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['sharedWithAccounts'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in monitors (list)
        _items = []
        if self.monitors:
            for _item in self.monitors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monitors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AgentToAgentTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "alertsEnabled": obj.get("alertsEnabled"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "alertRules": [AlertRule.from_dict(_item) for _item in obj["alertRules"]] if obj.get("alertRules") is not None else None,
            "createdBy": obj.get("createdBy"),
            "createdDate": obj.get("createdDate"),
            "description": obj.get("description"),
            "liveShare": obj.get("liveShare"),
            "modifiedBy": obj.get("modifiedBy"),
            "modifiedDate": obj.get("modifiedDate"),
            "savedEvent": obj.get("savedEvent"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "type": obj.get("type"),
            "_links": TestLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "labels": [TestLabel.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "sharedWithAccounts": [SharedWithAccount.from_dict(_item) for _item in obj["sharedWithAccounts"]] if obj.get("sharedWithAccounts") is not None else None,
            "direction": obj.get("direction"),
            "dscp": obj.get("dscp"),
            "dscpId": obj.get("dscpId"),
            "mss": obj.get("mss"),
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "port": obj.get("port") if obj.get("port") is not None else 49153,
            "protocol": obj.get("protocol"),
            "randomizedStartTime": obj.get("randomizedStartTime") if obj.get("randomizedStartTime") is not None else False,
            "targetAgentId": obj.get("targetAgentId"),
            "throughputMeasurements": obj.get("throughputMeasurements") if obj.get("throughputMeasurements") is not None else False,
            "throughputDuration": obj.get("throughputDuration") if obj.get("throughputDuration") is not None else 10000,
            "throughputRate": obj.get("throughputRate"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "bgpMeasurements": obj.get("bgpMeasurements") if obj.get("bgpMeasurements") is not None else True,
            "usePublicBgp": obj.get("usePublicBgp") if obj.get("usePublicBgp") is not None else True,
            "monitors": [Monitor.from_dict(_item) for _item in obj["monitors"]] if obj.get("monitors") is not None else None
        })
        return _obj


