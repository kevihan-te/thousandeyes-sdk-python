# coding: utf-8

"""
    Labels API

    ### Overview This is API for the Labels API (formerly called groups).

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from labels_api.api.all_labels_api import AllLabelsApi


class TestAllLabelsApi(unittest.TestCase):
    """AllLabelsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = AllLabelsApi()

    def tearDown(self) -> None:
        pass

    def test_get_labels(self) -> None:
        """Test case for get_labels

        Get list of Labels
        """
        pass


if __name__ == '__main__':
    unittest.main()
