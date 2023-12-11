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

from tests_api.models.update_ftp_server_test import UpdateFtpServerTest

class TestUpdateFtpServerTest(unittest.TestCase):
    """UpdateFtpServerTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpdateFtpServerTest:
        """Test UpdateFtpServerTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpdateFtpServerTest`
        """
        model = UpdateFtpServerTest()
        if include_optional:
            return UpdateFtpServerTest(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                alert_rules = [344753, 212697],
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'ftp-server',
                links = tests_api.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/pathvis"}], ),
                labels = [9842, 1283],
                shared_with_accounts = [2087, 100],
                agents = [
                    {"agentId":"125","sourceIpAddress":"1.1.1.1"}
                    ],
                bandwidth_measurements = True,
                download_limit = 1048576,
                ftp_target_time = 1000,
                ftp_time_limit = 10,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 3,
                password = 'password',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                protocol = 'tcp',
                request_type = 'download',
                url = 'www.thousandeyes.com',
                use_active_ftp = True,
                use_explicit_ftps = False,
                username = 'username',
                fixed_packet_rate = 50,
                ipv6_policy = 'use-agent-policy',
                bgp_measurements = True,
                monitors = [17410, 5]
            )
        else:
            return UpdateFtpServerTest(
                interval = 120,
                agents = [
                    {"agentId":"125","sourceIpAddress":"1.1.1.1"}
                    ],
                password = 'password',
                request_type = 'download',
                url = 'www.thousandeyes.com',
                username = 'username',
        )
        """

    def testUpdateFtpServerTest(self):
        """Test UpdateFtpServerTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
