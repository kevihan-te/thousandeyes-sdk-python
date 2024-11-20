# coding: utf-8

# flake8: noqa
"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from thousandeyes_sdk.endpoint_test_results.models.application_score_quality import ApplicationScoreQuality
from thousandeyes_sdk.endpoint_test_results.models.asn_details import AsnDetails
from thousandeyes_sdk.endpoint_test_results.models.conditional_operator import ConditionalOperator
from thousandeyes_sdk.endpoint_test_results.models.cpu_utilization import CpuUtilization
from thousandeyes_sdk.endpoint_test_results.models.dynamic_base_endpoint_test_result import DynamicBaseEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_test_webex import DynamicEndpointTestWebex
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_tests_data_round_search import DynamicEndpointTestsDataRoundSearch
from thousandeyes_sdk.endpoint_test_results.models.dynamic_endpoint_tests_data_search_filter import DynamicEndpointTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test import DynamicTest
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_links import DynamicTestLinks
from thousandeyes_sdk.endpoint_test_results.models.dynamic_test_self_link import DynamicTestSelfLink
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_browser import EndpointBrowser
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_data_point_score import EndpointHttpDataPointScore
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_http_server_test import EndpointHttpServerTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_ip_version_template import EndpointIpVersionTemplate
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request import EndpointNetworkTopologyResultRequest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_network_topology_result_request_filter import EndpointNetworkTopologyResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_trace import EndpointPathTrace
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_vis_hop import EndpointPathVisHop
from thousandeyes_sdk.endpoint_test_results.models.endpoint_path_vis_route import EndpointPathVisRoute
from thousandeyes_sdk.endpoint_test_results.models.endpoint_ping_data_point_score import EndpointPingDataPointScore
from thousandeyes_sdk.endpoint_test_results.models.endpoint_result_request_filter import EndpointResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_scheduled_test import EndpointScheduledTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_scheduled_test_type import EndpointScheduledTestType
from thousandeyes_sdk.endpoint_test_results.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test import EndpointTest
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_auth_type import EndpointTestAuthType
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_ethernet_profile import EndpointTestEthernetProfile
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_links import EndpointTestLinks
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_result import EndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_result_protocol import EndpointTestResultProtocol
from thousandeyes_sdk.endpoint_test_results.models.endpoint_test_self_link import EndpointTestSelfLink
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_rounds_search import EndpointTestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_search_filter import EndpointTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_search_sort import EndpointTestsDataSearchSort
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_search_sort_key import EndpointTestsDataSearchSortKey
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_threshold_filter import EndpointTestsDataThresholdFilter
from thousandeyes_sdk.endpoint_test_results.models.endpoint_tests_data_threshold_filters import EndpointTestsDataThresholdFilters
from thousandeyes_sdk.endpoint_test_results.models.error import Error
from thousandeyes_sdk.endpoint_test_results.models.expand_endpoint_http_server_options import ExpandEndpointHttpServerOptions
from thousandeyes_sdk.endpoint_test_results.models.gateway_network_ping import GatewayNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.hop import Hop
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_test_result import HttpEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_test_result_headers import HttpEndpointTestResultHeaders
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_test_results import HttpEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_rounds_search import HttpEndpointTestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_search_filter import HttpEndpointTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_search_sort import HttpEndpointTestsDataSearchSort
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_search_sort_key import HttpEndpointTestsDataSearchSortKey
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_threshold_filter import HttpEndpointTestsDataThresholdFilter
from thousandeyes_sdk.endpoint_test_results.models.http_endpoint_tests_data_threshold_filters import HttpEndpointTestsDataThresholdFilters
from thousandeyes_sdk.endpoint_test_results.models.http_error_type import HttpErrorType
from thousandeyes_sdk.endpoint_test_results.models.http_multi_endpoint_test_results import HttpMultiEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.http_threshold_filter_name import HttpThresholdFilterName
from thousandeyes_sdk.endpoint_test_results.models.interface_hardware_type import InterfaceHardwareType
from thousandeyes_sdk.endpoint_test_results.models.link import Link
from thousandeyes_sdk.endpoint_test_results.models.local_network_result import LocalNetworkResult
from thousandeyes_sdk.endpoint_test_results.models.local_network_results import LocalNetworkResults
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_detail_results import LocalNetworkTopologyDetailResults
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_result import LocalNetworkTopologyResult
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_result_base import LocalNetworkTopologyResultBase
from thousandeyes_sdk.endpoint_test_results.models.local_network_topology_results import LocalNetworkTopologyResults
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_endpoint_tests_data_rounds_search import MultiTestIdEndpointTestsDataRoundsSearch
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_endpoint_tests_data_search_filter import MultiTestIdEndpointTestsDataSearchFilter
from thousandeyes_sdk.endpoint_test_results.models.multi_test_id_network_endpoint_test_results import MultiTestIdNetworkEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.network_dynamic_endpoint_test_result import NetworkDynamicEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.network_dynamic_endpoint_test_results import NetworkDynamicEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.network_endpoint_test_result import NetworkEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.network_endpoint_test_results import NetworkEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.network_interface import NetworkInterface
from thousandeyes_sdk.endpoint_test_results.models.network_metrics import NetworkMetrics
from thousandeyes_sdk.endpoint_test_results.models.network_ping import NetworkPing
from thousandeyes_sdk.endpoint_test_results.models.network_profile import NetworkProfile
from thousandeyes_sdk.endpoint_test_results.models.network_proxy import NetworkProxy
from thousandeyes_sdk.endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile
from thousandeyes_sdk.endpoint_test_results.models.network_topology_type import NetworkTopologyType
from thousandeyes_sdk.endpoint_test_results.models.network_wireless_profile import NetworkWirelessProfile
from thousandeyes_sdk.endpoint_test_results.models.pagination_next_and_self_link import PaginationNextAndSelfLink
from thousandeyes_sdk.endpoint_test_results.models.pagination_next_link import PaginationNextLink
from thousandeyes_sdk.endpoint_test_results.models.path_vis_base_endpoint_test_result import PathVisBaseEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_endpoint_test_result import PathVisDetailDynamicEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_dynamic_endpoint_test_results import PathVisDetailDynamicEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_endpoint_test_result import PathVisDetailEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_detail_endpoint_test_results import PathVisDetailEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_dynamic_endpoint_test_result import PathVisDynamicEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_dynamic_endpoint_test_results import PathVisDynamicEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.path_vis_endpoint_test_result import PathVisEndpointTestResult
from thousandeyes_sdk.endpoint_test_results.models.path_vis_endpoint_test_results import PathVisEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.physical_memory_used_bytes import PhysicalMemoryUsedBytes
from thousandeyes_sdk.endpoint_test_results.models.platform import Platform
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test import RealUserEndpointTest
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_base import RealUserEndpointTestBase
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_coordinates import RealUserEndpointTestCoordinates
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_detail import RealUserEndpointTestDetail
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_detail_results import RealUserEndpointTestDetailResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network import RealUserEndpointTestNetwork
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network_result import RealUserEndpointTestNetworkResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_network_results import RealUserEndpointTestNetworkResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page import RealUserEndpointTestPage
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_detail_result import RealUserEndpointTestPageDetailResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_result import RealUserEndpointTestPageResult
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_results import RealUserEndpointTestPageResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_page_timings import RealUserEndpointTestPageTimings
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_result_request_filter import RealUserEndpointTestResultRequestFilter
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results import RealUserEndpointTestResults
from thousandeyes_sdk.endpoint_test_results.models.real_user_endpoint_test_results_request import RealUserEndpointTestResultsRequest
from thousandeyes_sdk.endpoint_test_results.models.self_links import SelfLinks
from thousandeyes_sdk.endpoint_test_results.models.sort_order import SortOrder
from thousandeyes_sdk.endpoint_test_results.models.system_metrics import SystemMetrics
from thousandeyes_sdk.endpoint_test_results.models.target_network_ping import TargetNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.target_profile import TargetProfile
from thousandeyes_sdk.endpoint_test_results.models.target_traceroute import TargetTraceroute
from thousandeyes_sdk.endpoint_test_results.models.tcp_connect import TcpConnect
from thousandeyes_sdk.endpoint_test_results.models.tcp_path_trace_mode_response import TcpPathTraceModeResponse
from thousandeyes_sdk.endpoint_test_results.models.test_interval import TestInterval
from thousandeyes_sdk.endpoint_test_results.models.test_label import TestLabel
from thousandeyes_sdk.endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.test_protocol import TestProtocol
from thousandeyes_sdk.endpoint_test_results.models.test_ssl_version_id import TestSslVersionId
from thousandeyes_sdk.endpoint_test_results.models.threshold_filter_name import ThresholdFilterName
from thousandeyes_sdk.endpoint_test_results.models.threshold_filter_operator import ThresholdFilterOperator
from thousandeyes_sdk.endpoint_test_results.models.traceroute import Traceroute
from thousandeyes_sdk.endpoint_test_results.models.traceroute_hop import TracerouteHop
from thousandeyes_sdk.endpoint_test_results.models.trigger import Trigger
from thousandeyes_sdk.endpoint_test_results.models.udp_path_trace_mode_response import UdpPathTraceModeResponse
from thousandeyes_sdk.endpoint_test_results.models.udp_probe_mode_response import UdpProbeModeResponse
from thousandeyes_sdk.endpoint_test_results.models.unauthorized_error import UnauthorizedError
from thousandeyes_sdk.endpoint_test_results.models.validation_error import ValidationError
from thousandeyes_sdk.endpoint_test_results.models.validation_error_item import ValidationErrorItem
from thousandeyes_sdk.endpoint_test_results.models.vpn_network_ping import VpnNetworkPing
from thousandeyes_sdk.endpoint_test_results.models.vpn_profile import VpnProfile
from thousandeyes_sdk.endpoint_test_results.models.vpn_traceroute import VpnTraceroute
from thousandeyes_sdk.endpoint_test_results.models.vpn_type import VpnType
