# coding: utf-8

"""
    Test Snapshots API

    Creates a new test snapshot in ThousandEyes.

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.snapshots.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.snapshots.api.create_test_snapshot_api import CreateTestSnapshotApi


class TestCreateTestSnapshotApi(unittest.TestCase):
    """CreateTestSnapshotApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CreateTestSnapshotApi()

    def tearDown(self) -> None:
        pass

    def test_create_test_snapshot_models_validation(self) -> None:
        """Test case for create_test_snapshot request and response models"""
        request_body_json = """
                {
                  "endDate" : "2023-06-06T01:00:00Z",
                  "displayName" : "Snapshot created through API",
                  "isPublic" : false,
                  "startDate" : "2023-06-06T00:00:00Z"
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.snapshots.models.SnapshotRequest.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "shareDate" : "2023-06-06T00:00:00Z",
                  "uid" : "281474976810911",
                  "test" : {
                    "_links" : {
                      "testResults" : [ {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/network"
                      }, {
                        "href" : "https://api.thousandeyes.com/v7/test-results/281474976710706/path-vis"
                      } ],
                      "self" : {
                        "hreflang" : "hreflang",
                        "templated" : true,
                        "profile" : "profile",
                        "name" : "name",
                        "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                        "type" : "type",
                        "deprecation" : "deprecation",
                        "title" : "title"
                      }
                    },
                    "liveShare" : false,
                    "savedEvent" : true,
                    "description" : "ThousandEyes Test",
                    "type" : "agent-to-server",
                    "enabled" : true,
                    "createdDate" : "2022-07-17T22:00:54Z",
                    "createdBy" : "user@user.com",
                    "modifiedDate" : "2022-07-17T22:00:54Z",
                    "interval" : 120,
                    "modifiedBy" : "user@user.com",
                    "testId" : "281474976710706",
                    "alertsEnabled" : true,
                    "testName" : "ThousandEyes Test"
                  },
                  "_links" : {
                    "appLink" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    },
                    "self" : {
                      "hreflang" : "hreflang",
                      "templated" : true,
                      "profile" : "profile",
                      "name" : "name",
                      "href" : "https://api.thousandeyes.com/v7/link/to/resource/id",
                      "type" : "type",
                      "deprecation" : "deprecation",
                      "title" : "title"
                    }
                  },
                  "startRoundId" : 1538784000,
                  "displayName" : "Snapshot created through API",
                  "endRoundId" : 1538787600,
                  "testId" : "281474976710801",
                  "extraParams" : "params",
                  "id" : "wdiac",
                  "roundId" : 1538784000,
                  "sourceTestId" : "281474976710706"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.snapshots.models.SnapshotResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
