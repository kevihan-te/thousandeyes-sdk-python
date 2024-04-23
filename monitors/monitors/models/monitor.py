# coding: utf-8

"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from monitors.models.monitor_type import MonitorType
from typing import Optional, Set
from typing_extensions import Self

class Monitor(BaseModel):
    """
    Monitor
    """ # noqa: E501
    country_id: Optional[StrictStr] = Field(default=None, description="Country ID", alias="countryId")
    monitor_id: Optional[StrictStr] = Field(default=None, description="BGP monitor ID", alias="monitorId")
    ip_address: Optional[StrictStr] = Field(default=None, description="IP address of the BGP monitor", alias="ipAddress")
    network: Optional[StrictStr] = Field(default=None, description="Name of the autonomous system in which the monitor is found")
    monitor_type: Optional[MonitorType] = Field(default=None, alias="monitorType")
    monitor_name: Optional[StrictStr] = Field(default=None, description="Display name of the BGP monitor", alias="monitorName")
    __properties: ClassVar[List[str]] = ["countryId", "monitorId", "ipAddress", "network", "monitorType", "monitorName"]

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
        """Create an instance of Monitor from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "country_id",
            "monitor_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Monitor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "countryId": obj.get("countryId"),
            "monitorId": obj.get("monitorId"),
            "ipAddress": obj.get("ipAddress"),
            "network": obj.get("network"),
            "monitorType": obj.get("monitorType"),
            "monitorName": obj.get("monitorName")
        })
        return _obj


