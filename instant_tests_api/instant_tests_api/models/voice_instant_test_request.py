# coding: utf-8

"""
    Instant Tests API

     ### Overview The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test.

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
from instant_tests_api.models.instant_test_request_agents_inner import InstantTestRequestAgentsInner
from instant_tests_api.models.test_dscp_id import TestDscpId
from instant_tests_api.models.unexpanded_instant_test_links import UnexpandedInstantTestLinks
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class VoiceInstantTestRequest(BaseModel):
    """
    VoiceInstantTestRequest
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
    links: Optional[UnexpandedInstantTestLinks] = Field(default=None, alias="_links")
    labels: Optional[List[StrictStr]] = Field(default=None, description="A list of test label identifiers (get `labelId` from `/labels` endpoint).")
    shared_with_accounts: Optional[List[StrictStr]] = Field(default=None, description="A list of account group identifiers that the test is shared with (get `aid` from `/account-groups` endpoint).", alias="sharedWithAccounts")
    agents: List[InstantTestRequestAgentsInner] = Field(description="A list of objects with `agentId` (required) and `sourceIpAddress` (optional).")
    codec: Optional[StrictStr] = Field(default=None, description="Codec label")
    codec_id: Optional[StrictStr] = Field(default=None, description="Coded ID, [see the list of acceptable values](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/working-with-test-settings#rtp-stream-advanced-settings-tab)", alias="codecId")
    dscp: Optional[StrictStr] = Field(default=None, description="DSCP label.")
    dscp_id: Optional[TestDscpId] = Field(default=None, alias="dscpId")
    duration: Optional[Annotated[int, Field(le=30, strict=True, ge=5)]] = Field(default=5, description="Duration of the test in seconds.")
    jitter_buffer: Optional[Annotated[int, Field(le=150, strict=True, ge=0)]] = Field(default=40, description="De-jitter buffer size in seconds.", alias="jitterBuffer")
    num_path_traces: Optional[Annotated[int, Field(le=10, strict=True, ge=3)]] = Field(default=3, description="Number of path traces executed by the agent.", alias="numPathTraces")
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1024)]] = Field(default=None, description="Port number for the chosen protocol.")
    target_agent_id: StrictStr = Field(description="Agent ID of the target agent for the test.", alias="targetAgentId")
    __properties: ClassVar[List[str]] = ["createdBy", "createdDate", "description", "liveShare", "modifiedBy", "modifiedDate", "savedEvent", "testId", "testName", "type", "_links", "labels", "sharedWithAccounts", "agents", "codec", "codecId", "dscp", "dscpId", "duration", "jitterBuffer", "numPathTraces", "port", "targetAgentId"]

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
        """Create an instance of VoiceInstantTestRequest from a JSON string"""
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
                "codec",
                "dscp",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in agents (list)
        _items = []
        if self.agents:
            for _item in self.agents:
                if _item:
                    _items.append(_item.to_dict())
            _dict['agents'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of VoiceInstantTestRequest from a dict"""
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
            "_links": UnexpandedInstantTestLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "labels": obj.get("labels"),
            "sharedWithAccounts": obj.get("sharedWithAccounts"),
            "agents": [InstantTestRequestAgentsInner.from_dict(_item) for _item in obj.get("agents")] if obj.get("agents") is not None else None,
            "codec": obj.get("codec"),
            "codecId": obj.get("codecId"),
            "dscp": obj.get("dscp"),
            "dscpId": obj.get("dscpId"),
            "duration": obj.get("duration") if obj.get("duration") is not None else 5,
            "jitterBuffer": obj.get("jitterBuffer") if obj.get("jitterBuffer") is not None else 40,
            "numPathTraces": obj.get("numPathTraces") if obj.get("numPathTraces") is not None else 3,
            "port": obj.get("port"),
            "targetAgentId": obj.get("targetAgentId")
        })
        return _obj


