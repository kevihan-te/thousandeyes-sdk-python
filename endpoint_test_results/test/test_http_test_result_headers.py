# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_test_results.models.http_test_result_headers import HttpTestResultHeaders

class TestHttpTestResultHeaders(unittest.TestCase):
    """HttpTestResultHeaders unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> HttpTestResultHeaders:
        """Test HttpTestResultHeaders
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `HttpTestResultHeaders`
        """
        model = HttpTestResultHeaders()
        if include_optional:
            return HttpTestResultHeaders(
                request_headers = 'GET / HTTP/1.1
Host: www.thousandeyes.com
User-Agent: curl/7.58.0-DEV
Accept: */*
Accept-Encoding: deflate, gzip
X-ThousandEyes-Agent: yes
',
                response_headers = 'HTTP/1.1 200 OK
Content-Type: text/html;charset=UTF-8
Content-Length: 9993
Connection: keep-alive
Date: Mon, 04 May 2020 16:13:00 GMT
Server: Apache
Content-Language: en-US
Content-Encoding: gzip
X-Frame-Options: sameorigin
Cache-Control: max-age=600, must-revalidate
Strict-Transport-Security: max-age=31536000
X-Content-Type-Options: nosniff
X-XSS-Protection: 1; mode=block
Vary: Accept-Encoding
X-Cache: Hit from cloudfront
Via: 1.1 7ba3caf71ae7a52dd411d1a543e80cd8.cloudfront.net (CloudFront)
X-Amz-Cf-Pop: SFO5-C3
X-Amz-Cf-Id: w4h42tkoJD-rEpkRDZUvnQBmy26GVGe6pUsuRr1Dphf7oajYbjXaOA==
Age: 132
'
            )
        else:
            return HttpTestResultHeaders(
        )
        """

    def testHttpTestResultHeaders(self):
        """Test HttpTestResultHeaders"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
