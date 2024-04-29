# coding: utf-8

"""
    Instant Tests API

    The Instant Tests API endpoint lets you create and run new instant tests. You will need to be a regular user or have the following permissions:   * `API Access`   * `View tests`  The response does not include the immediate test results. Use the Test Results endpoints to get test results after creating and executing an instant test. You can find the URLs for these endpoints in the _links section of the test definition that is returned when you create the instant test. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests.models.dns_trace_properties import DnsTraceProperties

class TestDnsTraceProperties(unittest.TestCase):
    """DnsTraceProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DnsTraceProperties:
        """Test DnsTraceProperties
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DnsTraceProperties`
        """
        model = DnsTraceProperties()
        if include_optional:
            return DnsTraceProperties(
                dns_transport_protocol = 'udp',
                domain = 'www.thousandeyes.com',
                dns_query_class = 'in',
                type = 'dns-trace'
            )
        else:
            return DnsTraceProperties(
                domain = 'www.thousandeyes.com',
        )
        """

    def testDnsTraceProperties(self):
        """Test DnsTraceProperties"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
