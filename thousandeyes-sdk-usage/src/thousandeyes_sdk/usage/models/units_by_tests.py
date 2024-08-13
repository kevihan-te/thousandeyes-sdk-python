# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View organization usage` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View organization usage` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UnitsByTests(BaseModel):
    """
    UnitsByTests
    """ # noqa: E501
    aid: Optional[StrictStr] = Field(default=None, description="Unique ID of the account group owning the test that is generating units")
    account_group_name: Optional[StrictStr] = Field(default=None, description="Name of the account group which owns the test that is generating the units", alias="accountGroupName")
    enterprise_units_used: Optional[StrictInt] = Field(default=None, description="Units generated by the by the enterprise agents running the test", alias="enterpriseUnitsUsed")
    enterprise_units_projected: Optional[StrictInt] = Field(default=None, description="Enterprise Units projected in the current usage period, based on units consumed to date and configuration of the test", alias="enterpriseUnitsProjected")
    cloud_units_used: Optional[StrictInt] = Field(default=None, description="Units generated by the by the cloud agents running the test", alias="cloudUnitsUsed")
    cloud_units_projected: Optional[StrictInt] = Field(default=None, description="Cloud Units projected in the current usage period, based on units consumed to date and configuration of the test", alias="cloudUnitsProjected")
    test_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the test generating usage", alias="testId")
    test_name: Optional[StrictStr] = Field(default=None, description="Name of the test generating usage", alias="testName")
    test_type: Optional[StrictStr] = Field(default=None, description="Type of test generating usage. Note that this is a friendly testType entry (so it shouldn’t be parsed to discover the correct endpoint to query for configuration details).", alias="testType")
    is_instant_test: Optional[StrictBool] = Field(default=None, description="Indicates whether the test is scheduled or instant", alias="isInstantTest")
    __properties: ClassVar[List[str]] = ["aid", "accountGroupName", "enterpriseUnitsUsed", "enterpriseUnitsProjected", "cloudUnitsUsed", "cloudUnitsProjected", "testId", "testName", "testType", "isInstantTest"]

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
        """Create an instance of UnitsByTests from a JSON string"""
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
        """Create an instance of UnitsByTests from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aid": obj.get("aid"),
            "accountGroupName": obj.get("accountGroupName"),
            "enterpriseUnitsUsed": obj.get("enterpriseUnitsUsed"),
            "enterpriseUnitsProjected": obj.get("enterpriseUnitsProjected"),
            "cloudUnitsUsed": obj.get("cloudUnitsUsed"),
            "cloudUnitsProjected": obj.get("cloudUnitsProjected"),
            "testId": obj.get("testId"),
            "testName": obj.get("testName"),
            "testType": obj.get("testType"),
            "isInstantTest": obj.get("isInstantTest")
        })
        return _obj


