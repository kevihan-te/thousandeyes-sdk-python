# coding: utf-8

# flake8: noqa
"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from endpoint_test_results.models.account_group_id import AccountGroupId
from endpoint_test_results.models.alert_direction import AlertDirection
from endpoint_test_results.models.alert_rounds_violation_mode import AlertRoundsViolationMode
from endpoint_test_results.models.alert_rule import AlertRule
from endpoint_test_results.models.alert_type import AlertType
from endpoint_test_results.models.application_score_quality import ApplicationScoreQuality
from endpoint_test_results.models.asn_details import AsnDetails
from endpoint_test_results.models.conditional_operator import ConditionalOperator
from endpoint_test_results.models.cpu_utilization import CpuUtilization
from endpoint_test_results.models.dynamic_base_test_result import DynamicBaseTestResult
from endpoint_test_results.models.dynamic_base_test_result_webex import DynamicBaseTestResultWebex
from endpoint_test_results.models.dynamic_test import DynamicTest
from endpoint_test_results.models.dynamic_test_links import DynamicTestLinks
from endpoint_test_results.models.dynamic_test_links_self import DynamicTestLinksSelf
from endpoint_test_results.models.dynamic_tests_data_round_search import DynamicTestsDataRoundSearch
from endpoint_test_results.models.dynamic_tests_data_search_filter import DynamicTestsDataSearchFilter
from endpoint_test_results.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig
from endpoint_test_results.models.endpoint_agent_selector_config import EndpointAgentSelectorConfig
from endpoint_test_results.models.endpoint_agent_to_server_test import EndpointAgentToServerTest
from endpoint_test_results.models.endpoint_all_agents_selector_config import EndpointAllAgentsSelectorConfig
from endpoint_test_results.models.endpoint_browser import EndpointBrowser
from endpoint_test_results.models.endpoint_http_data_point_score import EndpointHttpDataPointScore
from endpoint_test_results.models.endpoint_http_server_base_test import EndpointHttpServerBaseTest
from endpoint_test_results.models.endpoint_http_server_test import EndpointHttpServerTest
from endpoint_test_results.models.endpoint_network_topology_result_request_filter import EndpointNetworkTopologyResultRequestFilter
from endpoint_test_results.models.endpoint_ping_data_point_score import EndpointPingDataPointScore
from endpoint_test_results.models.endpoint_real_user_test import EndpointRealUserTest
from endpoint_test_results.models.endpoint_real_user_test_base import EndpointRealUserTestBase
from endpoint_test_results.models.endpoint_real_user_test_detail import EndpointRealUserTestDetail
from endpoint_test_results.models.endpoint_real_user_test_detail_results import EndpointRealUserTestDetailResults
from endpoint_test_results.models.endpoint_real_user_test_result_request_filter import EndpointRealUserTestResultRequestFilter
from endpoint_test_results.models.endpoint_real_user_test_results import EndpointRealUserTestResults
from endpoint_test_results.models.endpoint_result_request_filter import EndpointResultRequestFilter
from endpoint_test_results.models.endpoint_scheduled_test import EndpointScheduledTest
from endpoint_test_results.models.endpoint_scheduled_test_type import EndpointScheduledTestType
from endpoint_test_results.models.endpoint_specific_agents_selector_config import EndpointSpecificAgentsSelectorConfig
from endpoint_test_results.models.endpoint_test import EndpointTest
from endpoint_test_results.models.endpoint_test_auth_type import EndpointTestAuthType
from endpoint_test_results.models.endpoint_test_links import EndpointTestLinks
from endpoint_test_results.models.endpoint_test_links_self import EndpointTestLinksSelf
from endpoint_test_results.models.endpoint_test_protocol import EndpointTestProtocol
from endpoint_test_results.models.error import Error
from endpoint_test_results.models.ethernet_profile import EthernetProfile
from endpoint_test_results.models.expand import Expand
from endpoint_test_results.models.get_dynamic_test_result_network_pathvis200_response import GetDynamicTestResultNetworkPathvis200Response
from endpoint_test_results.models.get_dynamic_test_result_pathvis_agent_round200_response import GetDynamicTestResultPathvisAgentRound200Response
from endpoint_test_results.models.get_endpoint_local_network_topology_details200_response import GetEndpointLocalNetworkTopologyDetails200Response
from endpoint_test_results.models.get_endpoint_local_networks200_response import GetEndpointLocalNetworks200Response
from endpoint_test_results.models.get_endpoint_local_networks_topologies200_response import GetEndpointLocalNetworksTopologies200Response
from endpoint_test_results.models.get_endpoint_local_networks_topologies_request import GetEndpointLocalNetworksTopologiesRequest
from endpoint_test_results.models.get_endpoint_real_user_test_details200_response import GetEndpointRealUserTestDetails200Response
from endpoint_test_results.models.get_endpoint_real_user_test_pages_details200_response import GetEndpointRealUserTestPagesDetails200Response
from endpoint_test_results.models.get_endpoint_real_user_tests200_response import GetEndpointRealUserTests200Response
from endpoint_test_results.models.get_endpoint_real_user_tests_network200_response import GetEndpointRealUserTestsNetwork200Response
from endpoint_test_results.models.get_endpoint_real_user_tests_pages200_response import GetEndpointRealUserTestsPages200Response
from endpoint_test_results.models.get_endpoint_real_user_tests_request import GetEndpointRealUserTestsRequest
from endpoint_test_results.models.get_test_result_http_server200_response import GetTestResultHttpServer200Response
from endpoint_test_results.models.get_test_result_network_pathvis200_response import GetTestResultNetworkPathvis200Response
from endpoint_test_results.models.get_test_result_pathvis_agent_round200_response import GetTestResultPathvisAgentRound200Response
from endpoint_test_results.models.hop import Hop
from endpoint_test_results.models.http_error_type import HttpErrorType
from endpoint_test_results.models.http_test_result import HttpTestResult
from endpoint_test_results.models.http_test_result_headers import HttpTestResultHeaders
from endpoint_test_results.models.http_test_results import HttpTestResults
from endpoint_test_results.models.interface_hardware_type import InterfaceHardwareType
from endpoint_test_results.models.link import Link
from endpoint_test_results.models.local_network_result import LocalNetworkResult
from endpoint_test_results.models.local_network_results import LocalNetworkResults
from endpoint_test_results.models.local_network_topology_detail_results import LocalNetworkTopologyDetailResults
from endpoint_test_results.models.local_network_topology_result import LocalNetworkTopologyResult
from endpoint_test_results.models.local_network_topology_result_base import LocalNetworkTopologyResultBase
from endpoint_test_results.models.local_network_topology_results import LocalNetworkTopologyResults
from endpoint_test_results.models.multi_test_id_network_test_results import MultiTestIdNetworkTestResults
from endpoint_test_results.models.multi_test_id_tests_data_rounds_search import MultiTestIdTestsDataRoundsSearch
from endpoint_test_results.models.multi_test_id_tests_data_search_filter import MultiTestIdTestsDataSearchFilter
from endpoint_test_results.models.network_dynamic_test_result import NetworkDynamicTestResult
from endpoint_test_results.models.network_dynamic_test_results import NetworkDynamicTestResults
from endpoint_test_results.models.network_interface import NetworkInterface
from endpoint_test_results.models.network_metrics import NetworkMetrics
from endpoint_test_results.models.network_ping import NetworkPing
from endpoint_test_results.models.network_profile import NetworkProfile
from endpoint_test_results.models.network_proxy_profile import NetworkProxyProfile
from endpoint_test_results.models.network_proxy_profile_proxies_inner import NetworkProxyProfileProxiesInner
from endpoint_test_results.models.network_test_result import NetworkTestResult
from endpoint_test_results.models.network_test_results import NetworkTestResults
from endpoint_test_results.models.network_topology_type import NetworkTopologyType
from endpoint_test_results.models.network_wireless_profile import NetworkWirelessProfile
from endpoint_test_results.models.pagination_next_and_self_link import PaginationNextAndSelfLink
from endpoint_test_results.models.pagination_next_and_self_link_links import PaginationNextAndSelfLinkLinks
from endpoint_test_results.models.pagination_next_link import PaginationNextLink
from endpoint_test_results.models.pagination_next_link_links import PaginationNextLinkLinks
from endpoint_test_results.models.path_vis_base_test_result import PathVisBaseTestResult
from endpoint_test_results.models.path_vis_detail_dynamic_test_result import PathVisDetailDynamicTestResult
from endpoint_test_results.models.path_vis_detail_dynamic_test_results import PathVisDetailDynamicTestResults
from endpoint_test_results.models.path_vis_detail_test_result import PathVisDetailTestResult
from endpoint_test_results.models.path_vis_detail_test_results import PathVisDetailTestResults
from endpoint_test_results.models.path_vis_dynamic_test_result import PathVisDynamicTestResult
from endpoint_test_results.models.path_vis_dynamic_test_results import PathVisDynamicTestResults
from endpoint_test_results.models.path_vis_endpoint import PathVisEndpoint
from endpoint_test_results.models.path_vis_hop import PathVisHop
from endpoint_test_results.models.path_vis_route import PathVisRoute
from endpoint_test_results.models.path_vis_test_result import PathVisTestResult
from endpoint_test_results.models.path_vis_test_results import PathVisTestResults
from endpoint_test_results.models.physical_memory_used_bytes import PhysicalMemoryUsedBytes
from endpoint_test_results.models.platform import Platform
from endpoint_test_results.models.post_fetch_dynamic_test_result_metrics200_response import PostFetchDynamicTestResultMetrics200Response
from endpoint_test_results.models.post_fetch_test_result_metrics200_response import PostFetchTestResultMetrics200Response
from endpoint_test_results.models.post_fetch_test_result_metrics_multi_test200_response import PostFetchTestResultMetricsMultiTest200Response
from endpoint_test_results.models.query_window import QueryWindow
from endpoint_test_results.models.real_user_test_coordinates import RealUserTestCoordinates
from endpoint_test_results.models.real_user_test_network import RealUserTestNetwork
from endpoint_test_results.models.real_user_test_network_gateway_ping import RealUserTestNetworkGatewayPing
from endpoint_test_results.models.real_user_test_network_ping import RealUserTestNetworkPing
from endpoint_test_results.models.real_user_test_network_result import RealUserTestNetworkResult
from endpoint_test_results.models.real_user_test_network_results import RealUserTestNetworkResults
from endpoint_test_results.models.real_user_test_network_traceroute import RealUserTestNetworkTraceroute
from endpoint_test_results.models.real_user_test_network_vpn_ping import RealUserTestNetworkVpnPing
from endpoint_test_results.models.real_user_test_network_vpn_traceroute import RealUserTestNetworkVpnTraceroute
from endpoint_test_results.models.real_user_test_page import RealUserTestPage
from endpoint_test_results.models.real_user_test_page_page_timings import RealUserTestPagePageTimings
from endpoint_test_results.models.real_user_test_page_result import RealUserTestPageResult
from endpoint_test_results.models.real_user_test_page_results import RealUserTestPageResults
from endpoint_test_results.models.self_links import SelfLinks
from endpoint_test_results.models.self_links_links import SelfLinksLinks
from endpoint_test_results.models.severity import Severity
from endpoint_test_results.models.sort_order import SortOrder
from endpoint_test_results.models.system_metrics import SystemMetrics
from endpoint_test_results.models.tcp_connect import TcpConnect
from endpoint_test_results.models.test_interval import TestInterval
from endpoint_test_results.models.test_labels_inner import TestLabelsInner
from endpoint_test_results.models.test_probe_mode_response import TestProbeModeResponse
from endpoint_test_results.models.test_result import TestResult
from endpoint_test_results.models.test_ssl_version_id import TestSslVersionId
from endpoint_test_results.models.tests_data_rounds_search import TestsDataRoundsSearch
from endpoint_test_results.models.tests_data_search_filter import TestsDataSearchFilter
from endpoint_test_results.models.tests_data_search_sort import TestsDataSearchSort
from endpoint_test_results.models.tests_data_search_sort_key import TestsDataSearchSortKey
from endpoint_test_results.models.tests_data_threshold_filter import TestsDataThresholdFilter
from endpoint_test_results.models.tests_data_threshold_filters import TestsDataThresholdFilters
from endpoint_test_results.models.threshold_filter_name import ThresholdFilterName
from endpoint_test_results.models.threshold_filter_operator import ThresholdFilterOperator
from endpoint_test_results.models.traceroute import Traceroute
from endpoint_test_results.models.traceroute_hop import TracerouteHop
from endpoint_test_results.models.trigger import Trigger
from endpoint_test_results.models.unauthorized_error import UnauthorizedError
from endpoint_test_results.models.validation_error import ValidationError
from endpoint_test_results.models.validation_error_all_of_errors import ValidationErrorAllOfErrors
from endpoint_test_results.models.vpn_profile import VpnProfile
from endpoint_test_results.models.vpn_type import VpnType
