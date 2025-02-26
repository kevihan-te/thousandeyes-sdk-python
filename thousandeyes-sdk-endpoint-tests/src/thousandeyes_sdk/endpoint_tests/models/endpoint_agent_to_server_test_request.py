# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_agent_selector_type import EndpointTestAgentSelectorType
from thousandeyes_sdk.endpoint_tests.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_tests.models.test_interval import TestInterval
from typing import Optional, Set
from typing_extensions import Self

class EndpointAgentToServerTestRequest(BaseModel):
    """
    EndpointAgentToServerTestRequest
    """ # noqa: E501
    agent_selector_type: Optional[EndpointTestAgentSelectorType] = Field(default=None, alias="agentSelectorType")
    agents: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent IDs (obtained from `/endpoint/agents` endpoint). Required when `agentSelectorType` is set to `specific-agent`.")
    endpoint_agent_labels: Optional[List[StrictStr]] = Field(default=None, description="List of endpoint agent label IDs (obtained from `/endpoint/labels` endpoint), required when `agentSelectorType` is set to `agent-labels`.", alias="endpointAgentLabels")
    max_machines: Optional[StrictInt] = Field(default=25, description="Maximum number of agents which can execute the test.", alias="maxMachines")
    test_name: StrictStr = Field(description="Name of the test.", alias="testName")
    server_name: StrictStr = Field(description="A server address without a protocol or IP address.", alias="serverName")
    port: Optional[StrictInt] = Field(default=443, description="Port number.")
    is_prioritized: Optional[StrictBool] = Field(default=False, description="Indicates whether the test should be prioritized when the number of tests assigned to an agent exceeds the license limit.", alias="isPrioritized")
    interval: Optional[TestInterval] = None
    protocol: Optional[EndpointTestProtocol] = None
    __properties: ClassVar[List[str]] = ["agentSelectorType", "agents", "endpointAgentLabels", "maxMachines", "testName", "serverName", "port", "isPrioritized", "interval", "protocol"]

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
        """Create an instance of EndpointAgentToServerTestRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointAgentToServerTestRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "agentSelectorType": obj.get("agentSelectorType"),
            "agents": obj.get("agents"),
            "endpointAgentLabels": obj.get("endpointAgentLabels"),
            "maxMachines": obj.get("maxMachines") if obj.get("maxMachines") is not None else 25,
            "testName": obj.get("testName"),
            "serverName": obj.get("serverName"),
            "port": obj.get("port") if obj.get("port") is not None else 443,
            "isPrioritized": obj.get("isPrioritized") if obj.get("isPrioritized") is not None else False,
            "interval": obj.get("interval"),
            "protocol": obj.get("protocol")
        })
        return _obj


