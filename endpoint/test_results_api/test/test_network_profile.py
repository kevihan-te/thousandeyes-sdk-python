# coding: utf-8

"""
    Endpoint Test Results API

    Retrieve results for scheduled and dynamic tests on endpoint agents.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from test_results_api.models.network_profile import NetworkProfile

class TestNetworkProfile(unittest.TestCase):
    """NetworkProfile unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkProfile:
        """Test NetworkProfile
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkProfile`
        """
        model = NetworkProfile()
        if include_optional:
            return NetworkProfile(
                ip_address = '10.0.0.13',
                subnet_mask = '255.255.255.0',
                public_ip_address = '84.255.241.1',
                local_prefix = '10.0.0.0',
                public_ip_range = '84.255.241.0-84.255.241.255',
                dns_servers = [8.8.8.8, 8.8.8.4],
                hardware_type = 'wireless',
                interface_name = 'en0',
                error = 'An operation timed out.',
                gateway = '10.0.0.1',
                wireless_profile = test_results_api.models.network_wireless_profile.NetworkWirelessProfile(
                    ssid = 'Internet for the masses', 
                    bssid = '4c:ba:ba:f4:fa:fa', 
                    channel = 1, 
                    phy_mode = '802.11n', 
                    rssi = -38, 
                    noise = -95, 
                    quality = 100, 
                    tx_rate = 130, 
                    vendor = 'Cisco', ),
                proxy_profile = test_results_api.models.network_proxy_profile.NetworkProxyProfile(
                    method = 'System', 
                    proxies = [
                        test_results_api.models.network_proxy_profile_proxies_inner.NetworkProxyProfile_proxies_inner(
                            bypass = '*.local;169.254/16', 
                            proxy = '<direct>', )
                        ], ),
                ethernet_profile = test_results_api.models.ethernet_profile.EthernetProfile(
                    link_speed = 860, ),
                previous_interface = test_results_api.models.network_interface.NetworkInterface(
                    ip_address = '10.0.0.13', 
                    subnet_mask = '255.255.255.0', 
                    public_ip_address = '84.255.241.1', 
                    local_prefix = '10.0.0.0', 
                    public_ip_range = '84.255.241.0-84.255.241.255', 
                    dns_servers = ["8.8.8.8","8.8.8.4"], 
                    hardware_type = 'wireless', 
                    interface_name = 'en0', )
            )
        else:
            return NetworkProfile(
        )
        """

    def testNetworkProfile(self):
        """Test NetworkProfile"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
