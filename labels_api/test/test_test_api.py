# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from labels_api.api.test_api import TestApi


class TestTestApi(unittest.TestCase):
    """TestApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TestApi()

    def tearDown(self) -> None:
        pass

    def test_create_test_label(self) -> None:
        """Test case for create_test_label

        Create a Label of type `test`
        """
        pass

    def test_delete_test_label(self) -> None:
        """Test case for delete_test_label

        Delete a Label object of type `test`
        """
        pass

    def test_get_test_label(self) -> None:
        """Test case for get_test_label

        Get a Label object of type `test`
        """
        pass

    def test_update_test_label(self) -> None:
        """Test case for update_test_label

        Update a Label object of type `test`
        """
        pass


if __name__ == '__main__':
    unittest.main()
