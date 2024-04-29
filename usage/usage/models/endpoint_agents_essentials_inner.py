# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class EndpointAgentsEssentialsInner(BaseModel):
    """
    EndpointAgentsEssentialsInner
    """ # noqa: E501
    aid: Optional[Any] = Field(default=None, description="Unique identifier of the account group owning the endpoint agents essentials.")
    account_group_name: Optional[Any] = Field(default=None, description="Name of the account group which owns the endpoint agents essentials.", alias="accountGroupName")
    endpoint_agents_essentials_used: Optional[StrictInt] = Field(default=None, description="Number of endpoint agents essentials owned by the specific account group in the usage period.", alias="endpointAgentsEssentialsUsed")
    __properties: ClassVar[List[str]] = ["aid", "accountGroupName", "endpointAgentsEssentialsUsed"]

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
        """Create an instance of EndpointAgentsEssentialsInner from a JSON string"""
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
        # set to None if aid (nullable) is None
        # and model_fields_set contains the field
        if self.aid is None and "aid" in self.model_fields_set:
            _dict['aid'] = None

        # set to None if account_group_name (nullable) is None
        # and model_fields_set contains the field
        if self.account_group_name is None and "account_group_name" in self.model_fields_set:
            _dict['accountGroupName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of EndpointAgentsEssentialsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "accountGroupName": obj.get("accountGroupName"),
            "endpointAgentsEssentialsUsed": obj.get("endpointAgentsEssentialsUsed")
        })
        return _obj


