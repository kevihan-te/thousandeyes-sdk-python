# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from agents.models.labels import Labels
from agents.models.self_links_links import SelfLinksLinks
from agents.models.simple_test import SimpleTest
from typing import Optional, Set
from typing_extensions import Self

class CloudAgentDetail(BaseModel):
    """
    CloudAgentDetail
    """ # noqa: E501
    ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of private IP addresses.", alias="ipAddresses")
    public_ip_addresses: Optional[List[StrictStr]] = Field(default=None, description="Array of public IP addresses.", alias="publicIpAddresses")
    network: Optional[StrictStr] = Field(default=None, description="Network (including ASN) of agent’s public IP.")
    agent_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the agent.", alias="agentId")
    agent_name: Optional[StrictStr] = Field(default=None, description="Name of the agent.", alias="agentName")
    location: Optional[StrictStr] = Field(default=None, description="Location of the agent.")
    country_id: Optional[StrictStr] = Field(default=None, description="2-digit ISO country code", alias="countryId")
    enabled: Optional[StrictBool] = Field(default=None, description="Flag indicating if the agent is enabled.")
    prefix: Optional[StrictStr] = Field(default=None, description="Prefix containing agents public IP address.")
    verify_ssl_certificates: Optional[StrictBool] = Field(default=None, description="Flag indicating if has normal SSL operations or  if instead it's set to ignore SSL errors on browserbot-based tests.", alias="verifySslCertificates")
    links: Optional[SelfLinksLinks] = Field(default=None, alias="_links")
    agent_type: Annotated[str, Field(strict=True)] = Field(description="Cloud agent type.", alias="agentType")
    tests: Optional[List[SimpleTest]] = Field(default=None, description="List of tests. See `/tests` for more information.")
    labels: Optional[List[Labels]] = Field(default=None, description="List of labels - see `/labels` for more information.")
    __properties: ClassVar[List[str]] = ["ipAddresses", "publicIpAddresses", "network", "agentId", "agentName", "location", "countryId", "enabled", "prefix", "verifySslCertificates", "_links", "agentType", "tests", "labels"]

    @field_validator('agent_type')
    def agent_type_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^cloud$", value):
            raise ValueError(r"must validate the regular expression /^cloud$/")
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
        """Create an instance of CloudAgentDetail from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "ip_addresses",
            "public_ip_addresses",
            "network",
            "agent_id",
            "location",
            "country_id",
            "prefix",
            "verify_ssl_certificates",
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
        # override the default output from pydantic by calling `to_dict()` of each item in tests (list)
        _items = []
        if self.tests:
            for _item in self.tests:
                if _item:
                    _items.append(_item.to_dict())
            _dict['tests'] = _items
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
        """Create an instance of CloudAgentDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipAddresses": obj.get("ipAddresses"),
            "publicIpAddresses": obj.get("publicIpAddresses"),
            "network": obj.get("network"),
            "agentId": obj.get("agentId"),
            "agentName": obj.get("agentName"),
            "location": obj.get("location"),
            "countryId": obj.get("countryId"),
            "enabled": obj.get("enabled"),
            "prefix": obj.get("prefix"),
            "verifySslCertificates": obj.get("verifySslCertificates"),
            "_links": SelfLinksLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "agentType": obj.get("agentType"),
            "tests": [SimpleTest.from_dict(_item) for _item in obj["tests"]] if obj.get("tests") is not None else None,
            "labels": [Labels.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None
        })
        return _obj


