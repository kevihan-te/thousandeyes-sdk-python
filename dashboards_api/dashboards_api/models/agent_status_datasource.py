# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AgentStatusDatasource(str, Enum):
    """
    Datasource of the agent to retrieve status.
    """

    """
    allowed enum values
    """
    ALERTS = 'ALERTS'
    DEVICES = 'DEVICES'
    DNSP = 'DNSP'
    ENDPOINT_SCHEDULED_TEST = 'ENDPOINT_SCHEDULED_TEST'
    ENDPOINT_AST_TEST = 'ENDPOINT_AST_TEST'
    ENDPOINT_BROWSER_SESSION = 'ENDPOINT_BROWSER_SESSION'
    ENDPOINT_LOCAL_NETWORK = 'ENDPOINT_LOCAL_NETWORK'
    ENDPOINT_LOCAL_NETWORK_WIRELESS = 'ENDPOINT_LOCAL_NETWORK_WIRELESS'
    ROUTING = 'ROUTING'
    CLOUD_AND_ENTERPRISE_AGENTS = 'CLOUD_AND_ENTERPRISE_AGENTS'
    INTERNET_INSIGHTS = 'INTERNET_INSIGHTS'
    APPDYNAMICS_SERVICE_HEALTH = 'APPDYNAMICS_SERVICE_HEALTH'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentStatusDatasource from a JSON string"""
        return cls(json.loads(json_str))


