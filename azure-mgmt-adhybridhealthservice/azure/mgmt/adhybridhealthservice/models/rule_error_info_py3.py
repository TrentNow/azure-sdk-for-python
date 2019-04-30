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


class RuleErrorInfo(Model):
    """The error details in legacy rule processing.

    :param attribute_mapping: The attribute mapping details.
    :type attribute_mapping:
     ~azure.mgmt.adhybridhealthservice.models.AttributeMapping
    :param connector_id: The connector Id.
    :type connector_id: str
    :param connector_name: The connector name.
    :type connector_name: str
    :param cs_object_id: The object Id.
    :type cs_object_id: str
    :param dn: The distinguished name.
    :type dn: str
    """

    _attribute_map = {
        'attribute_mapping': {'key': 'attributeMapping', 'type': 'AttributeMapping'},
        'connector_id': {'key': 'connectorId', 'type': 'str'},
        'connector_name': {'key': 'connectorName', 'type': 'str'},
        'cs_object_id': {'key': 'csObjectId', 'type': 'str'},
        'dn': {'key': 'dn', 'type': 'str'},
    }

    def __init__(self, *, attribute_mapping=None, connector_id: str=None, connector_name: str=None, cs_object_id: str=None, dn: str=None, **kwargs) -> None:
        super(RuleErrorInfo, self).__init__(**kwargs)
        self.attribute_mapping = attribute_mapping
        self.connector_id = connector_id
        self.connector_name = connector_name
        self.cs_object_id = cs_object_id
        self.dn = dn
