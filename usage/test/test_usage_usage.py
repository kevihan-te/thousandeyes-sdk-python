# coding: utf-8

"""
    Usage API

     These usage endpoints define the following operations:  * **Usage**: Retrieve usage data for the specified time period (default is one month).          * Users must have the `View Billing` permission to access this endpoint.     * This endpoint offers visibility across all account groups within the organization.     * Users with `View Billing` permission in multiple organizations should query the endpoint with the `aid` query string parameter (see optional parameters) for each organization.  * **Quotas**: Obtain organization and account usage quotas. Additionally, users with the appropriate permissions can create, update, or delete these quotas.          * Users must have the necessary permissions to perform quota-related actions.  Refer to the Usage API endpoints for detailed usage instructions and optional parameters. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from usage.models.usage_usage import UsageUsage

class TestUsageUsage(unittest.TestCase):
    """UsageUsage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UsageUsage:
        """Test UsageUsage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UsageUsage`
        """
        model = UsageUsage()
        if include_optional:
            return UsageUsage(
                quota = usage.models.usage_usage_quota.Usage_usage_quota(
                    month_start = '2020-01-05T08:00Z', 
                    month_end = '2020-02-05T08:00Z', 
                    cloud_units_included = 4320000000, 
                    endpoint_agents_included = 200, 
                    endpoint_agents_essentials_included = 10, 
                    endpoint_agents_embedded_included = 10, 
                    enterprise_agents_included = 25, ),
                cloud_units_used = 8500489,
                cloud_units_projected = 20993812,
                cloud_units_next_billing_period = 25123456,
                enterprise_units_used = 79640902,
                enterprise_units_projected = 108016317,
                enterprise_units_next_billing_period = 0,
                endpoint_agents_used = 42,
                endpoint_agents_essentials_used = 5,
                endpoint_agents_embedded_used = 5,
                enterprise_agents_used = 58,
                enterprise_agent_units = [{"aid":"1234","agentId":"121404","accountGroupName":"Support","agentName":"TEVA-test-agent","enterpriseUnitsUsed":599878,"enterpriseUnitsProjected":597808,"vagentId":"123456"},{"aid":"315","agentId":"121404","accountGroupName":"Documentation","agentName":"lab-physical-appliance-1","enterpriseUnitsUsed":597123,"enterpriseUnitsProjected":597808,"vagentId":"789"}],
                tests = [{"aid":"1234","testId":"1158","accountGroupName":"Documentation","testName":"https://app.thousandeyes.com","testType":"Web-Page Load","cloudUnitsUsed":14050,"cloudUnitsProjected":340674},{"aid":"12345","testId":"1159","accountGroupName":"Documentation","testName":"https://support.thousandeyes.com","testType":"Web - HTTP Server","cloudUnitsUsed":64390,"cloudUnitsProjected":164457}],
                endpoint_agents = [{"aid":"1234","accountGroupName":"Support","endpointAgentsUsed":22},{"aid":"12345","accountGroupName":"Documentation","endpointAgentsUsed":14}],
                endpoint_agents_essentials = [{"aid":"1234","accountGroupName":"Support","endpointAgentsEssentialsUsed":2},{"aid":"12345","accountGroupName":"Documentation","endpointAgentsEssentialsUsed":3}],
                endpoint_agents_embedded = [{"aid":"1234","accountGroupName":"Support","endpointAgentsEmbeddedUsed":2},{"aid":"12345","accountGroupName":"Documentation","endpointAgentsEmbeddedUsed":3}],
                enterprise_agents = [{"aid":"1234","accountGroupName":"Support","enterpriseAgentsUsed":7},{"aid":"12345","accountGroupName":"Documentation","enterpriseAgentsUsed":1}]
            )
        else:
            return UsageUsage(
        )
        """

    def testUsageUsage(self):
        """Test UsageUsage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
