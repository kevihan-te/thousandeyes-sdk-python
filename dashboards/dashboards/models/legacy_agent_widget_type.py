# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class LegacyAgentWidgetType(str, Enum):
    """
    Type of the agent.
    """

    """
    allowed enum values
    """
    ENTERPRISE_AGENTS = 'Enterprise Agents'
    ENDPOINT_AGENTS = 'Endpoint Agents'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of LegacyAgentWidgetType from a JSON string"""
        return cls(json.loads(json_str))


