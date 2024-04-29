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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from endpoint_test_results.models.alert_rule import AlertRule
from endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from endpoint_test_results.models.endpoint_test_auth_type import EndpointTestAuthType
from endpoint_test_results.models.endpoint_test_links import EndpointTestLinks
from endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from endpoint_test_results.models.test_interval import TestInterval
from endpoint_test_results.models.test_labels_inner import TestLabelsInner
from endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from endpoint_test_results.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class EndpointHttpServerTest(BaseModel):
    """
    EndpointHttpServerTest
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="A unique identifier associated with your account group. You can retrieve your `AccountGroupId` from the `/account-groups` endpoint.")
    links: Optional[EndpointTestLinks] = Field(default=None, alias="_links")
    agent_selector_config: Optional[EndpointAgentSelectorConfig] = Field(default=None, alias="agentSelectorConfig")
    created_date: Optional[datetime] = Field(default=None, description="UTC created date (ISO date-time format).", alias="createdDate")
    interval: Optional[TestInterval] = None
    is_enabled: Optional[StrictBool] = Field(default=True, description="Indicates if test is enabled.", alias="isEnabled")
    is_saved_event: Optional[StrictBool] = Field(default=None, description="Indicates if the test is a saved event.", alias="isSavedEvent")
    has_path_trace_in_session: Optional[StrictBool] = Field(default=None, description="Enables \"in session\" path trace. When enabled, this option initiates a TCP session with the target server and sends path trace packets within the established TCP session.", alias="hasPathTraceInSession")
    modified_date: Optional[datetime] = Field(default=None, description="UTC last modification date (ISO date-time format).", alias="modifiedDate")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    port: Optional[StrictInt] = Field(default=None, description="Port number, if not specified, the port is selected based on a protocol (HTTP 80, HTTPS 443).")
    protocol: Optional[EndpointTestProtocol] = None
    server: Optional[StrictStr] = Field(default=None, description="Target domain name or IP address.")
    test_id: Optional[StrictStr] = Field(default=None, description="Each test is assigned a unique ID to access test data from other endpoints.", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="Name of the test.", alias="testName")
    type: Annotated[str, Field(strict=True)] = Field(description="Type of test being queried.")
    tcp_probe_mode: Optional[TestProbeModeResponse] = Field(default=None, alias="tcpProbeMode")
    alert_rules: Optional[List[AlertRule]] = Field(default=None, description="Contains list of enabled alert rule objects.", alias="alertRules")
    auth_type: Optional[EndpointTestAuthType] = Field(default=None, alias="authType")
    http_time_limit: Optional[StrictInt] = Field(default=None, description="Maximum amount of time in milliseconds the agents wait before a request times out.", alias="httpTimeLimit")
    url: Optional[StrictStr] = Field(default=None, description="Test target URL. Optionally, you can specify a protocol (http or https). If no protocol is provided, the default `https` protocol is used.")
    username: Optional[StrictStr] = Field(default=None, description="Username for Basic/NTLM authentication.")
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    verify_certificate: Optional[StrictBool] = Field(default=None, description="Flag indicating if a certificate should be verified.", alias="verifyCertificate")
    content_regex: Optional[StrictStr] = Field(default=None, description="Content regex, this field does not require escaping.", alias="contentRegex")
    follow_redirects: Optional[StrictBool] = Field(default=True, description="To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to false.", alias="followRedirects")
    http_target_time: Optional[Annotated[int, Field(le=5000, strict=True, ge=100)]] = Field(default=None, description="Target time for HTTP server completion, specified in milliseconds.", alias="httpTargetTime")
    http_version: Optional[Annotated[int, Field(le=2, strict=True, ge=1)]] = Field(default=2, description="HTTP protocol version. Set to '2' to prefer HTTP/2, or '1' to use only HTTP/1.1.", alias="httpVersion")
    post_body: Optional[StrictStr] = Field(default=None, description="Enter the body for the HTTP POST request in this field. No special escaping is necessary. If the post body is provided with content, the `requestMethod` is automatically set to POST.", alias="postBody")
    ssl_version: Optional[StrictStr] = Field(default=None, description="Reflects the verbose SSL protocol version used by a test.", alias="sslVersion")
    use_ntlm: Optional[StrictBool] = Field(default=None, description="Set to true to use NTLM, false to use Basic Authentication. Requires username and password to be set.", alias="useNtlm")
    user_agent: Optional[StrictStr] = Field(default=None, description="User-agent string to be provided during the test.", alias="userAgent")
    labels: Optional[List[TestLabelsInner]] = None
    __properties: ClassVar[List[str]] = ["aid", "_links", "agentSelectorConfig", "createdDate", "interval", "isEnabled", "isSavedEvent", "hasPathTraceInSession", "modifiedDate", "networkMeasurements", "port", "protocol", "server", "testId", "testName", "type", "tcpProbeMode", "alertRules", "authType", "httpTimeLimit", "url", "username", "sslVersionId", "verifyCertificate", "contentRegex", "followRedirects", "httpTargetTime", "httpVersion", "postBody", "sslVersion", "useNtlm", "userAgent", "labels"]

    @field_validator('type')
    def type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^http-server$", value):
            raise ValueError(r"must validate the regular expression /^http-server$/")
        return value

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
        """Create an instance of EndpointHttpServerTest from a JSON string"""
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
            "created_date",
            "is_saved_event",
            "modified_date",
            "test_id",
            "type",
            "ssl_version",
            "labels",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of agent_selector_config
        if self.agent_selector_config:
            _dict['agentSelectorConfig'] = self.agent_selector_config.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in alert_rules (list)
        _items = []
        if self.alert_rules:
            for _item in self.alert_rules:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alertRules'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item in self.labels:
                if _item:
                    _items.append(_item.to_dict())
            _dict['labels'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointHttpServerTest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "_links": EndpointTestLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "agentSelectorConfig": EndpointAgentSelectorConfig.from_dict(obj["agentSelectorConfig"]) if obj.get("agentSelectorConfig") is not None else None,
            "createdDate": obj.get("createdDate"),
            "interval": obj.get("interval"),
            "isEnabled": obj.get("isEnabled") if obj.get("isEnabled") is not None else True,
            "isSavedEvent": obj.get("isSavedEvent"),
            "hasPathTraceInSession": obj.get("hasPathTraceInSession"),
            "modifiedDate": obj.get("modifiedDate"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "port": obj.get("port"),
            "protocol": obj.get("protocol"),
            "server": obj.get("server"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "type": obj.get("type"),
            "tcpProbeMode": obj.get("tcpProbeMode"),
            "alertRules": [AlertRule.from_dict(_item) for _item in obj["alertRules"]] if obj.get("alertRules") is not None else None,
            "authType": obj.get("authType"),
            "httpTimeLimit": obj.get("httpTimeLimit"),
            "url": obj.get("url"),
            "username": obj.get("username"),
            "sslVersionId": obj.get("sslVersionId"),
            "verifyCertificate": obj.get("verifyCertificate"),
            "contentRegex": obj.get("contentRegex"),
            "followRedirects": obj.get("followRedirects") if obj.get("followRedirects") is not None else True,
            "httpTargetTime": obj.get("httpTargetTime"),
            "httpVersion": obj.get("httpVersion") if obj.get("httpVersion") is not None else 2,
            "postBody": obj.get("postBody"),
            "sslVersion": obj.get("sslVersion"),
            "useNtlm": obj.get("useNtlm"),
            "userAgent": obj.get("userAgent"),
            "labels": [TestLabelsInner.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None
        })
        return _obj


