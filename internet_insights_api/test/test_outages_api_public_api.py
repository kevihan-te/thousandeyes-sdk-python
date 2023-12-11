# coding: utf-8

"""
    Internet Insights API

    # Overview We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that: * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including: ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include: Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from internet_insights_api.api.outages_api_public_api import OutagesAPIPublicApi


class TestOutagesAPIPublicApi(unittest.TestCase):
    """OutagesAPIPublicApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OutagesAPIPublicApi()

    def tearDown(self) -> None:
        pass

    def test_get_outages_app(self) -> None:
        """Test case for get_outages_app

        Retrieve application outage
        """
        pass

    def test_get_outages_filter(self) -> None:
        """Test case for get_outages_filter

        List network and application outages
        """
        pass

    def test_get_outages_net(self) -> None:
        """Test case for get_outages_net

        Retrieve network outage
        """
        pass


if __name__ == '__main__':
    unittest.main()
