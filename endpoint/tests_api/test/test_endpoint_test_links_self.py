# coding: utf-8

"""
    Endpoint Tests API

     ## Overview Manage endpoint agent dynamic and scheduled tests using the Endpoint Tests API.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tests_api.models.endpoint_test_links_self import EndpointTestLinksSelf

class TestEndpointTestLinksSelf(unittest.TestCase):
    """EndpointTestLinksSelf unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointTestLinksSelf:
        """Test EndpointTestLinksSelf
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointTestLinksSelf`
        """
        model = EndpointTestLinksSelf()
        if include_optional:
            return EndpointTestLinksSelf(
                href = 'https://api.thousandeyes.com/v7/link/to/resource/id',
                templated = True,
                type = '',
                deprecation = '',
                name = '',
                profile = '',
                title = '',
                hreflang = ''
            )
        else:
            return EndpointTestLinksSelf(
                href = 'https://api.thousandeyes.com/v7/link/to/resource/id',
        )
        """

    def testEndpointTestLinksSelf(self):
        """Test EndpointTestLinksSelf"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
