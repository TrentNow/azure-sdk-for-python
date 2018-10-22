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


class ServiceReplicaProperties(Model):
    """Describes the properties of a service replica.

    All required parameters must be populated in order to send to Azure.

    :param os_type: Required. The operation system required by the code in
     service. Possible values include: 'Linux', 'Windows'
    :type os_type: str or
     ~azure.mgmt.servicefabricmesh.models.OperatingSystemType
    :param code_packages: Required. Describes the set of code packages that
     forms the service. A code package describes the container and the
     properties for running it. All the code packages are started together on
     the same host and share the same context (network, process etc.).
    :type code_packages:
     list[~azure.mgmt.servicefabricmesh.models.ContainerCodePackageProperties]
    :param network_refs: The names of the private networks that this service
     needs to be part of.
    :type network_refs: list[~azure.mgmt.servicefabricmesh.models.NetworkRef]
    :param diagnostics: Reference to sinks in DiagnosticsDescription.
    :type diagnostics: ~azure.mgmt.servicefabricmesh.models.DiagnosticsRef
    """

    _validation = {
        'os_type': {'required': True},
        'code_packages': {'required': True},
    }

    _attribute_map = {
        'os_type': {'key': 'osType', 'type': 'str'},
        'code_packages': {'key': 'codePackages', 'type': '[ContainerCodePackageProperties]'},
        'network_refs': {'key': 'networkRefs', 'type': '[NetworkRef]'},
        'diagnostics': {'key': 'diagnostics', 'type': 'DiagnosticsRef'},
    }

    def __init__(self, *, os_type, code_packages, network_refs=None, diagnostics=None, **kwargs) -> None:
        super(ServiceReplicaProperties, self).__init__(**kwargs)
        self.os_type = os_type
        self.code_packages = code_packages
        self.network_refs = network_refs
        self.diagnostics = diagnostics
