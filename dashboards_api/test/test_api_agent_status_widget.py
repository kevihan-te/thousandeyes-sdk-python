# coding: utf-8

"""
    Dashboards API

    Manage ThousandEyes Dashboards

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from dashboards_api.models.api_agent_status_widget import ApiAgentStatusWidget

class TestApiAgentStatusWidget(unittest.TestCase):
    """ApiAgentStatusWidget unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiAgentStatusWidget:
        """Test ApiAgentStatusWidget
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiAgentStatusWidget`
        """
        model = ApiAgentStatusWidget()
        if include_optional:
            return ApiAgentStatusWidget(
                id = '1234',
                type = 'Pie Chart',
                title = 'Widget Title',
                visual_mode = 'Full',
                embed_url = 'https://embed.thousandeyes.com/e/00aa:3039802d-5c76-42d2-9a93-c6e5f9d3122f',
                is_embedded = True,
                metric_group = 'BGP',
                direction = 'FROM_TARGET',
                metric = 'ENDPOINT_GATEWAY_CPU_LOAD_PERCENT',
                filters = {Tests=[5187]},
                measure = MEAN,
                fixed_timespan = dashboards_api.models.api_duration.ApiDuration(
                    value = 10, 
                    unit = 'hour', ),
                api_link = '',
                should_exclude_alert_suppression_windows = True,
                links = dashboards_api.models.self_links__links.SelfLinks__links(
                    self = dashboards_api.models.link.Link(
                        href = 'https://api.thousandeyes.com/v7/link/to/resource/id', 
                        templated = True, 
                        type = '', 
                        deprecation = '', 
                        name = '', 
                        profile = '', 
                        title = '', 
                        hreflang = '', ), ),
                agents = 'endpoint',
                show = 'owned',
                data_source = 'ENDPOINT_AST_TEST'
            )
        else:
            return ApiAgentStatusWidget(
        )
        """

    def testApiAgentStatusWidget(self):
        """Test ApiAgentStatusWidget"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
