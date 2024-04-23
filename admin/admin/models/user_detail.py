# coding: utf-8

"""
    Administrative API

    ## Overview Manage users, accounts, and account groups in the ThousandEyes platform using the Administrative API. This API provides the following endpoints that define the operations to manage your organization:     * `/account-groups`: Account groups are used to divide an organization into different sections. These endpoints can be used to create, retrieve, update and delete account groups.   * `/users`: Create, retrieve, update and delete users within an organization.    * `/roles`: Create, retrieve and update roles for the current user.    * `/permissions`: Retrieve all assignable permissions. Used in the context of modifying roles.    * `/audit-user-events`: Retrieve all activity log events.    For more information about the administrative models, see [Account Management](https://docs.thousandeyes.com/product-documentation/user-management).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from admin.models.account_group1 import AccountGroup1
from admin.models.account_group_roles_account_group_roles_inner import AccountGroupRolesAccountGroupRolesInner
from admin.models.role import Role
from typing import Optional, Set
from typing_extensions import Self

class UserDetail(BaseModel):
    """
    UserDetail
    """ # noqa: E501
    name: Optional[StrictStr] = Field(default=None, description="User's display name.")
    email: Optional[StrictStr] = Field(default=None, description="User's email address.")
    uid: Optional[StrictStr] = Field(default=None, description="Unique ID of the user.")
    date_registered: Optional[datetime] = Field(default=None, description="UTC date the user registered their account (ISO date-time format).", alias="dateRegistered")
    login_account_group: Optional[AccountGroup1] = Field(default=None, alias="loginAccountGroup")
    last_login: Optional[datetime] = Field(default=None, description="UTC last login of the user (ISO date-time format).", alias="lastLogin")
    account_group_roles: Optional[List[AccountGroupRolesAccountGroupRolesInner]] = Field(default=None, alias="accountGroupRoles")
    all_account_group_roles: Optional[List[Role]] = Field(default=None, alias="allAccountGroupRoles")
    __properties: ClassVar[List[str]] = ["name", "email", "uid", "dateRegistered", "loginAccountGroup", "lastLogin", "accountGroupRoles", "allAccountGroupRoles"]

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
        """Create an instance of UserDetail from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of login_account_group
        if self.login_account_group:
            _dict['loginAccountGroup'] = self.login_account_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in account_group_roles (list)
        _items = []
        if self.account_group_roles:
            for _item in self.account_group_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['accountGroupRoles'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in all_account_group_roles (list)
        _items = []
        if self.all_account_group_roles:
            for _item in self.all_account_group_roles:
                if _item:
                    _items.append(_item.to_dict())
            _dict['allAccountGroupRoles'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "uid": obj.get("uid"),
            "dateRegistered": obj.get("dateRegistered"),
            "loginAccountGroup": AccountGroup1.from_dict(obj["loginAccountGroup"]) if obj.get("loginAccountGroup") is not None else None,
            "lastLogin": obj.get("lastLogin"),
            "accountGroupRoles": [AccountGroupRolesAccountGroupRolesInner.from_dict(_item) for _item in obj["accountGroupRoles"]] if obj.get("accountGroupRoles") is not None else None,
            "allAccountGroupRoles": [Role.from_dict(_item) for _item in obj["allAccountGroupRoles"]] if obj.get("allAccountGroupRoles") is not None else None
        })
        return _obj


