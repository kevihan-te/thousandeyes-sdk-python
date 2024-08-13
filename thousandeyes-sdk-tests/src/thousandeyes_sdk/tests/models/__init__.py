# coding: utf-8

# flake8: noqa
"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.tests.models.agent import Agent
from thousandeyes_sdk.tests.models.agent_base import AgentBase
from thousandeyes_sdk.tests.models.agent_interfaces import AgentInterfaces
from thousandeyes_sdk.tests.models.agent_request import AgentRequest
from thousandeyes_sdk.tests.models.agent_to_agent_instant_test import AgentToAgentInstantTest
from thousandeyes_sdk.tests.models.agent_to_agent_properties import AgentToAgentProperties
from thousandeyes_sdk.tests.models.agent_to_agent_test import AgentToAgentTest
from thousandeyes_sdk.tests.models.agent_to_agent_test_protocol import AgentToAgentTestProtocol
from thousandeyes_sdk.tests.models.agent_to_agent_tests import AgentToAgentTests
from thousandeyes_sdk.tests.models.agent_to_server_instant_test import AgentToServerInstantTest
from thousandeyes_sdk.tests.models.agent_to_server_properties import AgentToServerProperties
from thousandeyes_sdk.tests.models.agent_to_server_test import AgentToServerTest
from thousandeyes_sdk.tests.models.agent_to_server_tests import AgentToServerTests
from thousandeyes_sdk.tests.models.alert_direction import AlertDirection
from thousandeyes_sdk.tests.models.alert_rounds_violation_mode import AlertRoundsViolationMode
from thousandeyes_sdk.tests.models.alert_rule import AlertRule
from thousandeyes_sdk.tests.models.alert_type import AlertType
from thousandeyes_sdk.tests.models.api_instant_test import ApiInstantTest
from thousandeyes_sdk.tests.models.api_predefined_variable import ApiPredefinedVariable
from thousandeyes_sdk.tests.models.api_properties import ApiProperties
from thousandeyes_sdk.tests.models.api_request import ApiRequest
from thousandeyes_sdk.tests.models.api_request_assertion import ApiRequestAssertion
from thousandeyes_sdk.tests.models.api_request_assertion_name import ApiRequestAssertionName
from thousandeyes_sdk.tests.models.api_request_assertion_operator import ApiRequestAssertionOperator
from thousandeyes_sdk.tests.models.api_request_auth_type import ApiRequestAuthType
from thousandeyes_sdk.tests.models.api_request_header import ApiRequestHeader
from thousandeyes_sdk.tests.models.api_request_method import ApiRequestMethod
from thousandeyes_sdk.tests.models.api_request_variable import ApiRequestVariable
from thousandeyes_sdk.tests.models.api_test import ApiTest
from thousandeyes_sdk.tests.models.api_tests import ApiTests
from thousandeyes_sdk.tests.models.base_bgp_test import BaseBgpTest
from thousandeyes_sdk.tests.models.base_request import BaseRequest
from thousandeyes_sdk.tests.models.base_test import BaseTest
from thousandeyes_sdk.tests.models.bgp_test import BgpTest
from thousandeyes_sdk.tests.models.bgp_tests import BgpTests
from thousandeyes_sdk.tests.models.cloud_enterprise_agent_type import CloudEnterpriseAgentType
from thousandeyes_sdk.tests.models.dns_query_class import DnsQueryClass
from thousandeyes_sdk.tests.models.dns_sec_instant_test import DnsSecInstantTest
from thousandeyes_sdk.tests.models.dns_sec_properties import DnsSecProperties
from thousandeyes_sdk.tests.models.dns_sec_test import DnsSecTest
from thousandeyes_sdk.tests.models.dns_sec_tests import DnsSecTests
from thousandeyes_sdk.tests.models.dns_server_instant_test import DnsServerInstantTest
from thousandeyes_sdk.tests.models.dns_server_properties import DnsServerProperties
from thousandeyes_sdk.tests.models.dns_server_test import DnsServerTest
from thousandeyes_sdk.tests.models.dns_server_tests import DnsServerTests
from thousandeyes_sdk.tests.models.dns_servers_request import DnsServersRequest
from thousandeyes_sdk.tests.models.dns_trace_instant_test import DnsTraceInstantTest
from thousandeyes_sdk.tests.models.dns_trace_properties import DnsTraceProperties
from thousandeyes_sdk.tests.models.dns_trace_test import DnsTraceTest
from thousandeyes_sdk.tests.models.dns_trace_tests import DnsTraceTests
from thousandeyes_sdk.tests.models.error import Error
from thousandeyes_sdk.tests.models.expand import Expand
from thousandeyes_sdk.tests.models.ftp_server_instant_test import FtpServerInstantTest
from thousandeyes_sdk.tests.models.ftp_server_properties import FtpServerProperties
from thousandeyes_sdk.tests.models.ftp_server_request_type import FtpServerRequestType
from thousandeyes_sdk.tests.models.ftp_server_test import FtpServerTest
from thousandeyes_sdk.tests.models.ftp_server_tests import FtpServerTests
from thousandeyes_sdk.tests.models.http_server_base_properties import HttpServerBaseProperties
from thousandeyes_sdk.tests.models.http_server_instant_test import HttpServerInstantTest
from thousandeyes_sdk.tests.models.http_server_properties import HttpServerProperties
from thousandeyes_sdk.tests.models.http_server_test import HttpServerTest
from thousandeyes_sdk.tests.models.http_server_tests import HttpServerTests
from thousandeyes_sdk.tests.models.instant_test import InstantTest
from thousandeyes_sdk.tests.models.interface_group import InterfaceGroup
from thousandeyes_sdk.tests.models.interface_groups import InterfaceGroups
from thousandeyes_sdk.tests.models.link import Link
from thousandeyes_sdk.tests.models.monitor import Monitor
from thousandeyes_sdk.tests.models.monitor_type import MonitorType
from thousandeyes_sdk.tests.models.monitors_request import MonitorsRequest
from thousandeyes_sdk.tests.models.o_auth import OAuth
from thousandeyes_sdk.tests.models.page_load_instant_test import PageLoadInstantTest
from thousandeyes_sdk.tests.models.page_load_properties import PageLoadProperties
from thousandeyes_sdk.tests.models.page_load_test import PageLoadTest
from thousandeyes_sdk.tests.models.page_load_tests import PageLoadTests
from thousandeyes_sdk.tests.models.request_method import RequestMethod
from thousandeyes_sdk.tests.models.self_links import SelfLinks
from thousandeyes_sdk.tests.models.sensitivity_level import SensitivityLevel
from thousandeyes_sdk.tests.models.severity import Severity
from thousandeyes_sdk.tests.models.shared_with_account import SharedWithAccount
from thousandeyes_sdk.tests.models.simple_agent import SimpleAgent
from thousandeyes_sdk.tests.models.simple_test import SimpleTest
from thousandeyes_sdk.tests.models.sip_server_instant_test import SipServerInstantTest
from thousandeyes_sdk.tests.models.sip_server_instant_test_request import SipServerInstantTestRequest
from thousandeyes_sdk.tests.models.sip_server_instant_test_response import SipServerInstantTestResponse
from thousandeyes_sdk.tests.models.sip_server_properties import SipServerProperties
from thousandeyes_sdk.tests.models.sip_server_test import SipServerTest
from thousandeyes_sdk.tests.models.sip_server_tests import SipServerTests
from thousandeyes_sdk.tests.models.sip_test_protocol import SipTestProtocol
from thousandeyes_sdk.tests.models.test_auth_type import TestAuthType
from thousandeyes_sdk.tests.models.test_custom_headers import TestCustomHeaders
from thousandeyes_sdk.tests.models.test_direction import TestDirection
from thousandeyes_sdk.tests.models.test_dns_server import TestDnsServer
from thousandeyes_sdk.tests.models.test_dns_transport_protocol import TestDnsTransportProtocol
from thousandeyes_sdk.tests.models.test_dscp_id import TestDscpId
from thousandeyes_sdk.tests.models.test_http_interval import TestHttpInterval
from thousandeyes_sdk.tests.models.test_interval import TestInterval
from thousandeyes_sdk.tests.models.test_ipv6_policy import TestIpv6Policy
from thousandeyes_sdk.tests.models.test_label import TestLabel
from thousandeyes_sdk.tests.models.test_links import TestLinks
from thousandeyes_sdk.tests.models.test_monitors_properties import TestMonitorsProperties
from thousandeyes_sdk.tests.models.test_page_loading_strategy import TestPageLoadingStrategy
from thousandeyes_sdk.tests.models.test_path_trace_mode import TestPathTraceMode
from thousandeyes_sdk.tests.models.test_probe_mode import TestProbeMode
from thousandeyes_sdk.tests.models.test_protocol import TestProtocol
from thousandeyes_sdk.tests.models.test_request import TestRequest
from thousandeyes_sdk.tests.models.test_self_link import TestSelfLink
from thousandeyes_sdk.tests.models.test_sip_credentials import TestSipCredentials
from thousandeyes_sdk.tests.models.test_ssl_version_id import TestSslVersionId
from thousandeyes_sdk.tests.models.test_sub_interval import TestSubInterval
from thousandeyes_sdk.tests.models.test_type import TestType
from thousandeyes_sdk.tests.models.tests import Tests
from thousandeyes_sdk.tests.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.tests.models.unexpanded_agent_to_agent_test import UnexpandedAgentToAgentTest
from thousandeyes_sdk.tests.models.unexpanded_agent_to_server_test import UnexpandedAgentToServerTest
from thousandeyes_sdk.tests.models.unexpanded_api_test import UnexpandedApiTest
from thousandeyes_sdk.tests.models.unexpanded_bgp_test import UnexpandedBgpTest
from thousandeyes_sdk.tests.models.unexpanded_dns_sec_test import UnexpandedDnsSecTest
from thousandeyes_sdk.tests.models.unexpanded_dns_server_test import UnexpandedDnsServerTest
from thousandeyes_sdk.tests.models.unexpanded_dns_trace_test import UnexpandedDnsTraceTest
from thousandeyes_sdk.tests.models.unexpanded_ftp_server_test import UnexpandedFtpServerTest
from thousandeyes_sdk.tests.models.unexpanded_http_server_test import UnexpandedHttpServerTest
from thousandeyes_sdk.tests.models.unexpanded_instant_test import UnexpandedInstantTest
from thousandeyes_sdk.tests.models.unexpanded_page_load_test import UnexpandedPageLoadTest
from thousandeyes_sdk.tests.models.unexpanded_sip_server_test import UnexpandedSipServerTest
from thousandeyes_sdk.tests.models.unexpanded_test import UnexpandedTest
from thousandeyes_sdk.tests.models.unexpanded_voice_test import UnexpandedVoiceTest
from thousandeyes_sdk.tests.models.unexpanded_web_transaction_test import UnexpandedWebTransactionTest
from thousandeyes_sdk.tests.models.update_agent_to_agent_test import UpdateAgentToAgentTest
from thousandeyes_sdk.tests.models.update_agent_to_server_test import UpdateAgentToServerTest
from thousandeyes_sdk.tests.models.update_api_test import UpdateApiTest
from thousandeyes_sdk.tests.models.update_bgp_test import UpdateBgpTest
from thousandeyes_sdk.tests.models.update_bgp_test_request import UpdateBgpTestRequest
from thousandeyes_sdk.tests.models.update_dns_sec_test import UpdateDnsSecTest
from thousandeyes_sdk.tests.models.update_dns_server_test import UpdateDnsServerTest
from thousandeyes_sdk.tests.models.update_dns_trace_test import UpdateDnsTraceTest
from thousandeyes_sdk.tests.models.update_ftp_server_test import UpdateFtpServerTest
from thousandeyes_sdk.tests.models.update_http_server_test import UpdateHttpServerTest
from thousandeyes_sdk.tests.models.update_page_load_test import UpdatePageLoadTest
from thousandeyes_sdk.tests.models.update_sip_server_test import UpdateSipServerTest
from thousandeyes_sdk.tests.models.update_sip_server_test1 import UpdateSipServerTest1
from thousandeyes_sdk.tests.models.update_voice_test import UpdateVoiceTest
from thousandeyes_sdk.tests.models.update_web_transaction_test import UpdateWebTransactionTest
from thousandeyes_sdk.tests.models.validation_error import ValidationError
from thousandeyes_sdk.tests.models.validation_error_item import ValidationErrorItem
from thousandeyes_sdk.tests.models.voice_instant_test import VoiceInstantTest
from thousandeyes_sdk.tests.models.voice_properties import VoiceProperties
from thousandeyes_sdk.tests.models.voice_test import VoiceTest
from thousandeyes_sdk.tests.models.voice_tests import VoiceTests
from thousandeyes_sdk.tests.models.web_transaction_instant_test import WebTransactionInstantTest
from thousandeyes_sdk.tests.models.web_transaction_properties import WebTransactionProperties
from thousandeyes_sdk.tests.models.web_transaction_test import WebTransactionTest
from thousandeyes_sdk.tests.models.web_transaction_tests import WebTransactionTests
