# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
from inspect import getfullargspec
import json
import pprint
import re  # noqa: F401

from typing import Any, List, Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from test_results_api.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from test_results_api.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from test_results_api.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from typing import Union, Any, List, TYPE_CHECKING, Optional, Dict
from typing_extensions import Literal
from pydantic import StrictStr, Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

ENDPOINTAGENTSELECTORCONFIG_ONE_OF_SCHEMAS = ["EndpointAgentLabelsSelectorConfig", "EndpointAllAgentsSelectorConfig", "EndpointSpecificAgentsSelectorConfig"]

class EndpointAgentSelectorConfig(BaseModel):
    """
    Agents selection object based on agentSelectorType.
    """
    # data type: EndpointAllAgentsSelectorConfig
    oneof_schema_1_validator: Optional[EndpointAllAgentsSelectorConfig] = None
    # data type: EndpointAgentLabelsSelectorConfig
    oneof_schema_2_validator: Optional[EndpointAgentLabelsSelectorConfig] = None
    # data type: EndpointSpecificAgentsSelectorConfig
    oneof_schema_3_validator: Optional[EndpointSpecificAgentsSelectorConfig] = None
    actual_instance: Optional[Union[EndpointAgentLabelsSelectorConfig, EndpointAllAgentsSelectorConfig, EndpointSpecificAgentsSelectorConfig]] = None
    one_of_schemas: List[str] = Literal["EndpointAgentLabelsSelectorConfig", "EndpointAllAgentsSelectorConfig", "EndpointSpecificAgentsSelectorConfig"]

    model_config = {
        "validate_assignment": True
    }


    discriminator_value_class_map: Dict[str, str] = {
    }

    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EndpointAgentSelectorConfig.model_construct()
        error_messages = []
        match = 0
        # validate data type: EndpointAllAgentsSelectorConfig
        if not isinstance(v, EndpointAllAgentsSelectorConfig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EndpointAllAgentsSelectorConfig`")
        else:
            match += 1
        # validate data type: EndpointAgentLabelsSelectorConfig
        if not isinstance(v, EndpointAgentLabelsSelectorConfig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EndpointAgentLabelsSelectorConfig`")
        else:
            match += 1
        # validate data type: EndpointSpecificAgentsSelectorConfig
        if not isinstance(v, EndpointSpecificAgentsSelectorConfig):
            error_messages.append(f"Error! Input type `{type(v)}` is not `EndpointSpecificAgentsSelectorConfig`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EndpointAgentSelectorConfig with oneOf schemas: EndpointAgentLabelsSelectorConfig, EndpointAllAgentsSelectorConfig, EndpointSpecificAgentsSelectorConfig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EndpointAgentSelectorConfig with oneOf schemas: EndpointAgentLabelsSelectorConfig, EndpointAllAgentsSelectorConfig, EndpointSpecificAgentsSelectorConfig. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into EndpointAllAgentsSelectorConfig
        try:
            instance.actual_instance = EndpointAllAgentsSelectorConfig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EndpointAgentLabelsSelectorConfig
        try:
            instance.actual_instance = EndpointAgentLabelsSelectorConfig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into EndpointSpecificAgentsSelectorConfig
        try:
            instance.actual_instance = EndpointSpecificAgentsSelectorConfig.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EndpointAgentSelectorConfig with oneOf schemas: EndpointAgentLabelsSelectorConfig, EndpointAllAgentsSelectorConfig, EndpointSpecificAgentsSelectorConfig. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EndpointAgentSelectorConfig with oneOf schemas: EndpointAgentLabelsSelectorConfig, EndpointAllAgentsSelectorConfig, EndpointSpecificAgentsSelectorConfig. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        to_json = getattr(self.actual_instance, "to_json", None)
        if callable(to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        to_dict = getattr(self.actual_instance, "to_dict", None)
        if callable(to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


