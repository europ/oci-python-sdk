# coding: utf-8
# Copyright (c) 2016, 2024, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

# NOTE: This class is auto generated by OracleSDKGenerator. DO NOT EDIT. API Version: 20200909


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ConnectorPluginSummary(object):
    """
    Summary information for a connector plugin.
    Example connector plugins include the Streaming source and the Notifications target.
    For more information about flows defined by connectors, see
    `Overview of Connector Hub`__.
    For configuration instructions, see
    `Creating a Connector`__.

    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/overview.htm
    __ https://docs.cloud.oracle.com/iaas/Content/connector-hub/create-service-connector.htm
    """

    #: A constant which can be used with the kind property of a ConnectorPluginSummary.
    #: This constant has a value of "SOURCE"
    KIND_SOURCE = "SOURCE"

    #: A constant which can be used with the kind property of a ConnectorPluginSummary.
    #: This constant has a value of "TARGET"
    KIND_TARGET = "TARGET"

    #: A constant which can be used with the estimated_throughput property of a ConnectorPluginSummary.
    #: This constant has a value of "LOW"
    ESTIMATED_THROUGHPUT_LOW = "LOW"

    #: A constant which can be used with the estimated_throughput property of a ConnectorPluginSummary.
    #: This constant has a value of "MEDIUM"
    ESTIMATED_THROUGHPUT_MEDIUM = "MEDIUM"

    #: A constant which can be used with the estimated_throughput property of a ConnectorPluginSummary.
    #: This constant has a value of "HIGH"
    ESTIMATED_THROUGHPUT_HIGH = "HIGH"

    #: A constant which can be used with the estimated_throughput property of a ConnectorPluginSummary.
    #: This constant has a value of "UNKNOWN"
    ESTIMATED_THROUGHPUT_UNKNOWN = "UNKNOWN"

    #: A constant which can be used with the lifecycle_state property of a ConnectorPluginSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ConnectorPluginSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    def __init__(self, **kwargs):
        """
        Initializes a new ConnectorPluginSummary object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.sch.models.SourceConnectorPluginSummary`
        * :class:`~oci.sch.models.TargetConnectorPluginSummary`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param kind:
            The value to assign to the kind property of this ConnectorPluginSummary.
            Allowed values for this property are: "SOURCE", "TARGET", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type kind: str

        :param name:
            The value to assign to the name property of this ConnectorPluginSummary.
        :type name: str

        :param time_created:
            The value to assign to the time_created property of this ConnectorPluginSummary.
        :type time_created: datetime

        :param estimated_throughput:
            The value to assign to the estimated_throughput property of this ConnectorPluginSummary.
            Allowed values for this property are: "LOW", "MEDIUM", "HIGH", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type estimated_throughput: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ConnectorPluginSummary.
            Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param display_name:
            The value to assign to the display_name property of this ConnectorPluginSummary.
        :type display_name: str

        """
        self.swagger_types = {
            'kind': 'str',
            'name': 'str',
            'time_created': 'datetime',
            'estimated_throughput': 'str',
            'lifecycle_state': 'str',
            'display_name': 'str'
        }

        self.attribute_map = {
            'kind': 'kind',
            'name': 'name',
            'time_created': 'timeCreated',
            'estimated_throughput': 'estimatedThroughput',
            'lifecycle_state': 'lifecycleState',
            'display_name': 'displayName'
        }

        self._kind = None
        self._name = None
        self._time_created = None
        self._estimated_throughput = None
        self._lifecycle_state = None
        self._display_name = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['kind']

        if type == 'SOURCE':
            return 'SourceConnectorPluginSummary'

        if type == 'TARGET':
            return 'TargetConnectorPluginSummary'
        else:
            return 'ConnectorPluginSummary'

    @property
    def kind(self):
        """
        **[Required]** Gets the kind of this ConnectorPluginSummary.
        The plugin type discriminator.

        Allowed values for this property are: "SOURCE", "TARGET", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The kind of this ConnectorPluginSummary.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """
        Sets the kind of this ConnectorPluginSummary.
        The plugin type discriminator.


        :param kind: The kind of this ConnectorPluginSummary.
        :type: str
        """
        allowed_values = ["SOURCE", "TARGET"]
        if not value_allowed_none_or_none_sentinel(kind, allowed_values):
            kind = 'UNKNOWN_ENUM_VALUE'
        self._kind = kind

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ConnectorPluginSummary.
        The service to be called by the connector plugin.


        :return: The name of this ConnectorPluginSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ConnectorPluginSummary.
        The service to be called by the connector plugin.


        :param name: The name of this ConnectorPluginSummary.
        :type: str
        """
        self._name = name

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ConnectorPluginSummary.
        The date and time when this plugin became available.
        Format is defined by `RFC3339`__.
        Example: `2023-09-10T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this ConnectorPluginSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ConnectorPluginSummary.
        The date and time when this plugin became available.
        Format is defined by `RFC3339`__.
        Example: `2023-09-10T21:10:29.600Z`

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this ConnectorPluginSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def estimated_throughput(self):
        """
        Gets the estimated_throughput of this ConnectorPluginSummary.
        The estimated throughput range (LOW, MEDIUM, HIGH).

        Allowed values for this property are: "LOW", "MEDIUM", "HIGH", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The estimated_throughput of this ConnectorPluginSummary.
        :rtype: str
        """
        return self._estimated_throughput

    @estimated_throughput.setter
    def estimated_throughput(self, estimated_throughput):
        """
        Sets the estimated_throughput of this ConnectorPluginSummary.
        The estimated throughput range (LOW, MEDIUM, HIGH).


        :param estimated_throughput: The estimated_throughput of this ConnectorPluginSummary.
        :type: str
        """
        allowed_values = ["LOW", "MEDIUM", "HIGH", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(estimated_throughput, allowed_values):
            estimated_throughput = 'UNKNOWN_ENUM_VALUE'
        self._estimated_throughput = estimated_throughput

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ConnectorPluginSummary.
        The current state of the service connector.

        Allowed values for this property are: "ACTIVE", "DELETED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ConnectorPluginSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ConnectorPluginSummary.
        The current state of the service connector.


        :param lifecycle_state: The lifecycle_state of this ConnectorPluginSummary.
        :type: str
        """
        allowed_values = ["ACTIVE", "DELETED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ConnectorPluginSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :return: The display_name of this ConnectorPluginSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ConnectorPluginSummary.
        A user-friendly name. It does not have to be unique, and it is changeable.
        Avoid entering confidential information.


        :param display_name: The display_name of this ConnectorPluginSummary.
        :type: str
        """
        self._display_name = display_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other