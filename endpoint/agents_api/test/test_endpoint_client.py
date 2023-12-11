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

from agents_api.models.endpoint_client import EndpointClient

class TestEndpointClient(unittest.TestCase):
    """EndpointClient unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointClient:
        """Test EndpointClient
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointClient`
        """
        model = EndpointClient()
        if include_optional:
            return EndpointClient(
                user_profile = agents_api.models.endpoint_user_profile.EndpointUserProfile(
                    user_name = 'joeblogs32', ),
                browser_extensions = [
                    agents_api.models.endpoint_browser_extension.EndpointBrowserExtension(
                        browser = 'edge', 
                        profile = 'Profile 1', 
                        version = '0.123.0', 
                        enabled = True, 
                        active = True, 
                        error = '', )
                    ]
            )
        else:
            return EndpointClient(
        )
        """

    def testEndpointClient(self):
        """Test EndpointClient"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
