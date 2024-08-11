# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

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
from typing_extensions import Annotated
from thousandeyes_sdk.instant_tests.models.agent import Agent
from thousandeyes_sdk.instant_tests.models.ftp_server_request_type import FtpServerRequestType
from thousandeyes_sdk.instant_tests.models.shared_with_account import SharedWithAccount
from thousandeyes_sdk.instant_tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.instant_tests.models.test_label import TestLabel
from thousandeyes_sdk.instant_tests.models.test_links import TestLinks
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.instant_tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.instant_tests.models.test_protocol import TestProtocol
from typing import Optional, Set
from typing_extensions import Self

class FtpServerInstantTest(BaseModel):
    """
    FtpServerInstantTest
    """ # noqa: E501
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
    bandwidth_measurements: Optional[StrictBool] = Field(default=None, description="Set to `true` to enable bandwidth measurements, only applies to Enterprise agents assigned to the test.", alias="bandwidthMeasurements")
    download_limit: Optional[StrictInt] = Field(default=None, description="Specify maximum number of bytes to download from the target object.", alias="downloadLimit")
    ftp_target_time: Optional[Annotated[int, Field(le=6000, strict=True, ge=1000)]] = Field(default=None, description="Target time for operation completion; specified in milliseconds.", alias="ftpTargetTime")
    ftp_time_limit: Optional[Annotated[int, Field(le=60, strict=True, ge=10)]] = Field(default=10, description="Set the time limit for the test in seconds.", alias="ftpTimeLimit")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    password: StrictStr = Field(description="Password for Basic/NTLM authentication.")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    request_type: FtpServerRequestType = Field(alias="requestType")
    url: StrictStr = Field(description="Target for the test.")
    use_active_ftp: Optional[StrictBool] = Field(default=False, description="Explicitly set the flag to use active FTP.", alias="useActiveFtp")
    use_explicit_ftps: Optional[StrictBool] = Field(default=None, description="Use explicit FTPS (ftp over SSL). By default, tests will autodetect when it is appropriate to use FTPS.", alias="useExplicitFtps")
    username: StrictStr = Field(description="Username for Basic/NTLM authentication.")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    ipv6_policy: Optional[TestIpv6Policy] = Field(default=None, alias="ipv6Policy")
    agents: Optional[List[Agent]] = Field(default=None, description="Contains list of agents.")
    __properties: ClassVar[List[str]] = ["createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "bandwidthMeasurements", "downloadLimit", "ftpTargetTime", "ftpTimeLimit", "mtuMeasurements", "networkMeasurements", "numPathTraces", "password", "pathTraceMode", "probeMode", "protocol", "requestType", "url", "useActiveFtp", "useExplicitFtps", "username", "fixedPacketRate", "ipv6Policy", "agents"]

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
        """Create an instance of FtpServerInstantTest from a JSON string"""
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
            "agents",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item in self.agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FtpServerInstantTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
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
            "bandwidthMeasurements": obj.get("bandwidthMeasurements"),
            "downloadLimit": obj.get("downloadLimit"),
            "ftpTargetTime": obj.get("ftpTargetTime"),
            "ftpTimeLimit": obj.get("ftpTimeLimit") if obj.get("ftpTimeLimit") is not None else 10,
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "password": obj.get("password"),
            "pathTraceMode": obj.get("pathTraceMode"),
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "requestType": obj.get("requestType"),
            "url": obj.get("url"),
            "useActiveFtp": obj.get("useActiveFtp") if obj.get("useActiveFtp") is not None else False,
            "useExplicitFtps": obj.get("useExplicitFtps"),
            "username": obj.get("username"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "ipv6Policy": obj.get("ipv6Policy"),
            "agents": [Agent.from_dict(_item) for _item in obj["agents"]] if obj.get("agents") is not None else None
        })
        return _obj


