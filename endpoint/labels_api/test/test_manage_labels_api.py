# coding: utf-8

"""
    Endpoint Agent Labels API

    Manage labels applied to endpoint agents using this API. 

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from labels_api.api.manage_labels_api import ManageLabelsApi


class TestManageLabelsApi(unittest.TestCase):
    """ManageLabelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ManageLabelsApi()

    def tearDown(self) -> None:
        pass

    def test_endpoint_label_delete(self) -> None:
        """Test case for endpoint_label_delete

        Deletes label
        """
        pass

    def test_endpoint_label_get(self) -> None:
        """Test case for endpoint_label_get

        Retrieve label
        """
        pass

    def test_endpoint_label_update(self) -> None:
        """Test case for endpoint_label_update

        Update label
        """
        pass

    def test_endpoint_labels_list(self) -> None:
        """Test case for endpoint_labels_list

        List labels
        """
        pass

    def test_v7_endpoint_labels_post(self) -> None:
        """Test case for v7_endpoint_labels_post

        Create label
        """
        pass


if __name__ == '__main__':
    unittest.main()
