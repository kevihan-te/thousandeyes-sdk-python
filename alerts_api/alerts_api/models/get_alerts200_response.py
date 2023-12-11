# coding: utf-8

"""
    Alerts API

     ## Overview Manage all alerts, alert rules and alert suppression windows.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel
from pydantic import Field
from alerts_api.models.alert import Alert
from alerts_api.models.pagination_links_links import PaginationLinksLinks
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class GetAlerts200Response(BaseModel):
    """
    GetAlerts200Response
    """ # noqa: E501
    alerts: Optional[List[Alert]] = None
    links: Optional[PaginationLinksLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["alerts", "_links"]

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
        """Create an instance of GetAlerts200Response from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in alerts (list)
        _items = []
        if self.alerts:
            for _item in self.alerts:
                if _item:
                    _items.append(_item.to_dict())
            _dict['alerts'] = _items
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of GetAlerts200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alerts": [Alert.from_dict(_item) for _item in obj.get("alerts")] if obj.get("alerts") is not None else None,
            "_links": PaginationLinksLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None
        })
        return _obj


