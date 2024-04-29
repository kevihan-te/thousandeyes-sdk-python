# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.   For more information about Endpoint Agents, see [Endpoint Agents](https://docs.thousandeyes.com/product-documentation/global-vantage-points/endpoint-agents).

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_agents.models.endpoint_agents_list200_response import EndpointAgentsList200Response

class TestEndpointAgentsList200Response(unittest.TestCase):
    """EndpointAgentsList200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgentsList200Response:
        """Test EndpointAgentsList200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgentsList200Response`
        """
        model = EndpointAgentsList200Response()
        if include_optional:
            return EndpointAgentsList200Response(
                total_agents = 1,
                agents = [
                    null
                    ],
                links = endpoint_agents.models.pagination_next_and_self_link__links.PaginationNextAndSelfLink__links(
                    next = endpoint_agents.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), 
                    self = endpoint_agents.models.link.Link(
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
            return EndpointAgentsList200Response(
        )
        """

    def testEndpointAgentsList200Response(self):
        """Test EndpointAgentsList200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
