# coding: utf-8

"""
    Endpoint Tests API

     Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_tests.models.endpoint_agent_labels_selector_config import EndpointAgentLabelsSelectorConfig

class TestEndpointAgentLabelsSelectorConfig(unittest.TestCase):
    """EndpointAgentLabelsSelectorConfig unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentLabelsSelectorConfig:
        """Test EndpointAgentLabelsSelectorConfig
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentLabelsSelectorConfig`
        """
        model = EndpointAgentLabelsSelectorConfig()
        if include_optional:
            return EndpointAgentLabelsSelectorConfig(
                agent_selector_type = 'agent-labels',
                max_machines = 10,
                endpoint_agent_labels = ["567","214"]
            )
        else:
            return EndpointAgentLabelsSelectorConfig(
                agent_selector_type = 'agent-labels',
        )
        """

    def testEndpointAgentLabelsSelectorConfig(self):
        """Test EndpointAgentLabelsSelectorConfig"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
