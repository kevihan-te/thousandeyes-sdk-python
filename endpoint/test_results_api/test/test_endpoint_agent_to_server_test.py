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

from test_results_api.models.endpoint_agent_to_server_test import EndpointAgentToServerTest

class TestEndpointAgentToServerTest(unittest.TestCase):
    """EndpointAgentToServerTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentToServerTest:
        """Test EndpointAgentToServerTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentToServerTest`
        """
        model = EndpointAgentToServerTest()
        if include_optional:
            return EndpointAgentToServerTest(
                links = test_results_api.models.endpoint_test_links.EndpointTestLinks(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/network/filter"},{"href":"https://api.thousandeyes.com/v7/endpoint/test-results/scheduled-tests/281474976710706/pathvis"}], ),
                agent_selector_config = test_results_api.models.endpoint_agent_selector_config.EndpointAgentSelectorConfig(),
                created_date = '2022-07-17T22:00:54Z',
                interval = 120,
                is_enabled = True,
                is_saved_event = False,
                has_path_trace_in_session = True,
                modified_date = '2022-07-17T22:00:54Z',
                network_measurements = True,
                port = 80,
                protocol = 'icmp',
                server = 'www.example.com',
                test_id = '281474976710706',
                aid = None,
                test_name = 'Test name',
                type = 'agent-to-server'
            )
        else:
            return EndpointAgentToServerTest(
        )
        """

    def testEndpointAgentToServerTest(self):
        """Test EndpointAgentToServerTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
