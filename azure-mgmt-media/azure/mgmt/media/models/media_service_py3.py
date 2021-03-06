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

from .tracked_resource_py3 import TrackedResource


class MediaService(TrackedResource):
    """A Media Services account.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Fully qualified resource ID for the resource.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource.
    :vartype type: str
    :param tags: Resource tags.
    :type tags: dict[str, str]
    :param location: The Azure Region of the resource.
    :type location: str
    :ivar media_service_id: The Media Services account ID.
    :vartype media_service_id: str
    :param storage_accounts: The storage accounts for this resource.
    :type storage_accounts: list[~azure.mgmt.media.models.StorageAccount]
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'media_service_id': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'tags': {'key': 'tags', 'type': '{str}'},
        'location': {'key': 'location', 'type': 'str'},
        'media_service_id': {'key': 'properties.mediaServiceId', 'type': 'str'},
        'storage_accounts': {'key': 'properties.storageAccounts', 'type': '[StorageAccount]'},
    }

    def __init__(self, *, tags=None, location: str=None, storage_accounts=None, **kwargs) -> None:
        super(MediaService, self).__init__(tags=tags, location=location, **kwargs)
        self.media_service_id = None
        self.storage_accounts = storage_accounts
