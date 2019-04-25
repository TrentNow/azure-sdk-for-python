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

from .resource import Resource


class ConfigurationStore(Resource):
    """The configuration store along with all resource properties. The
    Configuration Store will have all information to begin utilizing it.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: The resource ID.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param location: Required. The location of the resource. This cannot be
     changed after the resource is created.
    :type location: str
    :param tags: The tags of the resource.
    :type tags: dict[str, str]
    :ivar provisioning_state: The provisioning state of the configuration
     store. Possible values include: 'Creating', 'Updating', 'Deleting',
     'Succeeded', 'Failed', 'Canceled'
    :vartype provisioning_state: str or
     ~azure.mgmt.appconfiguration.models.ProvisioningState
    :ivar creation_date: The creation date of configuration store.
    :vartype creation_date: datetime
    :ivar endpoint: The DNS endpoint where the configuration store API will be
     available.
    :vartype endpoint: str
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'location': {'required': True},
        'provisioning_state': {'readonly': True},
        'creation_date': {'readonly': True},
        'endpoint': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'location': {'key': 'location', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'provisioning_state': {'key': 'properties.provisioningState', 'type': 'str'},
        'creation_date': {'key': 'properties.creationDate', 'type': 'iso-8601'},
        'endpoint': {'key': 'properties.endpoint', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(ConfigurationStore, self).__init__(**kwargs)
        self.provisioning_state = None
        self.creation_date = None
        self.endpoint = None
