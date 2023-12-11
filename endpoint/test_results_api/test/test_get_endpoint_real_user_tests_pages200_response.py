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

from test_results_api.models.get_endpoint_real_user_tests_pages200_response import GetEndpointRealUserTestsPages200Response

class TestGetEndpointRealUserTestsPages200Response(unittest.TestCase):
    """GetEndpointRealUserTestsPages200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetEndpointRealUserTestsPages200Response:
        """Test GetEndpointRealUserTestsPages200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetEndpointRealUserTestsPages200Response`
        """
        model = GetEndpointRealUserTestsPages200Response()
        if include_optional:
            return GetEndpointRealUserTestsPages200Response(
                start_date = '2022-07-17T22:00:54Z',
                end_date = '2022-07-18T22:00:54Z',
                results = [
                    null
                    ],
                links = test_results_api.models.pagination_next_link__links.PaginationNextLink__links(
                    next = test_results_api.models.link.Link(
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
            return GetEndpointRealUserTestsPages200Response(
        )
        """

    def testGetEndpointRealUserTestsPages200Response(self):
        """Test GetEndpointRealUserTestsPages200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
