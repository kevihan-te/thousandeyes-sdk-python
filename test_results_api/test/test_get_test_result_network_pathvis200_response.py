# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from test_results_api.models.get_test_result_network_pathvis200_response import GetTestResultNetworkPathvis200Response

class TestGetTestResultNetworkPathvis200Response(unittest.TestCase):
    """GetTestResultNetworkPathvis200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTestResultNetworkPathvis200Response:
        """Test GetTestResultNetworkPathvis200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTestResultNetworkPathvis200Response`
        """
        model = GetTestResultNetworkPathvis200Response()
        if include_optional:
            return GetTestResultNetworkPathvis200Response(
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                results = [
                    null
                    ],
                test = None,
                links = test_results_api.models.self_links__links.SelfLinks__links(
                    self = test_results_api.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), )
            )
        else:
            return GetTestResultNetworkPathvis200Response(
        )
        """

    def testGetTestResultNetworkPathvis200Response(self):
        """Test GetTestResultNetworkPathvis200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
