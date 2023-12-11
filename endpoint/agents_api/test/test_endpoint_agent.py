# coding: utf-8

"""
    Endpoint Agents API

    Manage ThousandEyes Endpoint Agents using this API.

    The version of the OpenAPI document: 7.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from agents_api.models.endpoint_agent import EndpointAgent

class TestEndpointAgent(unittest.TestCase):
    """EndpointAgent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EndpointAgent:
        """Test EndpointAgent
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EndpointAgent`
        """
        model = EndpointAgent()
        if include_optional:
            return EndpointAgent(
                id = '5d0764ac-7e42-4ec8-a0d4-39fc53edccba',
                aid = None,
                name = 'Office Printer',
                computer_name = 'DESKJET-123',
                os_version = 'Version 10.15.2 (Build 19C57)',
                platform = 'mac',
                kernel_version = 'Darwin 19.2.0',
                manufacturer = 'Apple, Inc.',
                model = 'MacBookAir7,2',
                last_seen = '2022-05-26T23:37:16Z',
                status = 'enabled',
                deleted = True,
                version = '0.123.4',
                created_at = '2022-05-26T23:37:16Z',
                number_of_clients = 3,
                public_ip = '88.45.2.123',
                location = agents_api.models.endpoint_agent_location.EndpointAgentLocation(
                    latitude = 51.51279, 
                    longitude = -0.09184, 
                    location_name = 'London', ),
                clients = [
                    agents_api.models.endpoint_client.EndpointClient(
                        user_profile = agents_api.models.endpoint_user_profile.EndpointUserProfile(
                            user_name = 'joeblogs32', ), 
                        browser_extensions = [
                            agents_api.models.endpoint_browser_extension.EndpointBrowserExtension(
                                browser = 'edge', 
                                profile = 'Profile 1', 
                                version = '0.123.0', 
                                enabled = True, 
                                active = True, 
                                error = '', )
                            ], )
                    ],
                total_memory = '16384 MB',
                agent_type = 'endpoint',
                vpn_profiles = [
                    agents_api.models.endpoint_vpn_profile.EndpointVpnProfile(
                        interface_name = '', 
                        vpn_type = 'cisco-anyconnect', 
                        vpn_gateway_address = '', 
                        vpn_client_addresses = ["10.100.0.10"], 
                        vpn_client_network_range = ["10.100.0.0/22"], )
                    ],
                network_interface_profiles = [
                    agents_api.models.interface_profile.InterfaceProfile(
                        interface_name = 'en0', 
                        address_profiles = [
                            agents_api.models.address_profile.AddressProfile(
                                address_type = 'unique-local', 
                                ip_address = '2001:db8:3333:4444:5555:6666:7777:8888', 
                                prefix_length = 24, 
                                gateway = '192.168.0.254', 
                                router_hardware_address = '5c:b1:3e:46:1c:84', )
                            ], 
                        hardware_type = 'wireless', 
                        ethernet_profile = agents_api.models.ethernet_profile.EthernetProfile(
                            link_speed = 56, ), 
                        wireless_profile = agents_api.models.wireless_profile.WirelessProfile(
                            bssid = '00:11:22:aa:bb:cc', 
                            ssid = 'GuestWiFi', 
                            rssi = -36, 
                            channel = 48, 
                            phy_mode = '802.11ac', ), )
                    ],
                asn_details = agents_api.models.endpoint_asn_details.EndpointAsnDetails(
                    as_number = 5089, 
                    as_name = 'Virgin Media Limited', ),
                license_type = 'essentials',
                tcp_driver_available = True,
                npcap_version = ''
            )
        else:
            return EndpointAgent(
        )
        """

    def testEndpointAgent(self):
        """Test EndpointAgent"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
