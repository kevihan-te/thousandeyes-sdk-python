# coding: utf-8

"""
    Tests API

     ### Overview This API supports listing, creating, editing, and deleting Cloud and Enterprise Agent (CEA) based tests.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from tests_api.api.voice_api import VoiceApi


class TestVoiceApi(unittest.TestCase):
    """VoiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = VoiceApi()

    def tearDown(self) -> None:
        pass

    def test_create_voice_test(self) -> None:
        """Test case for create_voice_test

        Create Voice test
        """
        pass

    def test_delete_voice_test(self) -> None:
        """Test case for delete_voice_test

        Delete Voice test
        """
        pass

    def test_get_voice_test(self) -> None:
        """Test case for get_voice_test

        Get Voice test
        """
        pass

    def test_get_voice_tests(self) -> None:
        """Test case for get_voice_tests

        List Voice tests
        """
        pass

    def test_update_voice_test(self) -> None:
        """Test case for update_voice_test

        Update Voice test
        """
        pass


if __name__ == '__main__':
    unittest.main()
