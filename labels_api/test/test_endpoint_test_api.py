# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from labels_api.api.endpoint_test_api import EndpointTestApi


class TestEndpointTestApi(unittest.TestCase):
    """EndpointTestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = EndpointTestApi()

    def tearDown(self) -> None:
        pass

    def test_create_endpoint_tests_label(self) -> None:
        """Test case for create_endpoint_tests_label

        Create a Label of type `endpoint-test`
        """
        pass

    def test_delete_endpoint_test_label(self) -> None:
        """Test case for delete_endpoint_test_label

        Delete a Label object of type `endpoint-test`
        """
        pass

    def test_get_endpoint_test_label(self) -> None:
        """Test case for get_endpoint_test_label

        Get a Label object of type `endpoint-test`
        """
        pass

    def test_update_endpoint_test_label(self) -> None:
        """Test case for update_endpoint_test_label

        Update a Label object of type `endpoint-test`
        """
        pass


if __name__ == '__main__':
    unittest.main()
