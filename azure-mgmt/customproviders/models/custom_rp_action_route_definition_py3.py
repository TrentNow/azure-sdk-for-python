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

from .custom_rp_route_definition_py3 import CustomRPRouteDefinition


class CustomRPActionRouteDefinition(CustomRPRouteDefinition):
    """The route definition for an action implemented by the custom resource
    provider.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The name of the route definition. This becomes the
     name for the ARM extension (e.g.
     '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.CustomProviders/resourceProviders/{resourceProviderName}/{name}')
    :type name: str
    :param endpoint: Required. The route definition endpoint URI that the
     custom resource provider will proxy requests to. This can be in the form
     of a flat URI (e.g. 'https://testendpoint/') or can specify to route via a
     path (e.g. 'https://testendpoint/{requestPath}')
    :type endpoint: str
    :param routing_type: The routing types that are supported for action
     requests. Possible values include: 'Proxy'
    :type routing_type: str or ~microsoft.customproviders.models.ActionRouting
    """

    _validation = {
        'name': {'required': True},
        'endpoint': {'required': True, 'pattern': r'^https://.+'},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'endpoint': {'key': 'endpoint', 'type': 'str'},
        'routing_type': {'key': 'routingType', 'type': 'str'},
    }

    def __init__(self, *, name: str, endpoint: str, routing_type=None, **kwargs) -> None:
        super(CustomRPActionRouteDefinition, self).__init__(name=name, endpoint=endpoint, **kwargs)
        self.routing_type = routing_type
