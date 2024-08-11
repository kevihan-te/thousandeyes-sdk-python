# coding: utf-8

# flake8: noqa
"""
    Event Detection API

     Event detection occurs when ThousandEyes identifies that error signals related to a component (proxy, network node, AS, server etc) have deviated from the baselines established by events. * To determine this, ThousandEyes takes the test results from all accounts groups within an organization, and analyzes that data. * Noisy test results (those that have too many errors in a short window) are removed until they stabilize, and the rest of the results are tagged with the components associated with that test result (for example, proxy, network, or server). * Next, any increase in failures from the test results and each component helps in determining the problem domain and which component may be at fault. * When this failure rate increases beyond a pre-defined threshold (set by the algorithm), an event is triggered and an email notification is sent to the user (if they've enabled email alerts).  With the Events API, you can perform the following tasks on the ThousandEyes platform: * **Retrieve Events**: Obtain a list of events and detailed information for each event. For more information about events, see [Event Detection](https://docs.thousandeyes.com/product-documentation/event-detection). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.event_detection.models.affected_agents import AffectedAgents
from thousandeyes_sdk.event_detection.models.affected_count import AffectedCount
from thousandeyes_sdk.event_detection.models.affected_targets import AffectedTargets
from thousandeyes_sdk.event_detection.models.affected_tests import AffectedTests
from thousandeyes_sdk.event_detection.models.agent_links import AgentLinks
from thousandeyes_sdk.event_detection.models.agent_local_event_detail import AgentLocalEventDetail
from thousandeyes_sdk.event_detection.models.agent_local_event_grouping import AgentLocalEventGrouping
from thousandeyes_sdk.event_detection.models.api_affected_agent import ApiAffectedAgent
from thousandeyes_sdk.event_detection.models.api_affected_target import ApiAffectedTarget
from thousandeyes_sdk.event_detection.models.api_affected_test import ApiAffectedTest
from thousandeyes_sdk.event_detection.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from thousandeyes_sdk.event_detection.models.dns_event_detail import DnsEventDetail
from thousandeyes_sdk.event_detection.models.dns_event_grouping import DnsEventGrouping
from thousandeyes_sdk.event_detection.models.error import Error
from thousandeyes_sdk.event_detection.models.event import Event
from thousandeyes_sdk.event_detection.models.event_detail import EventDetail
from thousandeyes_sdk.event_detection.models.event_detail_base import EventDetailBase
from thousandeyes_sdk.event_detection.models.event_state import EventState
from thousandeyes_sdk.event_detection.models.event_type import EventType
from thousandeyes_sdk.event_detection.models.events import Events
from thousandeyes_sdk.event_detection.models.link import Link
from thousandeyes_sdk.event_detection.models.network_event_detail import NetworkEventDetail
from thousandeyes_sdk.event_detection.models.network_event_grouping import NetworkEventGrouping
from thousandeyes_sdk.event_detection.models.network_pop_event_detail import NetworkPopEventDetail
from thousandeyes_sdk.event_detection.models.pagination_next_and_self_links import PaginationNextAndSelfLinks
from thousandeyes_sdk.event_detection.models.proxy_event_detail import ProxyEventDetail
from thousandeyes_sdk.event_detection.models.proxy_event_grouping import ProxyEventGrouping
from thousandeyes_sdk.event_detection.models.self_links import SelfLinks
from thousandeyes_sdk.event_detection.models.severity import Severity
from thousandeyes_sdk.event_detection.models.simple_event_detail import SimpleEventDetail
from thousandeyes_sdk.event_detection.models.target_event_detail import TargetEventDetail
from thousandeyes_sdk.event_detection.models.target_event_grouping import TargetEventGrouping
from thousandeyes_sdk.event_detection.models.target_network_event_detail import TargetNetworkEventDetail
from thousandeyes_sdk.event_detection.models.target_network_event_grouping import TargetNetworkEventGrouping
from thousandeyes_sdk.event_detection.models.test_links import TestLinks
from thousandeyes_sdk.event_detection.models.test_type import TestType
from thousandeyes_sdk.event_detection.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.event_detection.models.validation_error import ValidationError
from thousandeyes_sdk.event_detection.models.validation_error_item import ValidationErrorItem
