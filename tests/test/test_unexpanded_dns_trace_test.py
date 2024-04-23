# coding: utf-8

"""
    Tests API

    This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests.models.unexpanded_dns_trace_test import UnexpandedDnsTraceTest

class TestUnexpandedDnsTraceTest(unittest.TestCase):
    """UnexpandedDnsTraceTest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnexpandedDnsTraceTest:
        """Test UnexpandedDnsTraceTest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnexpandedDnsTraceTest`
        """
        model = UnexpandedDnsTraceTest()
        if include_optional:
            return UnexpandedDnsTraceTest(
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
                type = 'dns-trace',
                links = tests.models.unexpanded_instant_test__links.UnexpandedInstantTest__links(
                    self = null, 
                    test_results = [{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/network"},{"href":"https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"}], ),
                dns_transport_protocol = 'udp',
                domain = 'www.thousandeyes.com',
                dns_query_class = 'in'
            )
        else:
            return UnexpandedDnsTraceTest(
                interval = 120,
                domain = 'www.thousandeyes.com',
        )
        """

    def testUnexpandedDnsTraceTest(self):
        """Test UnexpandedDnsTraceTest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
