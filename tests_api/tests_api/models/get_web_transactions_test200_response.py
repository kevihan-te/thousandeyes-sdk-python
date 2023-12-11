# coding: utf-8

"""
    Tests API

     ### Overview This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.

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
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from typing_extensions import Annotated
from tests_api.models.agent import Agent
from tests_api.models.alert_rule import AlertRule
from tests_api.models.monitor import Monitor
from tests_api.models.self_links_links import SelfLinksLinks
from tests_api.models.test_auth_type import TestAuthType
from tests_api.models.test_custom_headers import TestCustomHeaders
from tests_api.models.test_interval import TestInterval
from tests_api.models.test_labels_inner import TestLabelsInner
from tests_api.models.test_page_loading_strategy import TestPageLoadingStrategy
from tests_api.models.test_path_trace_mode import TestPathTraceMode
from tests_api.models.test_probe_mode import TestProbeMode
from tests_api.models.test_protocol import TestProtocol
from tests_api.models.test_shared_accounts_inner import TestSharedAccountsInner
from tests_api.models.test_ssl_version_id import TestSslVersionId
from tests_api.models.test_sub_interval import TestSubInterval
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetWebTransactionsTest200Response(BaseModel):
    """
    GetWebTransactionsTest200Response
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
    links: Optional[SelfLinksLinks] = Field(default=None, alias="_links")
    labels: Optional[List[TestLabelsInner]] = None
    shared_with_accounts: Optional[List[TestSharedAccountsInner]] = Field(default=None, alias="sharedWithAccounts")
    agents: List[Agent] = Field(description="Contains list of agents.")
    auth_type: Optional[TestAuthType] = Field(default=None, alias="authType")
    bandwidth_measurements: Optional[StrictBool] = Field(default=None, description="Set to `true` to enable bandwidth measurements, only applies to Enterprise agents assigned to the test.", alias="bandwidthMeasurements")
    client_certificate: Optional[StrictStr] = Field(default=None, description="String representation (containing newline characters) of client certificate, the private key must be placed first, then the certificate.", alias="clientCertificate")
    content_regex: Optional[StrictStr] = Field(default=None, description="Verify content using a regular expression. This field does not require escaping.", alias="contentRegex")
    credentials: Optional[List[StrictStr]] = Field(default=None, description="Contains a list of credential IDs (get `credentialId` from `/credentials` endpoint).")
    custom_headers: Optional[TestCustomHeaders] = Field(default=None, alias="customHeaders")
    desired_status_code: Optional[StrictStr] = Field(default='200', description="Specify the HTTP status code value that indicates a successful response.", alias="desiredStatusCode")
    follow_redirects: Optional[StrictBool] = Field(default=True, description="To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to false.", alias="followRedirects")
    http_target_time: Optional[Annotated[int, Field(le=5000, strict=True, ge=100)]] = Field(default=None, description="Target time for HTTP server completion, specified in milliseconds.", alias="httpTargetTime")
    http_time_limit: Optional[Annotated[int, Field(le=60, strict=True, ge=5)]] = Field(default=5, description="HTTP time limit in seconds.", alias="httpTimeLimit")
    http_version: Optional[Annotated[int, Field(le=2, strict=True, ge=1)]] = Field(default=2, description="HTTP protocol version. Set to '2' to prefer HTTP/2, or '1' to use only HTTP/1.1.", alias="httpVersion")
    include_headers: Optional[StrictBool] = Field(default=True, description="Set to `true` to capture response headers for objects loaded by the test.", alias="includeHeaders")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=3)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    password: Optional[StrictStr] = Field(default=None, description="Password for Basic/NTLM authentication.")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    ssl_version: Optional[StrictStr] = Field(default=None, description="Reflects the verbose SSL protocol version used by a test.", alias="sslVersion")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    target_time: Optional[Annotated[int, Field(le=60, strict=True, ge=1)]] = Field(default=None, description="Target time for completion, defaults to 50% of time limit specified in seconds.", alias="targetTime")
    time_limit: Optional[Annotated[int, Field(le=180, strict=True, ge=5)]] = Field(default=30, description="Time limit for transaction in seconds.", alias="timeLimit")
    transaction_script: StrictStr = Field(description="JavaScript of a web transaction test. Quotes must be escaped (precede \" characters with \\ ).", alias="transactionScript")
    url: StrictStr = Field(description="Target for the test.")
    use_ntlm: Optional[StrictBool] = Field(default=None, description="Set to true to use NTLM, false to use Basic Authentication. Requires username and password to be set.", alias="useNtlm")
    user_agent: Optional[StrictStr] = Field(default=None, description="User-agent string to be provided during the test.", alias="userAgent")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    verify_certificate: Optional[StrictBool] = Field(default=False, description="Ignore or acknowledge certificate errors. Set to false to ignore certificate errors.", alias="verifyCertificate")
    block_domains: Optional[StrictStr] = Field(default=None, description="Domains or full object URLs to be excluded from metrics and waterfall data for transaction tests.", alias="blockDomains")
    disable_screenshot: Optional[StrictBool] = Field(default=False, description="Enables or disables screenshots on error. Set true to not capture", alias="disableScreenshot")
    allow_mic_and_camera: Optional[StrictBool] = Field(default=False, description="Set true allow the use of a fake mic and camera in the browser.", alias="allowMicAndCamera")
    allow_geolocation: Optional[StrictBool] = Field(default=False, description="Set true to use the agent’s geolocation by the web page.", alias="allowGeolocation")
    browser_language: Optional[StrictStr] = Field(default=None, description="Set one of the available browser language that you want to use to configure the browser.", alias="browserLanguage")
    page_loading_strategy: Optional[TestPageLoadingStrategy] = Field(default=None, alias="pageLoadingStrategy")
    fixed_packet_rate: Optional[Annotated[int, Field(le=100, strict=True, ge=0)]] = Field(default=None, description="Sets packets rate sent to measure the network in packets per second.", alias="fixedPacketRate")
    bgp_measurements: Optional[StrictBool] = Field(default=True, description="Set to `true` to enable bgp measurements.", alias="bgpMeasurements")
    monitors: Optional[List[Monitor]] = Field(default=None, description="Contains list of enabled BGP monitors.")
    subinterval: Optional[TestSubInterval] = None
    __properties: ClassVar[List[str]] = ["interval", "alertsEnabled", "enabled", "alertRules", "createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "agents", "authType", "bandwidthMeasurements", "clientCertificate", "contentRegex", "credentials", "customHeaders", "desiredStatusCode", "followRedirects", "httpTargetTime", "httpTimeLimit", "httpVersion", "includeHeaders", "mtuMeasurements", "networkMeasurements", "numPathTraces", "password", "pathTraceMode", "probeMode", "protocol", "sslVersion", "sslVersionId", "targetTime", "timeLimit", "transactionScript", "url", "useNtlm", "userAgent", "username", "verifyCertificate", "blockDomains", "disableScreenshot", "allowMicAndCamera", "allowGeolocation", "browserLanguage", "pageLoadingStrategy", "fixedPacketRate", "bgpMeasurements", "monitors", "subinterval"]

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
        """Create an instance of GetWebTransactionsTest200Response from a JSON string"""
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
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
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
                "ssl_version",
                "monitors",
            },
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
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item in self.agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agents'] = _items
        # override the default output from pydantic by calling `to_dict()` of custom_headers
        if self.custom_headers:
            _dict['customHeaders'] = self.custom_headers.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in monitors (list)
        _items = []
        if self.monitors:
            for _item in self.monitors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['monitors'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetWebTransactionsTest200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "interval": obj.get("interval"),
            "alertsEnabled": obj.get("alertsEnabled"),
            "enabled": obj.get("enabled") if obj.get("enabled") is not None else True,
            "alertRules": [AlertRule.from_dict(_item) for _item in obj.get("alertRules")] if obj.get("alertRules") is not None else None,
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
            "_links": SelfLinksLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "labels": [TestLabelsInner.from_dict(_item) for _item in obj.get("labels")] if obj.get("labels") is not None else None,
            "sharedWithAccounts": [TestSharedAccountsInner.from_dict(_item) for _item in obj.get("sharedWithAccounts")] if obj.get("sharedWithAccounts") is not None else None,
            "agents": [Agent.from_dict(_item) for _item in obj.get("agents")] if obj.get("agents") is not None else None,
            "authType": obj.get("authType"),
            "bandwidthMeasurements": obj.get("bandwidthMeasurements"),
            "clientCertificate": obj.get("clientCertificate"),
            "contentRegex": obj.get("contentRegex"),
            "credentials": obj.get("credentials"),
            "customHeaders": TestCustomHeaders.from_dict(obj.get("customHeaders")) if obj.get("customHeaders") is not None else None,
            "desiredStatusCode": obj.get("desiredStatusCode") if obj.get("desiredStatusCode") is not None else '200',
            "followRedirects": obj.get("followRedirects") if obj.get("followRedirects") is not None else True,
            "httpTargetTime": obj.get("httpTargetTime"),
            "httpTimeLimit": obj.get("httpTimeLimit") if obj.get("httpTimeLimit") is not None else 5,
            "httpVersion": obj.get("httpVersion") if obj.get("httpVersion") is not None else 2,
            "includeHeaders": obj.get("includeHeaders") if obj.get("includeHeaders") is not None else True,
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "password": obj.get("password"),
            "pathTraceMode": obj.get("pathTraceMode"),
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "sslVersion": obj.get("sslVersion"),
            "sslVersionId": obj.get("sslVersionId"),
            "targetTime": obj.get("targetTime"),
            "timeLimit": obj.get("timeLimit") if obj.get("timeLimit") is not None else 30,
            "transactionScript": obj.get("transactionScript"),
            "url": obj.get("url"),
            "useNtlm": obj.get("useNtlm"),
            "userAgent": obj.get("userAgent"),
            "username": obj.get("username"),
            "verifyCertificate": obj.get("verifyCertificate") if obj.get("verifyCertificate") is not None else False,
            "blockDomains": obj.get("blockDomains"),
            "disableScreenshot": obj.get("disableScreenshot") if obj.get("disableScreenshot") is not None else False,
            "allowMicAndCamera": obj.get("allowMicAndCamera") if obj.get("allowMicAndCamera") is not None else False,
            "allowGeolocation": obj.get("allowGeolocation") if obj.get("allowGeolocation") is not None else False,
            "browserLanguage": obj.get("browserLanguage"),
            "pageLoadingStrategy": obj.get("pageLoadingStrategy"),
            "fixedPacketRate": obj.get("fixedPacketRate"),
            "bgpMeasurements": obj.get("bgpMeasurements") if obj.get("bgpMeasurements") is not None else True,
            "monitors": [Monitor.from_dict(_item) for _item in obj.get("monitors")] if obj.get("monitors") is not None else None,
            "subinterval": obj.get("subinterval")
        })
        return _obj


