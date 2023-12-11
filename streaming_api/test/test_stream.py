# coding: utf-8

"""
    ThousandEyes for OpenTelemetry

     Configure ThousandEyes to stream or push test data to a OpenTelemetry compliant endpoint with the ThousandEyes for OpenTelemetry API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from streaming_api.models.stream import Stream

class TestStream(unittest.TestCase):
    """Stream unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Stream:
        """Test Stream
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Stream`
        """
        model = Stream()
        if include_optional:
            return Stream(
                custom_headers = {Authorization=*****, Content-Type=*****},
                tag_match = [{objectType=test, key=keyA, value=valueA}, {objectType=test, key=keyB, value=valueB}],
                enabled = False,
                type = 'opentelemetry',
                endpoint_type = 'grpc',
                stream_endpoint_url = 'https://api.thousandeyes.otel-collector'
            )
        else:
            return Stream(
        )
        """

    def testStream(self):
        """Test Stream"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
