# coding: utf-8

"""
    Internet Insights API

    # Overview We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that: * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including: ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include: Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from internet_insights_api.models.api_catalog_provider_response import ApiCatalogProviderResponse

class TestApiCatalogProviderResponse(unittest.TestCase):
    """ApiCatalogProviderResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiCatalogProviderResponse:
        """Test ApiCatalogProviderResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiCatalogProviderResponse`
        """
        model = ApiCatalogProviderResponse()
        if include_optional:
            return ApiCatalogProviderResponse(
                links = internet_insights_api.models.self_links__links.SelfLinks__links(
                    self = internet_insights_api.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), ),
                providers = [
                    null
                    ]
            )
        else:
            return ApiCatalogProviderResponse(
        )
        """

    def testApiCatalogProviderResponse(self):
        """Test ApiCatalogProviderResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
