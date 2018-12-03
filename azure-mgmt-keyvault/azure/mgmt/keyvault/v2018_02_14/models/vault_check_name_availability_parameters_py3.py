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


class VaultCheckNameAvailabilityParameters(Model):
    """The parameters used to check the availability of the vault name.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    All required parameters must be populated in order to send to Azure.

    :param name: Required. The vault name.
    :type name: str
    :ivar type: Required. The type of resource, Microsoft.KeyVault/vaults.
     Default value: "Microsoft.KeyVault/vaults" .
    :vartype type: str
    """

    _validation = {
        'name': {'required': True},
        'type': {'required': True, 'constant': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
    }

    type = "Microsoft.KeyVault/vaults"

    def __init__(self, *, name: str, **kwargs) -> None:
        super(VaultCheckNameAvailabilityParameters, self).__init__(**kwargs)
        self.name = name
