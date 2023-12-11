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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictStr
from pydantic import Field
from dashboards_api.models.api_duration import ApiDuration
from dashboards_api.models.api_numbers_card import ApiNumbersCard
from dashboards_api.models.api_widget_measure import ApiWidgetMeasure
from dashboards_api.models.dashboard_metric import DashboardMetric
from dashboards_api.models.dashboard_metric_direction import DashboardMetricDirection
from dashboards_api.models.metric_group import MetricGroup
from dashboards_api.models.numbers_card_datasource import NumbersCardDatasource
from dashboards_api.models.self_links_links import SelfLinksLinks
from dashboards_api.models.visual_mode import VisualMode
from dashboards_api.models.widget_type import WidgetType
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiNumbersCardWidget(BaseModel):
    """
    A widget composed of multiple cards, each presenting a singular metric, such as average packet loss, page load time, or alert count.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the widget.")
    type: Optional[WidgetType] = None
    title: Optional[StrictStr] = Field(default=None, description="Title of the widget")
    visual_mode: Optional[VisualMode] = Field(default=None, alias="visualMode")
    embed_url: Optional[StrictStr] = Field(default=None, description="When `isEmbedded` is set to `true`, an `embedUrl` is provided.", alias="embedUrl")
    is_embedded: Optional[StrictBool] = Field(default=None, description="Set to `true` if widget is marked as embedded; otherwise, set to `false`.", alias="isEmbedded")
    metric_group: Optional[MetricGroup] = Field(default=None, alias="metricGroup")
    direction: Optional[DashboardMetricDirection] = None
    metric: Optional[DashboardMetric] = None
    filters: Optional[Dict[str, List[Union[str, Any]]]] = Field(default=None, description="(Optional) Specifies the filters applied to the widget. When present, the `filters` property displays. Each filter object has two properties: `filterProperty` and `filterValue`. The `filterProperty` can be values like Agents, Agent Groups, Tests, Monitors, etc. The `filterValue` represents theIdentifierof the selected property.")
    measure: Optional[ApiWidgetMeasure] = None
    fixed_timespan: Optional[ApiDuration] = Field(default=None, alias="fixedTimespan")
    api_link: Optional[StrictStr] = Field(default=None, alias="apiLink")
    should_exclude_alert_suppression_windows: Optional[StrictBool] = Field(default=None, description="Excludes alert suppression window data if set to `true`.", alias="shouldExcludeAlertSuppressionWindows")
    links: Optional[SelfLinksLinks] = Field(default=None, alias="_links")
    number_cards: Optional[List[ApiNumbersCard]] = Field(default=None, alias="numberCards")
    data_source: Optional[NumbersCardDatasource] = Field(default=None, alias="dataSource")
    __properties: ClassVar[List[str]] = ["id", "type", "title", "visualMode", "embedUrl", "isEmbedded", "metricGroup", "direction", "metric", "filters", "measure", "fixedTimespan", "apiLink", "shouldExcludeAlertSuppressionWindows", "_links", "numberCards", "dataSource"]

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
        """Create an instance of ApiNumbersCardWidget from a JSON string"""
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "embed_url",
                "api_link",
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of measure
        if self.measure:
            _dict['measure'] = self.measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_timespan
        if self.fixed_timespan:
            _dict['fixedTimespan'] = self.fixed_timespan.to_dict()
        # override the default output from pydantic by calling `to_dict()` of links
        if self.links:
            _dict['_links'] = self.links.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in number_cards (list)
        _items = []
        if self.number_cards:
            for _item in self.number_cards:
                if _item:
                    _items.append(_item.to_dict())
            _dict['numberCards'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiNumbersCardWidget from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "type": obj.get("type"),
            "title": obj.get("title"),
            "visualMode": obj.get("visualMode"),
            "embedUrl": obj.get("embedUrl"),
            "isEmbedded": obj.get("isEmbedded"),
            "metricGroup": obj.get("metricGroup"),
            "direction": obj.get("direction"),
            "metric": obj.get("metric"),
            "filters": obj.get("filters"),
            "measure": ApiWidgetMeasure.from_dict(obj.get("measure")) if obj.get("measure") is not None else None,
            "fixedTimespan": ApiDuration.from_dict(obj.get("fixedTimespan")) if obj.get("fixedTimespan") is not None else None,
            "apiLink": obj.get("apiLink"),
            "shouldExcludeAlertSuppressionWindows": obj.get("shouldExcludeAlertSuppressionWindows"),
            "_links": SelfLinksLinks.from_dict(obj.get("_links")) if obj.get("_links") is not None else None,
            "numberCards": [ApiNumbersCard.from_dict(_item) for _item in obj.get("numberCards")] if obj.get("numberCards") is not None else None,
            "dataSource": obj.get("dataSource")
        })
        return _obj


