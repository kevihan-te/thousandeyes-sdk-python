# coding: utf-8

"""
    Tests API

     ### Overview This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from tests_api.models.sip_server_instant_test import SipServerInstantTest

class TestSipServerInstantTest(unittest.TestCase):
    """SipServerInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SipServerInstantTest:
        """Test SipServerInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SipServerInstantTest`
        """
        model = SipServerInstantTest()
        if include_optional:
            return SipServerInstantTest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'sip-server',
                links = tests_api.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/pathvis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltIn":false}
                    ],
                shared_with_accounts = [
                    tests_api.models.test_shared_accounts_inner.TestSharedAccounts_inner(
                        aid = '105', 
                        name = 'Account name', )
                    ],
                agents = [
                    tests_api.models.agent.Agent()
                    ],
                auth_user = 'username',
                mtu_measurements = False,
                network_measurements = True,
                options_regex = '["a-z"]',
                password = 'password',
                path_trace_mode = 'classic',
                port = 1,
                protocol = 'tcp',
                register_enabled = True,
                sip_registrar = 'voice.thousandeyes.com',
                sip_target_time = 100,
                sip_time_limit = 5,
                target_sip_credentials = tests_api.models.test_sip_credentials.TestSipCredentials(
                    auth_user = 'username', 
                    password = 'password', 
                    port = 1024, 
                    protocol = 'tcp', 
                    sip_registrar = 'sip.thousandeyes.com', 
                    user = 'username', ),
                user = 'username',
                fixed_packet_rate = 50,
                ipv6_policy = 'use-agent-policy'
            )
        else:
            return SipServerInstantTest(
                agents = [
                    tests_api.models.agent.Agent()
                    ],
                port = 1,
                target_sip_credentials = tests_api.models.test_sip_credentials.TestSipCredentials(
                    auth_user = 'username', 
                    password = 'password', 
                    port = 1024, 
                    protocol = 'tcp', 
                    sip_registrar = 'sip.thousandeyes.com', 
                    user = 'username', ),
        )
        """

    def testSipServerInstantTest(self):
        """Test SipServerInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
