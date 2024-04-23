# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.unexpanded_http_server_test import UnexpandedHttpServerTest

class TestUnexpandedHttpServerTest(unittest.TestCase):
    """UnexpandedHttpServerTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnexpandedHttpServerTest:
        """Test UnexpandedHttpServerTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnexpandedHttpServerTest`
        """
        model = UnexpandedHttpServerTest()
        if include_optional:
            return UnexpandedHttpServerTest(
                interval = 120,
                alerts_enabled = True,
                enabled = True,
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'http-server',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                auth_type = 'none',
                bandwidth_measurements = True,
                client_certificate = '-----BEGIN PRIVATE KEY-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END PRIVATE KEY-----
-----BEGIN CERTIFICATE-----
MIICUTCCAfugAwIBAgIBADANBgkqhkiG9w0BAQQFADBXMQswCQYDVQQGEwJDTjEL
-----END CERTIFICATE-----
',
                content_regex = '(regex)+',
                headers = [header1: value1, header2: value2],
                custom_headers = {"root":{"header1":"value1"},"domains":{"domain1.com":{"header2":"value2"}},"all":{"header3":"value3"}},
                desired_status_code = '200',
                download_limit = 2048,
                dns_override = '8.8.8.8',
                http_target_time = 100,
                http_time_limit = 5,
                http_version = 1,
                include_headers = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                password = 'password',
                path_trace_mode = 'classic',
                post_body = '{ "example" : "value"}',
                probe_mode = 'auto',
                protocol = 'tcp',
                ssl_version = 'Auto',
                ssl_version_id = '0',
                url = 'www.thousandeyes.com',
                use_ntlm = False,
                user_agent = 'curl',
                username = 'username',
                verify_certificate = True,
                allow_unsafe_legacy_renegotiation = True,
                ipv6_policy = 'use-agent-policy',
                follow_redirects = True,
                fixed_packet_rate = 50,
                bgp_measurements = True,
                use_public_bgp = True
            )
        else:
            return UnexpandedHttpServerTest(
                interval = 120,
                url = 'www.thousandeyes.com',
        )
        """

    def testUnexpandedHttpServerTest(self):
        """Test UnexpandedHttpServerTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
