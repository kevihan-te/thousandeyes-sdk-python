# coding: utf-8

"""
    Test Results API

    Get test result metrics for Cloud and Enterprise Agent tests.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from test_results.models.get_test_results_bgp200_response import GetTestResultsBgp200Response

class TestGetTestResultsBgp200Response(unittest.TestCase):
    """GetTestResultsBgp200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetTestResultsBgp200Response:
        """Test GetTestResultsBgp200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetTestResultsBgp200Response`
        """
        model = GetTestResultsBgp200Response()
        if include_optional:
            return GetTestResultsBgp200Response(
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                results = [
                    null
                    ],
                test = { },
                links = test_results.models.pagination_links__links.PaginationLinks__links(
                    previous = test_results.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    next = test_results.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = , )
            )
        else:
            return GetTestResultsBgp200Response(
        )
        """

    def testGetTestResultsBgp200Response(self):
        """Test GetTestResultsBgp200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
