# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.web_transaction_instant_test import WebTransactionInstantTest

class TestWebTransactionInstantTest(unittest.TestCase):
    """WebTransactionInstantTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> WebTransactionInstantTest:
        """Test WebTransactionInstantTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `WebTransactionInstantTest`
        """
        model = WebTransactionInstantTest()
        if include_optional:
            return WebTransactionInstantTest(
                created_by = 'user@user.com',
                created_date = '2022-07-17T22:00:54Z',
                description = 'ThousandEyes Test',
                live_share = False,
                modified_by = 'user@user.com',
                modified_date = '2022-07-17T22:00:54Z',
                saved_event = True,
                test_id = '281474976710706',
                test_name = 'ThousandEyes Test',
                type = 'web-transactions',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                labels = [
                    {"labelId":"961","name":"Artem label","isBuiltIn":false}
                    ],
                shared_with_accounts = [
                    tests.models.test_shared_accounts_inner.TestSharedAccounts_inner(
                        aid = '1234', 
                        name = 'Account name', )
                    ],
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
                custom_headers = {"root":{"header1":"value1"},"domains":{"domain1.com":{"header2":"value2"}},"all":{"header3":"value3"}},
                desired_status_code = '200',
                follow_redirects = True,
                http_target_time = 100,
                http_time_limit = 5,
                http_version = 1,
                include_headers = True,
                mtu_measurements = False,
                network_measurements = True,
                num_path_traces = 1,
                password = 'password',
                path_trace_mode = 'classic',
                probe_mode = 'auto',
                protocol = 'tcp',
                ssl_version = 'Auto',
                ssl_version_id = '0',
                target_time = 1,
                time_limit = 5,
                transaction_script = 'if (true) { return true; }',
                url = 'www.thousandeyes.com',
                use_ntlm = False,
                user_agent = 'curl',
                username = 'username',
                verify_certificate = True,
                allow_unsafe_legacy_renegotiation = True,
                block_domains = 'domain.com/',
                disable_screenshot = True,
                allow_mic_and_camera = True,
                allow_geolocation = True,
                browser_language = 'en-US',
                page_loading_strategy = 'normal',
                fixed_packet_rate = 50,
                agents = [
                    null
                    ],
                credentials = ["3247","1051"]
            )
        else:
            return WebTransactionInstantTest(
                transaction_script = 'if (true) { return true; }',
                url = 'www.thousandeyes.com',
        )
        """

    def testWebTransactionInstantTest(self):
        """Test WebTransactionInstantTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
