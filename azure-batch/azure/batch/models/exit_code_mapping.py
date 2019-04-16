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


class ExitCodeMapping(Model):
    """How the Batch service should respond if a task exits with a particular exit
    code.

    All required parameters must be populated in order to send to Azure.

    :param code: Required. A process exit code.
    :type code: int
    :param exit_options: Required. How the Batch service should respond if the
     task exits with this exit code.
    :type exit_options: ~azure.batch.models.ExitOptions
    """

    _validation = {
        'code': {'required': True},
        'exit_options': {'required': True},
    }

    _attribute_map = {
        'code': {'key': 'code', 'type': 'int'},
        'exit_options': {'key': 'exitOptions', 'type': 'ExitOptions'},
    }

    def __init__(self, **kwargs):
        super(ExitCodeMapping, self).__init__(**kwargs)
        self.code = kwargs.get('code', None)
        self.exit_options = kwargs.get('exit_options', None)
