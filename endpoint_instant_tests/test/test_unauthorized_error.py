# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from endpoint_instant_tests.models.unauthorized_error import UnauthorizedError

class TestUnauthorizedError(unittest.TestCase):
    """UnauthorizedError unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UnauthorizedError:
        """Test UnauthorizedError
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UnauthorizedError`
        """
        model = UnauthorizedError()
        if include_optional:
            return UnauthorizedError(
                error = 'invalid_token',
                error_description = 'Invalid access token'
            )
        else:
            return UnauthorizedError(
        )
        """

    def testUnauthorizedError(self):
        """Test UnauthorizedError"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
