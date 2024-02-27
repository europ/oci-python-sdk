# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909

from .connector_plugin import ConnectorPlugin
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetConnectorPlugin(ConnectorPlugin):
    """
    A connector plugin for sending data to a target service.
    For configuration instructions, see
    `Creating a Connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/create-service-connector.htm
    """

    def __init__(self, **kwargs):
        """
        Initializes a new TargetConnectorPlugin object with values from keyword arguments. The default value of the :py:attr:`~oci.sch.models.TargetConnectorPlugin.kind` attribute
        of this class is ``TARGET`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this TargetConnectorPlugin.
            Allowed values for this property are: "SOURCE", "TARGET"
        :type kind: str

        :param name:
            The value to assign to the name property of this TargetConnectorPlugin.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this TargetConnectorPlugin.
        :type time_created: datetime

        :param estimated_throughput:
            The value to assign to the estimated_throughput property of this TargetConnectorPlugin.
            Allowed values for this property are: "LOW", "MEDIUM", "HIGH", "UNKNOWN"
        :type estimated_throughput: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TargetConnectorPlugin.
            Allowed values for this property are: "ACTIVE", "DELETED"
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this TargetConnectorPlugin.
        :type display_name: str

        :param schema:
            The value to assign to the schema property of this TargetConnectorPlugin.
        :type schema: str

        """
        self.swagger_types = {
            'kind': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'estimated_throughput': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str',
            'schema': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'name': 'name',
            'time_created': 'timeCreated',
            'estimated_throughput': 'estimatedThroughput',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName',
            'schema': 'schema'
        }

        self._kind = None
        self._name = None
        self._time_created = None
        self._estimated_throughput = None
        self._lifecycle_state = None
        self._display_name = None
        self._schema = None
        self._kind = 'TARGET'

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
