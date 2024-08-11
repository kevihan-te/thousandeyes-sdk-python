# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from thousandeyes_sdk.endpoint_labels.models.validation_error_item import ValidationErrorItem
from typing import Optional, Set
from typing_extensions import Self

class ValidationError(BaseModel):
    """
    ValidationError
    """ # noqa: E501
    type: Optional[StrictStr] = Field(default=None, description="A URI reference that identifies the problem type. When this member is not present, its value is assumed to be \"about:blank\".")
    title: Optional[StrictStr] = Field(default=None, description="A short, human-readable summary of the problem type.")
    status: Optional[StrictInt] = Field(default=None, description="The HTTP status code generated by the origin server for this occurrence of the problem.")
    detail: Optional[StrictStr] = Field(default=None, description="A human-readable explanation specific to this occurrence of the problem.")
    instance: Optional[StrictStr] = Field(default=None, description="A URI reference that identifies the specific occurrence of the problem.")
    errors: Optional[List[ValidationErrorItem]] = Field(default=None, description="(Optional) When multiple errors occur, the details for each error are listed.")
    __properties: ClassVar[List[str]] = ["type", "title", "status", "detail", "instance", "errors"]

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
        """Create an instance of ValidationError from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in errors (list)
        _items = []
        if self.errors:
            for _item in self.errors:
                if _item:
                    _items.append(_item.to_dict())
            _dict['errors'] = _items
        # set to None if errors (nullable) is None
        # and model_fields_set contains the field
        if self.errors is None and "errors" in self.model_fields_set:
            _dict['errors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "title": obj.get("title"),
            "status": obj.get("status"),
            "detail": obj.get("detail"),
            "instance": obj.get("instance"),
            "errors": [ValidationErrorItem.from_dict(_item) for _item in obj["errors"]] if obj.get("errors") is not None else None
        })
        return _obj


