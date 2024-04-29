# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_tests.models.endpoint_agent_to_server_instant_test import EndpointAgentToServerInstantTest

class TestEndpointAgentToServerInstantTest(unittest.TestCase):
    """EndpointAgentToServerInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentToServerInstantTest:
        """Test EndpointAgentToServerInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentToServerInstantTest`
        """
        model = EndpointAgentToServerInstantTest()
        if include_optional:
            return EndpointAgentToServerInstantTest(
                agent_selector_type = 'all-agents',
                agents = [0a3b9998-dc3a-4ff2-b50d-ac4a7cd986e1, 66eec0f1-72b4-4755-aa83-3aed61d17f3c],
                has_ping = True,
                has_traceroute = True,
                endpoint_agent_labels = [567, 214],
                max_machines = 10,
                port = 80,
                test_name = 'Test name',
                server_name = 'www.example.com'
            )
        else:
            return EndpointAgentToServerInstantTest(
                agent_selector_type = 'all-agents',
                max_machines = 10,
                test_name = 'Test name',
                server_name = 'www.example.com',
        )
        """

    def testEndpointAgentToServerInstantTest(self):
        """Test EndpointAgentToServerInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
