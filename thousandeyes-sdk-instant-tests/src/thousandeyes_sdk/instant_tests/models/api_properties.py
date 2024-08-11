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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from thousandeyes_sdk.instant_tests.models.api_predefined_variable import ApiPredefinedVariable
from thousandeyes_sdk.instant_tests.models.api_request import ApiRequest
from thousandeyes_sdk.instant_tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.instant_tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.instant_tests.models.test_protocol import TestProtocol
from thousandeyes_sdk.instant_tests.models.test_ssl_version_id import TestSslVersionId
from typing import Optional, Set
from typing_extensions import Self

class ApiProperties(BaseModel):
    """
    ApiProperties
    """ # noqa: E501
    follow_redirects: Optional[StrictBool] = Field(default=True, description="To disable following HTTP/301 or HTTP/302 redirect directives, set this parameter to `false`.", alias="followRedirects")
    mtu_measurements: Optional[StrictBool] = Field(default=None, description="Set `true` to measure MTU sizes on network from agents to the target.", alias="mtuMeasurements")
    network_measurements: Optional[StrictBool] = Field(default=True, description="Enable or disable network measurements. Set to true to enable or false to disable network measurements.", alias="networkMeasurements")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=1)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    path_trace_mode: Optional[TestPathTraceMode] = Field(default=None, alias="pathTraceMode")
    predefined_variables: Optional[List[ApiPredefinedVariable]] = Field(default=None, alias="predefinedVariables")
    probe_mode: Optional[TestProbeMode] = Field(default=None, alias="probeMode")
    protocol: Optional[TestProtocol] = None
    requests: List[ApiRequest]
    ssl_version_id: Optional[TestSslVersionId] = Field(default=None, alias="sslVersionId")
    target_time: Optional[Annotated[int, Field(le=60, strict=True, ge=0)]] = Field(default=None, description="Target time for completion metric, defaults to 50% of time limit specified in seconds. (0 means default behavior)", alias="targetTime")
    time_limit: Optional[Annotated[int, Field(le=180, strict=True, ge=5)]] = Field(default=30, description="Time limit for transaction in seconds. Exceeding this limit will result in a Timeout error.", alias="timeLimit")
    url: StrictStr = Field(description="Target for the test.")
    type: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["followRedirects", "mtuMeasurements", "networkMeasurements", "numPathTraces", "pathTraceMode", "predefinedVariables", "probeMode", "protocol", "requests", "sslVersionId", "targetTime", "timeLimit", "url", "type"]

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
        """Create an instance of ApiProperties from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in predefined_variables (list)
        _items = []
        if self.predefined_variables:
            for _item in self.predefined_variables:
                if _item:
                    _items.append(_item.to_dict())
            _dict['predefinedVariables'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in requests (list)
        _items = []
        if self.requests:
            for _item in self.requests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['requests'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiProperties from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "followRedirects": obj.get("followRedirects") if obj.get("followRedirects") is not None else True,
            "mtuMeasurements": obj.get("mtuMeasurements"),
            "networkMeasurements": obj.get("networkMeasurements") if obj.get("networkMeasurements") is not None else True,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "pathTraceMode": obj.get("pathTraceMode"),
            "predefinedVariables": [ApiPredefinedVariable.from_dict(_item) for _item in obj["predefinedVariables"]] if obj.get("predefinedVariables") is not None else None,
            "probeMode": obj.get("probeMode"),
            "protocol": obj.get("protocol"),
            "requests": [ApiRequest.from_dict(_item) for _item in obj["requests"]] if obj.get("requests") is not None else None,
            "sslVersionId": obj.get("sslVersionId"),
            "targetTime": obj.get("targetTime"),
            "timeLimit": obj.get("timeLimit") if obj.get("timeLimit") is not None else 30,
            "url": obj.get("url"),
            "type": obj.get("type")
        })
        return _obj


