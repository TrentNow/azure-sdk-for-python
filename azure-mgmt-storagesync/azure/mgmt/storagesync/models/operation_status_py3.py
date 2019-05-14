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


class OperationStatus(Model):
    """Operation status object.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar name: Operation Id
    :vartype name: str
    :ivar status: Operation status
    :vartype status: str
    :ivar start_time: Start time of the operation
    :vartype start_time: datetime
    :ivar end_time: End time of the operation
    :vartype end_time: datetime
    :ivar error: Error details.
    :vartype error: ~azure.mgmt.storagesync.models.StorageSyncApiError
    """

    _validation = {
        'name': {'readonly': True},
        'status': {'readonly': True},
        'start_time': {'readonly': True},
        'end_time': {'readonly': True},
        'error': {'readonly': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'start_time': {'key': 'startTime', 'type': 'iso-8601'},
        'end_time': {'key': 'endTime', 'type': 'iso-8601'},
        'error': {'key': 'error', 'type': 'StorageSyncApiError'},
    }

    def __init__(self, **kwargs) -> None:
        super(OperationStatus, self).__init__(**kwargs)
        self.name = None
        self.status = None
        self.start_time = None
        self.end_time = None
        self.error = None
