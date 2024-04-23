# coding: utf-8

# flake8: noqa

"""
    BGP Monitors API

     Retrieve information about BGP monitors available to your ThousandEyes account. ThousandEyes ingests BGP routing data from dozens of global BGP collectors and automatically integrates that visibility as a configurable layer under service, network, and path visualization layers.  When you specify a service URL in a test, layered BGP tests automatically track reachability and path changes for any relevant prefix. When you use an IP address as the target for a test, the ThousandEyes platform monitors the relevant internet-routed prefix. You can also create specific BGP monitoring for a prefix, and can alert on hijacks and leaks.  For more information about monitors, see [Inside-Out BGP Visibility](https://docs.thousandeyes.com/product-documentation/internet-and-wan-monitoring/tests/bgp-tests/inside-out-bgp-visibility). 

    The version of the OpenAPI document: 7.0.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "1.0.0"

# import apis into sdk package
from monitors.api.list_bgp_monitors_api import ListBGPMonitorsApi

# import ApiClient
from monitors.api_response import ApiResponse
from monitors.api_client import ApiClient
from monitors.configuration import Configuration
from monitors.exceptions import OpenApiException
from monitors.exceptions import ApiTypeError
from monitors.exceptions import ApiValueError
from monitors.exceptions import ApiKeyError
from monitors.exceptions import ApiAttributeError
from monitors.exceptions import ApiException

# import models into sdk package
from monitors.models.error import Error
from monitors.models.get_bgp_monitors200_response import GetBGPMonitors200Response
from monitors.models.link import Link
from monitors.models.monitor import Monitor
from monitors.models.monitor_type import MonitorType
from monitors.models.monitors import Monitors
from monitors.models.self_links import SelfLinks
from monitors.models.self_links_links import SelfLinksLinks
from monitors.models.unauthorized_error import UnauthorizedError
