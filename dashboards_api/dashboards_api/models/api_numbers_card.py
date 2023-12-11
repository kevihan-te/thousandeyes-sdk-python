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
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from dashboards_api.models.api_numbers_card_all_of_fixed_timespan import ApiNumbersCardAllOfFixedTimespan
from dashboards_api.models.api_widget_fixed_y_scale_prefix import ApiWidgetFixedYScalePrefix
from dashboards_api.models.api_widget_measure import ApiWidgetMeasure
from dashboards_api.models.dashboard_metric import DashboardMetric
from dashboards_api.models.dashboard_metric_direction import DashboardMetricDirection
from dashboards_api.models.metric_group import MetricGroup
from dashboards_api.models.numbers_card_datasource import NumbersCardDatasource
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class ApiNumbersCard(BaseModel):
    """
    An individual number card within the numbers card widget.
    """ # noqa: E501
    min_scale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Mininum scale configured in the widget.", alias="minScale")
    max_scale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Maximum scale configured in the widget.", alias="maxScale")
    unit: Optional[ApiWidgetFixedYScalePrefix] = None
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the widget.")
    description: Optional[StrictStr] = Field(default=None, description="Description of the number card.")
    measure: Optional[ApiWidgetMeasure] = None
    compare_to_previous_value: Optional[StrictBool] = Field(default=None, alias="compareToPreviousValue")
    fixed_timespan: Optional[ApiNumbersCardAllOfFixedTimespan] = Field(default=None, alias="fixedTimespan")
    should_exclude_alert_suppression_windows: Optional[StrictBool] = Field(default=None, description="Excludes alert suppression windows from the widget when set to `true`.", alias="shouldExcludeAlertSuppressionWindows")
    data_source: Optional[NumbersCardDatasource] = Field(default=None, alias="dataSource")
    metric_group: Optional[MetricGroup] = Field(default=None, alias="metricGroup")
    direction: Optional[DashboardMetricDirection] = None
    metric: Optional[DashboardMetric] = None
    filters: Optional[Dict[str, List[Union[str, Any]]]] = Field(default=None, description="Filters to apply to the widget.")
    __properties: ClassVar[List[str]] = ["minScale", "maxScale", "unit", "id", "description", "measure", "compareToPreviousValue", "fixedTimespan", "shouldExcludeAlertSuppressionWindows", "dataSource", "metricGroup", "direction", "metric", "filters"]

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
        """Create an instance of ApiNumbersCard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of measure
        if self.measure:
            _dict['measure'] = self.measure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of fixed_timespan
        if self.fixed_timespan:
            _dict['fixedTimespan'] = self.fixed_timespan.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of ApiNumbersCard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minScale": obj.get("minScale"),
            "maxScale": obj.get("maxScale"),
            "unit": obj.get("unit"),
            "id": obj.get("id"),
            "description": obj.get("description"),
            "measure": ApiWidgetMeasure.from_dict(obj.get("measure")) if obj.get("measure") is not None else None,
            "compareToPreviousValue": obj.get("compareToPreviousValue"),
            "fixedTimespan": ApiNumbersCardAllOfFixedTimespan.from_dict(obj.get("fixedTimespan")) if obj.get("fixedTimespan") is not None else None,
            "shouldExcludeAlertSuppressionWindows": obj.get("shouldExcludeAlertSuppressionWindows"),
            "dataSource": obj.get("dataSource"),
            "metricGroup": obj.get("metricGroup"),
            "direction": obj.get("direction"),
            "metric": obj.get("metric"),
            "filters": obj.get("filters")
        })
        return _obj


