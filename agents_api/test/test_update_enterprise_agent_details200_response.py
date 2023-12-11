# coding: utf-8

"""
    Agents API

     ## Overview Manage all agents available to your account in ThousandEyes, including both Cloud and Enterprise Agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agents_api.models.update_enterprise_agent_details200_response import UpdateEnterpriseAgentDetails200Response

class TestUpdateEnterpriseAgentDetails200Response(unittest.TestCase):
    """UpdateEnterpriseAgentDetails200Response unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateEnterpriseAgentDetails200Response:
        """Test UpdateEnterpriseAgentDetails200Response
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateEnterpriseAgentDetails200Response`
        """
        model = UpdateEnterpriseAgentDetails200Response()
        if include_optional:
            return UpdateEnterpriseAgentDetails200Response(
                ip_addresses = [99.139.65.220, 99.139.65.221],
                public_ip_addresses = [192.168.1.78, 192.168.1.79],
                network = 'AT&T Services, Inc. (AS 7018)',
                agent_id = '281474976710706',
                agent_name = 'thousandeyes-stg-va-254',
                agent_type = 'enterprise-cluster',
                location = 'San Francisco Bay Area',
                country_id = 'US',
                enabled = True,
                verify_ssl_certificates = True,
                cluster_members = [
                    null
                    ],
                utilization = 25,
                account_groups = [
                    agents_api.models.account_group.AccountGroup()
                    ],
                prefix = '99.128.0.0/11',
                ipv6_policy = 'force-ipv4',
                error_details = [
                    agents_api.models.error_detail.ErrorDetail(
                        code = 'agent-version-outdated', 
                        description = 'Agent Version 0.1.1 (latest: 1.0.0)', )
                    ],
                hostname = 'thousandeyes.com',
                last_seen = '2022-07-17T22:00:54Z',
                agent_state = 'online',
                keep_browser_cache = True,
                created_date = '2022-07-17T22:00:54Z',
                target_for_tests = '1.1.1.1',
                local_resolution_prefixes = [
                    '10.2.3.3/24'
                    ],
                interface_ip_mappings = [
                    agents_api.models.interface_ip_mapping.InterfaceIpMapping(
                        interface_name = 'wlp4s0', 
                        ip_addresses = ["73.252.207.219","2601:646:300:3ae0::b977"], )
                    ],
                tests = [
                    null
                    ],
                notification_rules = [
                    agents_api.models.notification_rules.NotificationRules(
                        agent_alert_rules = [{"ruleId":"281474976710706","ruleName":"Default Agent Offline Notification","expression":"((lastContact >= 30 min))","notifyOnClear":true,"isDefault":false},{"ruleId":"281474976710709","ruleName":"Test Rule","expression":"((lastContact >= 40 min))","notifyOnClear":true,"isDefault":true}], )
                    ],
                labels = [
                    agents_api.models.labels.Labels(
                        label_id = '11', 
                        name = 'Label name', )
                    ],
                links = agents_api.models.self_links__links.SelfLinks__links(
                    self = agents_api.models.link.Link(
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
            return UpdateEnterpriseAgentDetails200Response(
        )
        """

    def testUpdateEnterpriseAgentDetails200Response(self):
        """Test UpdateEnterpriseAgentDetails200Response"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
