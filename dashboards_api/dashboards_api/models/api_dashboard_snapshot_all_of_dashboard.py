# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

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
from dashboards_api.models.api_default_timespan import ApiDefaultTimespan
from dashboards_api.models.api_widget import ApiWidget
from dashboards_api.models.dashboard_links_links import DashboardLinksLinks
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiDashboardSnapshotAllOfDashboard(BaseModel):
    """
    ApiDashboardSnapshotAllOfDashboard
    """ # noqa: E501
    dashboard_id: Optional[StrictStr] = Field(default=None, description="Identifier of a dashboard.", alias="dashboardId")
    title: Optional[StrictStr] = Field(default=None, description="Title of a dashboard.")
    is_built_in: Optional[StrictBool] = Field(default=None, description="Indicates if a dashboard is built-in. True for built-in dashboards, false for user-created dashboards.", alias="isBuiltIn")
    aid: Optional[StrictStr] = Field(default=None, description="Identifier for the account group associated with a dashboard.")
    dashboard_created_by: Optional[StrictStr] = Field(default=None, description="Identifier for the user that created a dashboard.", alias="dashboardCreatedBy")
    dashboard_modified_by: Optional[StrictStr] = Field(default=None, description="Identifier for the user that last modified a dashboard.", alias="dashboardModifiedBy")
    dashboard_modified_date: Optional[datetime] = Field(default=None, description="UTC date/time when a dashboard was last modified (ISO date-time format).", alias="dashboardModifiedDate")
    is_private: Optional[StrictBool] = Field(default=None, description="A dashboard can be viewed by other users in the account. If true, only the creator of the dashboard may view it. If false, all users in the same account may view it.", alias="isPrivate")
    is_default_for_user: Optional[StrictBool] = Field(default=None, description="Indicates whether this dashboard is the user's default. True for default, false if not.", alias="isDefaultForUser")
    is_default_for_account: Optional[StrictBool] = Field(default=None, description="Indicates whether this dashboard is the account group's default. True for default, false if not.", alias="isDefaultForAccount")
    widgets: Optional[List[ApiWidget]] = None
    description: Optional[StrictStr] = Field(default=None, description="A text description of the dashboard's purpose and functionality. This information assists users in understanding the dashboard but isn't displayed when viewing a dashboard.")
    default_timespan: Optional[ApiDefaultTimespan] = Field(default=None, alias="defaultTimespan")
    is_global_override: Optional[StrictBool] = Field(default=None, description="When set to `true`, the defaultTimespan is used and overrides the widget's timespan. If set to `false`, the the widget's timespan is used.", alias="isGlobalOverride")
    is_migrated_report: Optional[StrictBool] = Field(default=None, description="True if this dashboard was previously a report.", alias="isMigratedReport")
    links: Optional[DashboardLinksLinks] = Field(default=None, alias="_links")
    __properties: ClassVar[List[str]] = ["dashboardId", "title", "isBuiltIn", "aid", "dashboardCreatedBy", "dashboardModifiedBy", "dashboardModifiedDate", "isPrivate", "isDefaultForUser", "isDefaultForAccount", "widgets", "description", "defaultTimespan", "isGlobalOverride", "isMigratedReport", "_links"]

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
        """Create an instance of ApiDashboardSnapshotAllOfDashboard from a JSON string"""
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "dashboard_id",
                "is_built_in",
                "aid",
                "dashboard_created_by",
                "dashboard_modified_by",
                "dashboard_modified_date",
                "is_default_for_user",
                "is_default_for_account",
                "is_migrated_report",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in widgets (list)
        _items = []
        if self.widgets:
            for _item in self.widgets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['widgets'] = _items
        # override the default output from pydantic by calling `to_dict()` of default_timespan
        if self.default_timespan:
            _dict['defaultTimespan'] = self.default_timespan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiDashboardSnapshotAllOfDashboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dashboardId": obj.get("dashboardId"),
            "title": obj.get("title"),
            "isBuiltIn": obj.get("isBuiltIn"),
            "aid": obj.get("aid"),
            "dashboardCreatedBy": obj.get("dashboardCreatedBy"),
            "dashboardModifiedBy": obj.get("dashboardModifiedBy"),
            "dashboardModifiedDate": obj.get("dashboardModifiedDate"),
            "isPrivate": obj.get("isPrivate"),
            "isDefaultForUser": obj.get("isDefaultForUser"),
            "isDefaultForAccount": obj.get("isDefaultForAccount"),
            "widgets": [ApiWidget.from_dict(_item) for _item in obj.get("widgets")] if obj.get("widgets") is not None else None,
            "description": obj.get("description"),
            "defaultTimespan": ApiDefaultTimespan.from_dict(obj.get("defaultTimespan")) if obj.get("defaultTimespan") is not None else None,
            "isGlobalOverride": obj.get("isGlobalOverride"),
            "isMigratedReport": obj.get("isMigratedReport"),
            "_links": DashboardLinksLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None
        })
        return _obj


