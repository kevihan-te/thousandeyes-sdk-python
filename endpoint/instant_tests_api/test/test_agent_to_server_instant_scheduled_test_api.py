# coding: utf-8

"""
    Endpoint Instant Scheduled Tests API

     ### Overview  You can create and execute a new endpoint instant scheduled test within ThousandEyes using this API. The test parameters are specified in the `POST` data.  The following applies to the Endpoint Instant Scheduled Tests API:  * To initiate the creation and execution of an instant scheduled test, the user must possess the `Edit endpoint tests` permission.  * Upon successful creation of an instant scheduled test, the API responds with an HTTP/201 CREATED status code and return the test definition. * It's important to note that the response does not include the results of the instant scheduled test. To retrieve test results, users can utilize the Endpoint Test Data endpoints. The URLs for these API test data endpoints are provided within the test definition output when an instant scheduled test is created. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from instant_tests_api.api.agent_to_server_instant_scheduled_test_api import AgentToServerInstantScheduledTestApi


class TestAgentToServerInstantScheduledTestApi(unittest.TestCase):
    """AgentToServerInstantScheduledTestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AgentToServerInstantScheduledTestApi()

    def tearDown(self) -> None:
        pass

    def test_post_agent_to_server_instant_test(self) -> None:
        """Test case for post_agent_to_server_instant_test

        Run agent to server instant scheduled test
        """
        pass


if __name__ == '__main__':
    unittest.main()
