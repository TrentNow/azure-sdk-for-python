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

from .proxy_resource_py3 import ProxyResource


class ServiceResource(ProxyResource):
    """The service resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Azure resource identifier.
    :vartype id: str
    :ivar name: Azure resource name.
    :vartype name: str
    :ivar type: Azure resource type.
    :vartype type: str
    :param location: Azure resource location.
    :type location: str
    :param tags: Azure resource tags.
    :type tags: dict[str, str]
    :ivar etag: Azure resource etag.
    :vartype etag: str
    :param placement_constraints: The placement constraints as a string.
     Placement constraints are boolean expressions on node properties and allow
     for restricting a service to particular nodes based on the service
     requirements. For example, to place a service on nodes where NodeType is
     blue specify the following: "NodeColor == blue)".
    :type placement_constraints: str
    :param correlation_scheme: A list that describes the correlation of the
     service with other services.
    :type correlation_scheme:
     list[~azure.mgmt.servicefabric.models.ServiceCorrelationDescription]
    :param service_load_metrics: The service load metrics is given as an array
     of ServiceLoadMetricDescription objects.
    :type service_load_metrics:
     list[~azure.mgmt.servicefabric.models.ServiceLoadMetricDescription]
    :param service_placement_policies: A list that describes the correlation
     of the service with other services.
    :type service_placement_policies:
     list[~azure.mgmt.servicefabric.models.ServicePlacementPolicyDescription]
    :param default_move_cost: Specifies the move cost for the service.
     Possible values include: 'Zero', 'Low', 'Medium', 'High'
    :type default_move_cost: str or ~azure.mgmt.servicefabric.models.MoveCost
    :ivar provisioning_state: The current deployment or provisioning state,
     which only appears in the response
    :vartype provisioning_state: str
    :param service_type_name: The name of the service type
    :type service_type_name: str
    :param partition_description: Describes how the service is partitioned.
    :type partition_description:
     ~azure.mgmt.servicefabric.models.PartitionSchemeDescription
    :param service_package_activation_mode: The activation Mode of the service
     package. Possible values include: 'SharedProcess', 'ExclusiveProcess'
    :type service_package_activation_mode: str or
     ~azure.mgmt.servicefabric.models.ArmServicePackageActivationMode
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'etag': {'readonly': True},
        'provisioning_state': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'etag': {'key': 'etag', 'type': 'str'},
        'placement_constraints': {'key': 'properties.placementConstraints', 'type': 'str'},
        'correlation_scheme': {'key': 'properties.correlationScheme', 'type': '[ServiceCorrelationDescription]'},
        'service_load_metrics': {'key': 'properties.serviceLoadMetrics', 'type': '[ServiceLoadMetricDescription]'},
        'service_placement_policies': {'key': 'properties.servicePlacementPolicies', 'type': '[ServicePlacementPolicyDescription]'},
        'default_move_cost': {'key': 'properties.defaultMoveCost', 'type': 'str'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'service_type_name': {'key': 'properties.serviceTypeName', 'type': 'str'},
        'partition_description': {'key': 'properties.partitionDescription', 'type': 'PartitionSchemeDescription'},
        'service_package_activation_mode': {'key': 'properties.servicePackageActivationMode', 'type': 'str'},
    }

    def __init__(self, *, location: str=None, tags=None, placement_constraints: str=None, correlation_scheme=None, service_load_metrics=None, service_placement_policies=None, default_move_cost=None, service_type_name: str=None, partition_description=None, service_package_activation_mode=None, **kwargs) -> None:
        super(ServiceResource, self).__init__(location=location, tags=tags, **kwargs)
        self.placement_constraints = placement_constraints
        self.correlation_scheme = correlation_scheme
        self.service_load_metrics = service_load_metrics
        self.service_placement_policies = service_placement_policies
        self.default_move_cost = default_move_cost
        self.provisioning_state = None
        self.service_type_name = service_type_name
        self.partition_description = partition_description
        self.service_package_activation_mode = service_package_activation_mode
