# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AzureFirewallNatRule(Model):
    """Properties of a NAT rule.

    :param name: Name of the NAT rule.
    :type name: str
    :param description: Description of the rule.
    :type description: str
    :param source_addresses: List of source IP addresses for this rule.
    :type source_addresses: list[str]
    :param destination_addresses: List of destination IP addresses for this
     rule.
    :type destination_addresses: list[str]
    :param destination_ports: List of destination ports.
    :type destination_ports: list[str]
    :param protocols: Array of AzureFirewallNetworkRuleProtocols applicable to
     this NAT rule.
    :type protocols: list[str or
     ~azure.mgmt.network.v2018_10_01.models.AzureFirewallNetworkRuleProtocol]
    :param translated_address: The translated address for this NAT rule.
    :type translated_address: str
    :param translated_port: The translated port for this NAT rule.
    :type translated_port: str
    """

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'description': {'key': 'description', 'type': 'str'},
        'source_addresses': {'key': 'sourceAddresses', 'type': '[str]'},
        'destination_addresses': {'key': 'destinationAddresses', 'type': '[str]'},
        'destination_ports': {'key': 'destinationPorts', 'type': '[str]'},
        'protocols': {'key': 'protocols', 'type': '[str]'},
        'translated_address': {'key': 'translatedAddress', 'type': 'str'},
        'translated_port': {'key': 'translatedPort', 'type': 'str'},
    }

    def __init__(self, *, name: str=None, description: str=None, source_addresses=None, destination_addresses=None, destination_ports=None, protocols=None, translated_address: str=None, translated_port: str=None, **kwargs) -> None:
        super(AzureFirewallNatRule, self).__init__(**kwargs)
        self.name = name
        self.description = description
        self.source_addresses = source_addresses
        self.destination_addresses = destination_addresses
        self.destination_ports = destination_ports
        self.protocols = protocols
        self.translated_address = translated_address
        self.translated_port = translated_port
