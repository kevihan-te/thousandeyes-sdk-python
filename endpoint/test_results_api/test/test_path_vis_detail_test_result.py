# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from test_results_api.models.path_vis_detail_test_result import PathVisDetailTestResult

class TestPathVisDetailTestResult(unittest.TestCase):
    """PathVisDetailTestResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PathVisDetailTestResult:
        """Test PathVisDetailTestResult
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PathVisDetailTestResult`
        """
        model = PathVisDetailTestResult()
        if include_optional:
            return PathVisDetailTestResult(
                agent_id = '861b7557-cd57-4bbb-b648-00bddf88ef49',
                aid = test_results_api.models.account_group_id.AccountGroupId(
                    aid = '11', ),
                round_id = 1384309800,
                server_ip = '185.199.108.153',
                system_metrics = test_results_api.models.system_metrics.SystemMetrics(
                    start_time_ms = 1581508857327, 
                    end_time_ms = 1581508867333, 
                    cpu_utilization = test_results_api.models.cpu_utilization.CpuUtilization(
                        min = 0.22, 
                        max = 0.75, 
                        mean = 0.55, 
                        median = 0.61, 
                        std_dev = 0.01, 
                        count = 150, ), 
                    physical_memory_used_bytes = test_results_api.models.physical_memory_used_bytes.PhysicalMemoryUsedBytes(
                        min = 1.2, 
                        max = 2.5, 
                        mean = 1.77, 
                        median = 1.85, 
                        std_dev = 0.25, 
                        count = 155, ), 
                    physical_memory_total_bytes = 1024, ),
                vpn_profile = test_results_api.models.vpn_profile.VpnProfile(
                    vpn_client_addresses = ["184.81.113.85","13.129.91.62"], 
                    vpn_client_network_range = [
                        '9.88.37.27'
                        ], 
                    vpn_gateway_address = '120.98.134.7', 
                    vpn_type = 'cisco-anyconnect', ),
                asn_details = test_results_api.models.asn_details.AsnDetails(
                    as_name = 'ThousandEyes, Inc', 
                    as_number = 394101, ),
                server = 'www.google.com:443',
                source_ip = '196.40.106.237',
                source_prefix = '196.40.96.0/20',
                routes = [
                    test_results_api.models.path_vis_route.PathVisRoute(
                        path_id = '4711301366345855606023718047703941305741293841502186803', 
                        hops = [
                            null
                            ], )
                    ],
                vpn_routes = [
                    test_results_api.models.path_vis_route.PathVisRoute(
                        path_id = '4711301366345855606023718047703941305741293841502186803', 
                        hops = [
                            null
                            ], )
                    ]
            )
        else:
            return PathVisDetailTestResult(
        )
        """

    def testPathVisDetailTestResult(self):
        """Test PathVisDetailTestResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
