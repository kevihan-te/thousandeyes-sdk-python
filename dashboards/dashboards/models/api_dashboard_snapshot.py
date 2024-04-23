# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from dashboards.models.api_dashboard import ApiDashboard
from dashboards.models.api_report_snapshot_time_span import ApiReportSnapshotTimeSpan
from dashboards.models.api_widget import ApiWidget
from dashboards.models.app_and_self_links_links import AppAndSelfLinksLinks
from typing import Optional, Set
from typing_extensions import Self

class ApiDashboardSnapshot(BaseModel):
    """
    ApiDashboardSnapshot
    """ # noqa: E501
    snapshot_id: Optional[StrictStr] = Field(default=None, description="Identifier of the dashboard snapshot.", alias="snapshotId")
    account_id: Optional[StrictInt] = Field(default=None, description="Identifier of the account group that the snapshot belongs to.", alias="accountId")
    created_date: Optional[StrictStr] = Field(default=None, description="UTC date when dashboard snapshot was created.", alias="createdDate")
    expiration_date: Optional[StrictStr] = Field(default=None, description="Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date.", alias="expirationDate")
    permalink: Optional[StrictStr] = Field(default=None, description="Hyperlink to dashboard snapshot in ThousandEyes Application")
    api_links: Optional[List[Dict[str, Any]]] = Field(default=None, description="A links array containing the self link.", alias="apiLinks")
    links: Optional[AppAndSelfLinksLinks] = Field(default=None, alias="_links")
    snapshot_name: Optional[StrictStr] = Field(default=None, description="Name of the dashboard snapshot.", alias="snapshotName")
    aid: Optional[StrictStr] = Field(default=None, description="Identifier of the account group that the snapshot belongs to.")
    is_shared: Optional[StrictBool] = Field(default=None, description="Set `true` if dashboard snapshot is shared, `false` otherwise.", alias="isShared")
    snapshot_created_date: Optional[datetime] = Field(default=None, description="UTC date when dashboard snapshot was created (ISO date-time format).", alias="snapshotCreatedDate")
    dashboard: Optional[ApiDashboard] = None
    widgets: Optional[List[ApiWidget]] = None
    is_scheduled: Optional[StrictBool] = Field(default=None, description="Set `true` if dashboard snapshot was generated from a schedule, `false` otherwise.", alias="isScheduled")
    time_span: Optional[ApiReportSnapshotTimeSpan] = Field(default=None, alias="timeSpan")
    snapshot_expiration_date: Optional[datetime] = Field(default=None, description="Expiration date of the snapshot. If unspecified, the snapshot expires 1 year from its creation date. The expiration date must be set within 5 years from the current date and adhere to the ISO date-time format.", alias="snapshotExpirationDate")
    __properties: ClassVar[List[str]] = ["snapshotId", "accountId", "createdDate", "expirationDate", "permalink", "apiLinks", "_links", "snapshotName", "aid", "isShared", "snapshotCreatedDate", "dashboard", "widgets", "isScheduled", "timeSpan", "snapshotExpirationDate"]

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
        """Create an instance of ApiDashboardSnapshot from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dashboard
        if self.dashboard:
            _dict['dashboard'] = self.dashboard.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in widgets (list)
        _items = []
        if self.widgets:
            for _item in self.widgets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['widgets'] = _items
        # override the default output from pydantic by calling `to_dict()` of time_span
        if self.time_span:
            _dict['timeSpan'] = self.time_span.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiDashboardSnapshot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "snapshotId": obj.get("snapshotId"),
            "accountId": obj.get("accountId"),
            "createdDate": obj.get("createdDate"),
            "expirationDate": obj.get("expirationDate"),
            "permalink": obj.get("permalink"),
            "apiLinks": obj.get("apiLinks"),
            "_links": AppAndSelfLinksLinks.from_dict(obj["_links"]) if obj.get("_links") is not None else None,
            "snapshotName": obj.get("snapshotName"),
            "aid": obj.get("aid"),
            "isShared": obj.get("isShared"),
            "snapshotCreatedDate": obj.get("snapshotCreatedDate"),
            "dashboard": ApiDashboard.from_dict(obj["dashboard"]) if obj.get("dashboard") is not None else None,
            "widgets": [ApiWidget.from_dict(_item) for _item in obj["widgets"]] if obj.get("widgets") is not None else None,
            "isScheduled": obj.get("isScheduled"),
            "timeSpan": ApiReportSnapshotTimeSpan.from_dict(obj["timeSpan"]) if obj.get("timeSpan") is not None else None,
            "snapshotExpirationDate": obj.get("snapshotExpirationDate")
        })
        return _obj


