# coding: utf-8

"""
    Internet Insights API

    We are happy to announce the release of the Internet Insights API set. This limited release includes endpoints that:  * Make our catalog provider and Internet outage data accessible to API users. * Provide access to advanced filtering, which is part of our next-generation API efforts to allow API users to fine-tune queries across all of our APIs in a consistent manner.  Internet Insights provide visibility into core Internet infrastructure, including ISPs, DNS providers, IaaS, CDNs , and SaaS providers. It tracks the macro-level impact of Internet events on individual users and enterprise networks connecting at the edge of the Internet. These events include Outages, Routing hijacks and leaks, DDoS attacks, And political interference, among others.  Future releases of the Internet Insights API set will further unlock access to core Internet Insights functionality, unlocking potential integrations to enrich customer process flows.  For more information about Internet Insights, see the [Internet Insights](https://docs.thousandeyes.com/product-documentation/internet-insights). 

    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import json
import unittest
import thousandeyes_sdk.internet_insights.models

from .test_utils import assert_constructed_model_matches_example_json
from thousandeyes_sdk.internet_insights.api.catalog_providers_api import CatalogProvidersApi


class TestCatalogProvidersApi(unittest.TestCase):
    """CatalogProvidersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = CatalogProvidersApi()

    def tearDown(self) -> None:
        pass

    def test_filter_catalog_providers_models_validation(self) -> None:
        """Test case for filter_catalog_providers request and response models"""
        request_body_json = """
                {
                  "providerName" : "Amazon Web Services",
                  "providerType" : "IAAS",
                  "region" : "North America",
                  "location" : "San Jose, US",
                  "asn" : "Amazon.com, Inc.",
                  "included" : true
                }"""

        request_loaded_json = json.loads(request_body_json)
        request_from_json = thousandeyes_sdk.internet_insights.models.ApiCatalogProviderFilter.from_json(request_body_json)
        assert_constructed_model_matches_example_json(request_from_json, request_loaded_json)

        response_body_json = """
                {
                  "_links" : {
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
                  "providers" : [ {
                    "interfacesCount" : 15,
                    "locationsCount" : 50,
                    "_links" : {
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
                    "countriesCount" : 2,
                    "dataType" : "Application",
                    "id" : "85602a0a-54a7-4e97-946e-67492ef1fa26",
                    "region" : "North America",
                    "asnsCount" : 10,
                    "included" : true,
                    "providerName" : "Amazon Web Services",
                    "providerType" : "IAAS"
                  }, {
                    "interfacesCount" : 15,
                    "locationsCount" : 50,
                    "_links" : {
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
                    "countriesCount" : 2,
                    "dataType" : "Application",
                    "id" : "85602a0a-54a7-4e97-946e-67492ef1fa26",
                    "region" : "North America",
                    "asnsCount" : 10,
                    "included" : true,
                    "providerName" : "Amazon Web Services",
                    "providerType" : "IAAS"
                  } ]
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.internet_insights.models.ApiCatalogProviderResponse.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)

    def test_get_catalog_provider_models_validation(self) -> None:
        """Test case for get_catalog_provider request and response models"""

        response_body_json = """
                {
                  "_links" : {
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
                  "dataType" : "Application",
                  "asns" : [ {
                    "name" : "LVLT-1 - Level 3 Communications, Inc.",
                    "id" : 1
                  }, {
                    "name" : "LVLT-1 - Level 3 Communications, Inc.",
                    "id" : 1
                  } ],
                  "locations" : [ {
                    "interfacesCount" : 5,
                    "location" : "San Jose, US"
                  }, {
                    "interfacesCount" : 5,
                    "location" : "San Jose, US"
                  } ],
                  "id" : "85602a0a-54a7-4e97-946e-67492ef1fa26",
                  "region" : "North America",
                  "providerName" : "Amazon Web Services",
                  "providerType" : "IAAS"
                }"""

        response_loaded_json = json.loads(response_body_json)
        response_from_json = thousandeyes_sdk.internet_insights.models.ApiCatalogProviderDetails.from_json(response_body_json)
        assert_constructed_model_matches_example_json(response_from_json, response_loaded_json)


if __name__ == '__main__':
    unittest.main()
