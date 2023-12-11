# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agents_api.models.endpoint_agent_location import EndpointAgentLocation

class TestEndpointAgentLocation(unittest.TestCase):
    """EndpointAgentLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentLocation:
        """Test EndpointAgentLocation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentLocation`
        """
        model = EndpointAgentLocation()
        if include_optional:
            return EndpointAgentLocation(
                latitude = 51.51279,
                longitude = -0.09184,
                location_name = 'London'
            )
        else:
            return EndpointAgentLocation(
        )
        """

    def testEndpointAgentLocation(self):
        """Test EndpointAgentLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
