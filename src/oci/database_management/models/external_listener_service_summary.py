# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalListenerServiceSummary(object):
    """
    The summary of a service registered with an external listener.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalListenerServiceSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ExternalListenerServiceSummary.
        :type name: str

        :param listener_id:
            The value to assign to the listener_id property of this ExternalListenerServiceSummary.
        :type listener_id: str

        :param managed_database_id:
            The value to assign to the managed_database_id property of this ExternalListenerServiceSummary.
        :type managed_database_id: str

        """
        self.swagger_types = {
            'name': 'str',
            'listener_id': 'str',
            'managed_database_id': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'listener_id': 'listenerId',
            'managed_database_id': 'managedDatabaseId'
        }

        self._name = None
        self._listener_id = None
        self._managed_database_id = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ExternalListenerServiceSummary.
        The name of the service.


        :return: The name of this ExternalListenerServiceSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ExternalListenerServiceSummary.
        The name of the service.


        :param name: The name of this ExternalListenerServiceSummary.
        :type: str
        """
        self._name = name

    @property
    def listener_id(self):
        """
        Gets the listener_id of this ExternalListenerServiceSummary.
        The `OCID`__ of the external listener.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The listener_id of this ExternalListenerServiceSummary.
        :rtype: str
        """
        return self._listener_id

    @listener_id.setter
    def listener_id(self, listener_id):
        """
        Sets the listener_id of this ExternalListenerServiceSummary.
        The `OCID`__ of the external listener.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param listener_id: The listener_id of this ExternalListenerServiceSummary.
        :type: str
        """
        self._listener_id = listener_id

    @property
    def managed_database_id(self):
        """
        Gets the managed_database_id of this ExternalListenerServiceSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The managed_database_id of this ExternalListenerServiceSummary.
        :rtype: str
        """
        return self._managed_database_id

    @managed_database_id.setter
    def managed_database_id(self, managed_database_id):
        """
        Sets the managed_database_id of this ExternalListenerServiceSummary.
        The `OCID`__ of the Managed Database.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param managed_database_id: The managed_database_id of this ExternalListenerServiceSummary.
        :type: str
        """
        self._managed_database_id = managed_database_id

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other