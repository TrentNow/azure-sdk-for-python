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


class SecretResourceDescription(Model):
    """This type describes a secret resource.

    All required parameters must be populated in order to send to Azure.

    :param properties: Required. Describes the properties of a secret
     resource.
    :type properties: ~azure.servicefabric.models.SecretResourceProperties
    :param name: Required. Name of the Secret resource.
    :type name: str
    """

    _validation = {
        'properties': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'properties': {'key': 'properties', 'type': 'SecretResourceProperties'},
        'name': {'key': 'name', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(SecretResourceDescription, self).__init__(**kwargs)
        self.properties = kwargs.get('properties', None)
        self.name = kwargs.get('name', None)
